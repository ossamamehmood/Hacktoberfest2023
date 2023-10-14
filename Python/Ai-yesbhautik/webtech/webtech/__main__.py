#!/usr/bin/env python
import sys
from optparse import OptionParser

from .__version__ import __version__ as VERSION
from .webtech import WebTech


def split_on_comma(option, opt_str, value, parser):
    setattr(parser.values, option.dest, value.split(','))


def main():
    """
    Main function when running from command line.
    """
    parser = OptionParser(prog="webtech", version="%prog {}".format(VERSION))
    parser.add_option(
        "-u", "--urls",
        help="url(s) to scan", type="string", action="callback", callback=split_on_comma)
    parser.add_option(
        "--urls-file", "--ul",
        help="url(s) list file to scan", type="string")
    parser.add_option(
        "--user-agent", "--ua",
        help="use this user agent")
    parser.add_option(
        "--random-user-agent", "--rua", action="store_true",
        help="use a random user agent", default=False)
    parser.add_option(
        "--database-file", "--db",
        help="custom database file")
    parser.add_option(
        "--json", "--oj", action="store_true",
        help="output json-encoded report", default=False)
    parser.add_option(
        "--grep", "--og", action="store_true",
        help="output grepable report", default=False)
    parser.add_option(
        "--update-db", "--udb", action="store_true",
        help="force update of remote db files", default=False)
    parser.add_option(
        "--timeout", type="float", help="maximum timeout for scrape requests", default=10)

    (options, _args) = parser.parse_args(sys.argv)
    options = vars(options)

    if options.get('urls') is None and options.get('urls_file') is None and not options.get('update_db'):
        print("No URL(s) given!")
        parser.print_help()
        exit()

    wt = WebTech(options)
    wt.start()


if __name__ == "__main__":
    main()
