#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import re
import sre_constants
from io import open
from .__burp__ import BURP

if not BURP:
    from requests import get
    from requests.utils import dict_from_cookiejar
    from requests.structures import CaseInsensitiveDict
    from requests.exceptions import RequestException

    # Disable warning about Insecure SSL
    from requests.packages.urllib3 import disable_warnings
    from requests.packages.urllib3.util import parse_url
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    disable_warnings(InsecureRequestWarning)

from . import encoder
from .utils import ConnectionException, FileNotFoundException, WrongContentTypeException, Format, Tech, caseinsensitive_in, dict_from_caseinsensitivedict
from .parser import WTParser

# Hacky hack to hack ack. Support python2 and python3 without depending on six
if sys.version_info[0] > 2:
    unicode = str


def parse_regex_string(string):
    """
    Parse header string according to wappalizer DB format

    strings follow the below format:
    <string>[\\;version:\\\d][\\;confidence:\d]

    "string" is a mandatory regex string followed by 0 or more parameters (key:value), can be empty
    parameters are divided by a \\; sequence (a backslash followed by a semicolon)

    examples of parameters are:
    "version": indicate wich regex group store the version information
    "confidence": indicate a rate of confidence
    """
    parts = string.split(r"\;")
    if len(parts) == 1:
        return parts[0], None
    else:
        extra = {}
        for p in parts[1:]:
            p = p.split(":")
            extra[p[0]] = p[1]
        return parts[0], extra


