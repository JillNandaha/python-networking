from netmiko import ConnectHandler
connection = ConnectHandler(
    host = '192.178.3.50',
    username = 'admin',
    password = 'Cisco',
    device_type = 'cisco_ios'
)

output = connection.send_command('show ip int brief')
print(output)
connection.disconnect()


#DEVICE CONFIGURATION
from netmiko import ConnectHandler
import getpass

#getpass allows us to prompt user for the  password
passwd = getpass.getpass('Please enter the password: ')
SW_01 = {
    "device_type": "cisco_ios",
    "host": "172.16.10.11",
    "username": "admin",
    "password": "cisco",
    "secret": "cisco123"  # Enable password
}

#establis connection and elevate permission to privileged exec mode
connection = ConnectHandler(**SW_01)
connection.enable()

#enter global config mode
connection.config_mode()

#send command
connection.send_command('access-list 1 permit any')

#exit
connection.exit_config_mode()

#back to privileged mode where we can execute show commands and other tasks
show_output = connection.send_command('show interface desc')
print(show_output)

connection.disconnect()

#SENDING MULTIPLE COMMANDS
from netmiko import ConnectHandler
import getpass

passwd = getpass.getpass('Please enter the password: ')
SW_01 = {
    "device_type": "cisco_ios",
    "host": "172.16.10.11",
    "username": "admin",
    "password": "cisco",
    "secret": "cisco123"  # Enable password
}

connection = ConnectHandler(**SW_01)
connection.enable()

#define a list of config commands to be sent to the switch
config_commands = ['interface gi0/0', 'description WAN', 'exit', 'access-list 1 permit any']

#send_config_set is used to send all the commands
connection.send_config_set(config_commands)

#to prove configs have been applied
print(connection.send_command('show interfaces description'))
print(connection.send_command('show access-lists'))

connection.disconnect()

#CONNECTING TO MULTIPLE DEVICES
from netmiko import ConnectHandler
import getpass
import json

passwd = getpass.getpass('Enter password: ')

ip_list = ['192.176.8.30', '192.172.8.24']

#create a list of dictionaries for each device
device_list = []

#populate the device list with device details
for ip in ip_list:
    device = device = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": "admin",
        "password": passwd,  # Log in password from getpass
        "secret": passwd  # Enable password from getpass
    }
    device_list.append(device)

#print json formatted device details using json formatting
json_formatted = json.dumps(device_list, indent=4)
print(json_formatted)

#iterate over eac device and connect to it
for each_device in device_list:
    connection = ConnectHandler(**each_device)
    connection.enable()
    print(f'Connecting to {each_device['host']}')
    output = connection.send_command('show run | incl hostname')
    print(output)
    print(f'Closing Connection on {each_device["host"]}')
    connection.disconnect()



