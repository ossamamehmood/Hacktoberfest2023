# WebTech
Identify technologies used on websites. [More info on the release's blogpost](https://www.shielder.it/blog/webtech-identify-technologies-used-on-websites/).

## CLI Installation

WebTech is available on pip:

```
pip install webtech
```

It can be also installed via setup.py:

```
python setup.py install --user
```

## Burp Integration

Download Jython 2.7.0 standalone and install it into Burp.

In "Extender" > "Options" > "Python Environment":
- Select the Jython jar location

Finally, in "Extender" > "Extension":
- Click "Add"
- Select "py" or "Python" as extension format
- Select the `Burp-WebTech.py` file in this folder


## Usage

Scan a website:

```
$ webtech -u https://example.com/

Target URL: https://example.com
...

$ webtech -u file://response.txt

Target URL:
...
```

Full usage:

```
$ webtech -h

Usage: webtech [options]

Options:
  -h, --help            show this help message and exit
  -u URLS, --urls=URLS  url(s) to scan
  --ul=URLS_FILE, --urls-file=URLS_FILE
                        url(s) list file to scan
  --ua=USER_AGENT, --user-agent=USER_AGENT
                        use this user agent
  --rua, --random-user-agent
                        use a random user agent
  --db=DB_FILE, --database-file=DB_FILE
                        custom database file
  --oj, --json          output json-encoded report
  --og, --grep          output grepable report
  --udb, --update-db    force update of remote db files

```

## Use WebTech as a library

```
import webtech

# you can use options, same as from the command line
wt = webtech.WebTech(options={'json': True})

# scan a single website
try:
  report = wt.start_from_url('https://shielder.it')
  print(report)
except webtech.utils.ConnectionException:
  print("Connection error")
```

For more examples see `webtech_example.py`.


## Resources for database matching

HTTP Headers information - http://netinfo.link/http/headers.html  
Cookie names - https://webcookies.org/top-cookie-names  
