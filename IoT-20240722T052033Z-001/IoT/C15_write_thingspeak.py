import requests
import time
import random
 
channel_id = 394744 # PUT CHANNEL ID HERE
write_key  = 'AAOG612RJT5LW21R' # PUT YOUR WRITE KEY HERE
read_key   = 'TSPKJB230K65QPJQ' # PUT YOUR READ KEY HERE


if __name__ == "__main__":
	
	while True:
		val = random.randint(0,99)
		#print(val)
		URL = 'http://api.thingspeak.com/update?api_key=%s&field1=%s' %(write_key,val)	
		#print(URL)
		resp = requests.get(url=URL)
		#print(resp.json())
		# free account has an api limit of 15sec
		time.sleep(30)