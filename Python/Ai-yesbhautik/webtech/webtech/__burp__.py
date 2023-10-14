BURP=False
try:
    from burp import IBurpExtender
    BURP=True
except ImportError:
    pass
