#!/usr/bin/env python3
import webtech

# make sure to have the latest db version
webtech.database.update_database(force=True)

# you can use options, same as from the command line
wt = webtech.WebTech(options={'json': True})

# scan a single website
report = wt.start_from_url('https://google.com', timeout=1)
print(report)

# scan multiple websites from a list 
for site in ['https://shielder.it', 'http://connectionerror']:
    try:
        report = wt.start_from_url(site)

        techs = report['tech']
        print("Site: {}".format(site))
        for tech in techs:
        	print(" - {}".format(tech))
    except webtech.utils.ConnectionException:
        print("Site unavailable: {}".format(site))

print("Done")