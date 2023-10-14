#!/usr/bin/env python
try:
    from html.parser import HTMLParser
except ImportError:
    from HTMLParser import HTMLParser

# Don't blame on me for this mess, we can't use external libs and all we have is HTMLParser
class WTParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.meta = {}
        self.scripts = []

    def handle_starttag(self, tag, attrs):
        if tag == 'meta':
            m = {}
            for name, value in attrs:
                m[name] = value

            name = m.get('name') or m.get('property')
            if name:
                self.meta[name] = m.get('content', '')
        elif tag == 'script':
            for name, value in attrs:
                if name == 'src':
                    self.scripts.append(value)
        return