class Target():
    """
    This class represents a single Target (from scraping a page, from a response file, from a replayed request or from a JSON request-response exchange)

    The only self attributes MUST be self.data that contains the fetched data and self.report that contains the results from various checks.response

    Every function MUST do only 1 action since we are need to parallelize this and all the data must be source-independent
    """
    def __init__(self):
        # self.data contains the data fetched from the request
        # this object SHOULD be append-only and immutable after the scraping/whitelist process
        self.data = {
            'url': None,
            'html': None,
            'headers': {},
            'cookies': {},
            'meta': {},
            'script': {}
        }

        # self.report contains the information about the technologies detected
        self.report = {
            'tech': set(),
            'headers': [],
        }

    def scrape_url(self, url, headers={}, cookies={}, timeout=10):
        """
        Scrape the target URL and collects all the data that will be filtered afterwards
        """
        if BURP:
            # Burp flag is set when requests is not installed.
            # When using Burp we shouldn't end up in this function so we are in a Python CLI env without requests
            raise ImportError("Missing Requests module")

        # By default we don't verify SSL certificates, we are only performing some useless GETs
        try:
            response = get(url, headers=headers, cookies=cookies, verify=False, allow_redirects=True, timeout=timeout)
        except RequestException as e:
            raise ConnectionException(e)
        # print("status: {}".format(response.status_code))

        # TODO: switch-case for various response.status_code

        ct = response.headers.get('Content-Type', None)
        if ct is None or not 'text/html' in ct:
            raise WrongContentTypeException('{} response use Content-Type "{}" but "text/html" is needed'.format(url, ct))

        self.data['url'] = url
        self.data['html'] = response.text
        self.data['headers'] = dict_from_caseinsensitivedict(response.headers)
        self.data['cookies'] = dict_from_cookiejar(response.cookies)
        self.parse_html_page()

    def parse_http_file(self, url):
        """
        Receives an HTTP request/response file and redirect to request/response parsing
        """
        path = url.replace('file://', '')
        data = open(path, encoding="ISO-8859-1").read()

        # e.g. HTTP/1.1 200 OK -> that's a response!
        # does not check HTTP/1 since it might be HTTP/2 :)
        if data.startswith("HTTP/"):
            # BUG: path is not a reliable information. url matching will always fail
            self.data['url'] = path
            return self.parse_http_response(data)
        elif "HTTP/" in data.split('\n')[0]:
            return self.parse_http_request(data)
        else:
            raise ValueError("The supplied file is not an HTTP Request or an HTTP Response. The file content is missing HTTP headers")

    def parse_http_response(self, response):
        """
        Parse an HTTP response file and collects all the data that will be filtered afterwards

        TODO: find a better way to do this :(
        """
        response = response.replace('\r', '')
        headers_raw, self.data['html'] = response.split('\n\n', 1)
        self.data['cookies'] = {}
        for header in headers_raw.split('\n'):
            header = [x.strip() for x in header.split(":", 1)]
            # might be first row: HTTP/1.1 200
            if len(header) != 2:
                continue
            if "set-cookie" in header[0].lower():
                # 'Set-Cookie: dr=gonzo; path=/trmon'
                cookie = [x.strip() for x in header[1].split(";", 1)[0].split("=", 1)]
                # BUG: if there are cookies for different domains with the same name
                # they are going to be overwritten (last occurrence will last)...
                # ¯\_(ツ)_/¯
                self.data['cookies'][cookie[0]] = cookie[1]
            else:
                self.data['headers'][header[0].lower()] = (header[1], header[0])

        self.parse_html_page()

    def parse_http_request(self, request, replay=True):
        """
        Parse an HTTP request file and collects all the headers

        TODO: find a better way to do this :(
        TODO: should we support POST request?
        """
        # GET / HTTP/1.1 -> /
        request = request.replace('\r', '')
        replay_uri = request.split('\n', 1)[0].split(" ")[1]
        replay_headers = {}
        replay_cookies = {}

        headers_raw = request.split('\n\n', 1)[0]
        for header in headers_raw.split('\n'):
            header = [x.strip() for x in header.split(":", 1)]
            # might be first row: GET / HTTP/1.1
            if len(header) != 2:
                continue
            if "cookie" not in header[0].lower():
                if "host" in header[0].lower():
                    host = header[1]
                else:
                    replay_headers[header[0]] = header[1]
            else:
                # 'Cookie: dr=gonzo; mamm=ta; trmo=n'
                for cookie in header[1].split(';'):
                    cookie = [x.strip() for x in cookie.split("=", 1)]
                    # BUG: if there are cookies for different domains with the same name
                    # they are going to be overwritten (last occurrence will last)...
                    # ¯\_(ツ)_/¯
                    replay_cookies[cookie[0]] = cookie[1]

        # BUG: we don't know for sure if it's through HTTP or HTTPS
        replay_url = "https://" + host + replay_uri
        if replay:
            self.scrape_url(replay_url, headers=replay_headers, cookies=replay_cookies)
        else:
            # The URL is the only usefull information when parsing a request without replaying it
            self.data['url'] = replay_url

    def parse_html_page(self):
        """
        Parse HTML content to get meta tag and script-src
        """
        p = WTParser()
        p.feed(self.data['html'])
        self.data['meta'] = p.meta
        self.data['script'] = p.scripts
        p.close()

    def whitelist_data(self, common_headers):
        """
        Whitelist collected data to report the important/uncommon data BEFORE matching with the database

        This function is useful for CMS/technologies that are not in the database
        """
        for key, value in self.data['headers'].items():
            if key not in common_headers:
                # In value[1] it's stored the original header name
                self.report['headers'].append({"name": value[1], "value": value[0]})

    def check_html(self, tech, html):
        """
        Check if request html contains some database matches
        """
        if isinstance(html, str) or isinstance(html, unicode):
            html = [html]

        for source in html:
            # Parse the matching regex
            attr, extra = parse_regex_string(source)
            matches = None
            try:
                matches = re.search(attr, self.data['html'], re.IGNORECASE)
            except sre_constants.error:
                pass
            if matches is not None:
                matched_tech = Tech(name=tech, version=None)
                # The version extra data is present
                if extra and 'version' in extra:
                    if matches.group(1):
                        matched_tech = matched_tech._replace(version=matches.group(1))
                self.report['tech'].add(matched_tech)
                # this tech is matched, GOTO next
                return

    def check_headers(self, tech, headers):
        """
        Check if request headers match some database headers
        """
        if not isinstance(headers, dict):
            raise ValueError('Invalid headers data in database: {}'.format(headers))

        # For every tech header check if there is a match in our target
        for header in headers:
            content = self.data['headers'].get(header.lower())
            if content is None:
                # Tech not found
                return
            else:
                # Get the real content
                content = content[0]
            # Parse the matching regex
            attr, extra = parse_regex_string(headers[header])
            matches = re.search(attr, content, re.IGNORECASE)
            # Attr is empty for a "generic" tech header
            if attr == '' or matches is not None:
                matched_tech = Tech(name=tech, version=None)
                # The version extra data is present
                if extra and 'version' in extra:
                    if matches.group(1):
                        matched_tech = matched_tech._replace(version=matches.group(1))
                self.report['tech'].add(matched_tech)
                # remove ALL the tech headers from the Custom Header list
                # first make a list of tech headers
                tech_headers = list(map(str, headers.keys()))
                # then filter them in target headers case insensitively
                self.report['headers'] = list(filter(lambda h: not caseinsensitive_in(str(h['name']), tech_headers), self.report['headers']))
                # this tech is matched, GOTO next
                return

    def check_meta(self, tech, meta):
        """
        Check if request meta from page's HTML contains some database matches
        """
        for m in meta:
            content = self.data['meta'].get(m)
            # filter not-available meta
            if content is None:
                continue
            if type(meta[m])==list:
                strings_to_check=meta[m]
            else:
                strings_to_check=[meta[m]]
            for str_to_check in strings_to_check:
                attr, extra = parse_regex_string(str_to_check)
                matches = re.search(attr, content, re.IGNORECASE)
                # Attr is empty for a "generic" tech meta
                if attr == '' or matches is not None:
                    matched_tech = Tech(name=tech, version=None)
                    # The version extra data is present
                    if extra and 'version' in extra:
                        if matches.group(1):
                            matched_tech = matched_tech._replace(version=matches.group(1))
                    self.report['tech'].add(matched_tech)
                    # this tech is matched, GOTO next
                    continue

    def check_script(self, tech, script):
        """
        Check if request script src from page's HTML contains some database matches
        """
        # FIX repair to some database inconsistencies
        if isinstance(script, str) or isinstance(script, unicode):
            script = [script]

        for source in script:
            attr, extra = parse_regex_string(source)
            for src in self.data['script']:
                matches = re.search(attr, src, re.IGNORECASE)
                # Attr is empty for a "generic" tech meta
                if attr == '' or matches is not None:
                    matched_tech = Tech(name=tech, version=None)
                    # The version extra data is present
                    if extra and 'version' in extra:
                        if matches.group(1):
                            matched_tech = matched_tech._replace(version=matches.group(1))
                    self.report['tech'].add(matched_tech)
                    # this tech is matched, GOTO next
                    return

    def check_cookies(self, tech, cookies):
        """
        Check if request cookies match some database cookies
        """
        for cookie in cookies:
            # cookies in db are regexes so we must test them all
            cookie = cookie.replace("*","") # FIX for "Fe26.2**" hapi.js cookie in the database
            for biscuit in self.data['cookies'].keys():
                matches = re.search(cookie, biscuit, re.IGNORECASE)
                if matches is not None:
                    if cookies[cookie] != '':
                        # Let's check the cookie content
                        content = self.data['cookies'][biscuit]
                        matches = re.search(cookies[cookie], content, re.IGNORECASE)
                        if matches is None:
                            # No match, exit
                            return
                    matched_tech = Tech(name=tech, version=None)
                    self.report['tech'].add(matched_tech)
                    # this tech is matched, GOTO next
                    return

    def check_url(self, tech, url):
        """
        Check if request url match some database url rules
        """
        if isinstance(url, str) or isinstance(url, unicode):
            url = [url]

        for source in url:
            matches = re.search(source, self.data['url'], re.IGNORECASE)
            if matches is not None:
                matched_tech = Tech(name=tech, version=None)
                self.report['tech'].add(matched_tech)
                # this tech is matched, GOTO next
                return

    def generate_report(self, output_format):
        """
        Generate a report
        """
        if output_format == Format['grep']:
            techs = ""
            for tech in self.report['tech']:
                if len(techs): techs += "//"
                techs += "{}/{}".format(tech.name, 'unknown' if tech.version is None else tech.version)

            headers = ""
            for header in self.report['headers']:
                if len(headers): headers += "//"
                headers += "{}:{}".format(header["name"], header["value"])

            return "Url>{}\tTechs>{}\tHeaders>{}".format(self.data['url'], techs, headers)
        elif output_format == Format['json']:
            return json.loads(json.dumps(self.report, cls=encoder.Encoder))
        else:
            retval = ""
            retval += "Target URL: {}\n".format(self.data['url'])
            if self.report['tech']:
                retval += "Detected technologies:\n"
                for tech in self.report['tech']:
                    retval += "\t- {} {}\n".format(tech.name, '' if tech.version is None else tech.version)
            if self.report['headers']:
                retval += "Detected the following interesting custom headers:\n"
                for header in self.report['headers']:
                    retval += "\t- {}: {}\n".format(header["name"], header["value"])
            return retval
