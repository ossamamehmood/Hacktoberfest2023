#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from io import open
import json
import random
try:
    from urlparse import urlparse
except ImportError:  # For Python 3
    from urllib.parse import urlparse

from .__burp__ import BURP
from . import database
from .utils import Format, FileNotFoundException, ConnectionException, WrongContentTypeException
from .target import Target
from .__version__ import __version__ as VERSION


def default_user_agent():
    return "webtech/{}".format(VERSION)

def get_random_user_agent():
    """
    Get a random user agent from a file
    """
    ua_file = os.path.join(os.path.realpath(os.path.dirname(__file__)), "ua.txt")
    try:
        with open(ua_file, 'r', encoding='utf8') as f:
            agents = f.readlines()
            return random.choice(agents).strip()
    except FileNotFoundException as e:
        print(e)
        print('Please: Reinstall webtech correctly or provide a valid User-Agent list')
        exit(-1)


class WebTech():
    """
    Main class. The orchestrator that decides what to do.

    This class is the bridge between the tech's database and the Targets' data
    """
    COMMON_HEADERS = ['Accept-Ranges', 'Access-Control-Allow-Methods', 'Access-Control-Allow-Origin', 'Age', 'Cache-Control', 'Connection',
                      'Content-Encoding', 'Content-Language', 'Content-Length', 'Content-Security-Policy', 'Content-Type', 'Date', 'ETag', 'Expect-CT', 'Expires',
                      'Feature-Policy', 'Permissions-Policy', 'Keep-Alive', 'Last-Modified', 'Link', 'Location', 'P3P', 'Pragma', 'Referrer-Policy', 'Set-Cookie',
                      'Strict-Transport-Security', 'Transfer-Encoding', 'Vary', 'X-Accel-Buffering', 'X-Cache', 'X-Cache-Hits', 'X-Content-Security-Policy',
                      'X-Content-Type-Options', 'X-Frame-Options', 'X-Timer', 'X-WebKit-CSP', 'X-XSS-Protection']
    COMMON_HEADERS = [ch.lower() for ch in COMMON_HEADERS]

    # 'cats' tech categories
    # 'implies' website is using also this tech
    # 'excludes' exclude this tech
    # 'website' website for this tech
    # 'icon' icon for this tech (useless)

    # 'headers' check this pattern in headers
    # 'html' check this regex in html
    # 'meta' check this pattern in meta
    # 'js' check this expression in javascript context
    # 'cookies' check this pattern in cookies
    # 'script' check this pattern in scripts src
    # 'url' check this pattern in url

    def __init__(self, options=None):
        if not BURP:
            update = False if options is None else options.get('update_db', False)
            database.update_database(force=update)

        self.db = None
        if os.path.isfile(database.WAPPALYZER_DATABASE_FILE):
            with open(database.WAPPALYZER_DATABASE_FILE, 'r', encoding='utf8') as f:
                self.db = json.load(f)
        with open(database.DATABASE_FILE, 'r', encoding='utf8') as f:
            self.db = database.merge_databases(self.db, json.load(f))

        # Output text only
        self.output_format = Format['text']

        # Default user agent
        self.USER_AGENT = default_user_agent()

        if options is None:
            return

        if options.get('database_file'):
            try:
                with open(options.get('database_file'), 'r', encoding='utf8') as f:
                    self.db = database.merge_databases(self.db, json.load(f))
            except (FileNotFoundException, ValueError) as e:
                print(e)
                exit(-1)

        self.urls = options.get('urls') or []

        if options.get('urls_file'):
            try:
                with open(options.get('urls_file'), 'r', encoding='utf8') as f:
                    self.urls = [line.rstrip() for line in f]
            except FileNotFoundException as e:
                print(e)
                exit(-1)

        if options.get('user_agent'):
            self.USER_AGENT = options.get('user_agent')
        elif options.get('random_user_agent'):
            self.USER_AGENT = get_random_user_agent()

        if options.get('grep'):
            # Greppable output
            self.output_format = Format['grep']
        elif options.get('json'):
            # JSON output
            self.output_format = Format['json']

        self.auto_fallback = options.get('auto_fallback')

        try:
            self.timeout = int(options.get('timeout', '10'))
        except ValueError:
            self.timeout = 10

    def start(self):
        """
        Start the engine, fetch an URL and report the findings
        """
        self.output = {}
        self.auto_fallback = True
        for url in self.urls or []:
            try:
                temp_output = self.start_from_url(url)
            except (FileNotFoundException, ValueError) as e:
                print(e)
                continue
            except ConnectionException as e:
                print("Connection error while scanning {}".format(url))
                continue

            if self.output_format == Format['text']:
                print(temp_output)
            else:
                self.output[url] = temp_output

        if self.output_format == Format['json']:
            print(json.dumps(self.output))
        else:
            for o in self.output.values():
                print(o)

    def start_from_url(self, url, headers={}, timeout=None):
        """
        Start webtech on a single URL/target

        Returns the report for that specific target
        """
        timeout = timeout or self.timeout
        target = Target()

        parsed_url = urlparse(url)
        if "http" in parsed_url.scheme:
            # Scrape the URL by making a request
            h = {'User-Agent': self.USER_AGENT}
            h.update(headers)
            try:
                target.scrape_url(url, headers=h, cookies={}, timeout=timeout)
            except WrongContentTypeException as e:
                if self.auto_fallback:
                    print("Fallback to top level folder since response Content-Type is not text/html")
                    path = '/' + '/'.join(parsed_url.path.split('/')[:-1])
                    parsed_url = parsed_url._replace(path=path)
                    target.scrape_url(parsed_url.geturl(), headers=h, cookies={}, timeout=timeout)
                else: raise e
        elif "file" in parsed_url.scheme:
            # Load the file and read it
            target.parse_http_file(url)
        else:
            raise ValueError("Invalid scheme {} for URL {}. Only 'http', 'https' and 'file' are supported".format(parsed_url.scheme, url))

        return self.perform(target)

    def start_from_json(self, exchange):
        """
        Start webtech on a single target from a HTTP request-response exchange as JSON serialized string

        This function is the entry point for the Burp extension
        """
        return self.start_from_exchange(json.loads(exchange))

    def start_from_exchange(self, exchange):
        """
        Start webtech on a single target from a HTTP request-response exchange as Object
        """
        target = Target()

        target.parse_http_response(exchange['response'])
        target.parse_http_request(exchange['request'], replay=False)

        return self.perform(target)

    def perform(self, target):
        """
        Performs all the checks on the current target received as argument

        This function can be executed on multiple threads since "it doesn't access on shared data"
        """
        target.whitelist_data(self.COMMON_HEADERS)

        # Cycle through all the db technologies and do all the checks
        # It's more efficent cycling all technologies and match against the target once for tech
        # instead of cycling each target feature against every technology
        for tech in self.db["apps"]:
            t = self.db["apps"][tech]
            headers = t.get("headers")
            html = t.get("html")
            meta = t.get("meta")
            cookies = t.get("cookies")
            script = t.get("script")
            url = t.get("url")
            if headers:
                target.check_headers(tech, headers)
            if html:
                target.check_html(tech, html)
            if meta:
                target.check_meta(tech, meta)
            if cookies:
                target.check_cookies(tech, cookies)
            if script:
                target.check_script(tech, script)
            if url:
                target.check_url(tech, url)

        return target.generate_report(self.output_format)
