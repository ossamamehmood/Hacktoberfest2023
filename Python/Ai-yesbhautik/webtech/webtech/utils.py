#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from collections import namedtuple

try:
    FileNotFoundException = FileNotFoundError
except NameError:
    FileNotFoundException = IOError

Format = {
    'text': 0,
    'grep': 1,
    'json': 2
}

Tech = namedtuple('Tech', ['name', 'version'])


class ConnectionException(Exception):
    pass

class WrongContentTypeException(Exception):
    pass

def caseinsensitive_in(element, elist):
    """
    Given a list and an element, return true if the element is present in the list
    in a case-insensitive flavor
    """
    return element.lower() in map(str.lower, elist)

def dict_from_caseinsensitivedict(cidict):
    # This is pretty bad, but in Python2 we don't have CaseInsensitiveDict and with Burp we cannot use requests's implementation
    d = {}
    for key, value in cidict.items():
        d[key.lower()] = (value, key)
    return d

def user_data_dir(appname):
    system = system_platform()
    if system == "win32":
        path = os.path.normpath(os.path.expandvars(r'%APPDATA%'))
    elif system == 'darwin':
        path = os.path.expanduser('~/Library/Application Support/')
    else:
        path = os.getenv('XDG_DATA_HOME', os.path.expanduser("~/.local/share"))
    path = os.path.join(path, appname)
    return path

def system_platform():
    system = sys.platform
    if sys.platform.startswith('java'):
        import platform
        os_name = platform.java_ver()[3][0]
        if os_name.startswith('Windows'): # "Windows XP", "Windows 7", etc.
            system = 'win32'
        elif os_name.startswith('Mac'): # "Mac OS X", etc.
            system = 'darwin'
        else: # "Linux", "SunOS", "FreeBSD", etc.
            # Setting this to "linux2" is not ideal, but only Windows or Mac
            # are actually checked for and the rest of the module expects
            # *sys.platform* style strings.
            system = 'linux2'
    return system