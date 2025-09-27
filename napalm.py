import napalm

#Create a NAPALM driver for cisco ios
driver = napalm.get_network_driver('cisco')

#Connect to device
device = driver(hostname = '192.168.3.10', username = 'host', password = 'cisco')
device.open()

#perform operations
device.close()


#RETEREIVING DEVICE INFORMATION AND CONFIG DATA
import napalm
import json

#Create a napalm driver
driver = napalm.get_network_driver('ios')

#connect to device
device = driver(hostname = '192.127.8.30', username = 'admin', password = 'Cisco')
device.open()

#retrieve running configs
device_facts = device.get_facts()

#print running configs
print(json.dumps(device_facts, indent=4))

#close connection
device.close()