# Convert CrateJoy CSV export to simple address list, including only active subs

import csv
import glob
import os.path
import time

# Assume the CSV file was just downloaded to desktop 
m = glob.glob('/Users/bemmu/Desktop/customers_export*')
if len(m) == 0:
	print "Remember to export from CrateJoy first"
	exit()

in_fn = m[0]

# Make sure this file is likely to be the latest export
elapsed = time.time() - os.path.getmtime(in_fn)
if elapsed > 86400:
	print "I don't know, man, that %s file looks kinda old. Sure you exported it just now?" % in_fn
	exit()

out = []

with open(in_fn, 'rb') as f:
	c = csv.DictReader(f)
	for row in c:
		if row['subscription_status'] != 'active':
			continue

		for k, v in row.items():
			row[k] = v.upper().strip().replace('  ', ' ')

		label = "%(id)s\n%(ship_to)s\n%(ship_street)s %(ship_unit)s\n%(ship_city)s %(ship_state)s %(ship_zip_code)s\n%(ship_country)s" % row
		out.append({
			"id" : row["id"],
			"label" : label
		})

import json
print json.dumps(out)