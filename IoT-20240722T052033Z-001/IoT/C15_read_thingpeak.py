#!/usr/bin/env python3

import requests
import json
import time

Key = 'TSPKJB230K65QPJQ'
channel = 394744

while True:
	try:
		#URL = 'http://api.thingspeak.com/channels/%s/feeds/last.json?' %(channel)
		URL = 'http://api.thingspeak.com/channels/%s/field/1' %(channel)
		#print(URL)
		resp = requests.get(url=URL)
		#print(resp)
		resp = resp.json()['feeds'][-1]['field1']
		print(resp)
		time.sleep(0.3)
	
	except KeyboardInterrupt:
		exit()




