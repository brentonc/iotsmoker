import time
import sys
from azure.servicebus import ServiceBusService


key_name = "MySender"
key_value = "MyKeyGoesHere"

sbs = ServiceBusService("robotdeskeventhub-ns",shared_access_key_name=key_name, shared_access_key_value=key_value)

while(True):
	print('sending...')
	sbs.send_event('nameofeventhub', '{ "DeviceId": "smokerpi", "Temperature": "37.0" }')
	print('sent!')
	time.sleep(10)
	
	

