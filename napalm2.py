#CONFIGURING INTERFACE DESCRIPTION
import napalm

#Create napalm driver
driver = napalm.get_network_driver('ios')

#connect to device
device = driver(hostname ='192.168.3.2', username='admin', password='Cisco')
device.open()

#Load config changes
config = 'interface GigabitEthernet0/3\ndescription Test Interface'
device.load_merge_candidate(config=config)

#apply config changes
device.commit_config()

#close connection
device.close()

#MANAGING NETWORK CONFIGS
import napalm

driver = napalm.get_network_driver('ios')

device = driver(hostname ='192.168.3.2', username='admin', password='Cisco')
device.open()

#Load te candidate config from file
device.load_merge_candidate(filename='acl.conf')

#compare candidate config with running config
difference = device.compare_config()

#check for differences and apply changes if necessary
if len(difference) > 0:
    print('Configuration changes detected')
    print(difference)
    device.commit_config()

else:
    print('No chnages required')
    device.discard_config()

device.close()
