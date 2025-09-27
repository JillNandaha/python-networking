#SEND CONFIG COMMANDS TO MULTIPLE DEVICES
from netmiko import ConnectHandler

#define device details for cisco devices
devices = [
    {
        'device_type': 'cisco_ios',
        'ip': '172.16.10.11',
        'username': 'admin',
        'password': 'cisco',
        'secret': 'cisco123',
    },
    {
        'device_type': 'cisco_ios',
        'ip': '172.16.10.12',
        'username': 'admin',
        'password': 'cisco',
        'secret': 'cisco123',
    },
]

for device in devices:
    print(f'Connecting to {device['ip']}')
    net_connect = ConnectHandler(**device)
    net_connect.enable()

    #configure device
    config_commands = ['username admin pri 15 password cisco']
    net_connect.send_config_set(config_commands)
    net_connect.save_config()

    #display updated config
    output = net_connect.send_config('show running-config | section username')
    print(output)

    print(f'Closing Connection on {device["ip"]}')
    net_connect.disconnect()


#CONFIG CHANGES FROM A FILE
from netmiko import ConnectHandler

# Define device details for a Cisco device
device = {
    'device_type': 'cisco_ios',
    'ip': '172.16.10.11',
    'username': 'admin',
    'password': 'cisco',
    'secret': 'cisco123',
}

file = "config_file.cfg"

# Use a context manager to establish a connection to the device
with ConnectHandler(**device) as net_connect:
    output = net_connect.send_config_from_file(file)
    output += net_connect.save_config()

print(output)


#BACKUP DEVICE CONFIG
from netmiko import ConnectHandler
from datetime import datetime

# Define device details for Cisco devices
devices = [
    {
        "host": "172.16.10.11",
        "username": "admin",
        "password": "cisco",
        "device_type": "cisco_ios",
    },
    {
        "host": "172.16.10.12",
        "username": "admin",
        "password": "cisco",
        "device_type": "cisco_ios",
    }
]

# Get current timestamp
time_stamp = datetime.now().strftime("%d-%b-%Y")

# Retrieve the running configuration of each device and save it to a file with a timestamp
for device in devices:
    net_connect = ConnectHandler(**device)
    print(f"Initiating running config backup for {device['host']}...")
    sh_run = net_connect.send_command('show run')

    with open(f"{device['host']}_{time_stamp}.cfg", 'w') as f:
        f.write(sh_run)
        print("Backup saved")

print("Finished backup process.")