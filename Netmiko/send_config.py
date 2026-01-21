#Create VLAN and assign IP using SSH
from getpass import getpass

from netmiko import ConnectHandler

password = getpass()

secret = getpass("Enter secret: ")

CoreSW = {
    "device_type": "cisco_ios",
    "ip": "192.168.100.20",
    "username": "admin",
    "password": password,
    "secret": secret,
}

"""calling the ConnectHandler Library [**iosv_l2] means telling
python to consider the contents of the dictionary as key value pairs
instead of single elements."""

net_connect = ConnectHandler(**CoreSW)
net_connect.enable()

#Send command to the switch
output = net_connect.send_command("show ip int br")
print(output)

#Create a list of all commands to be executed
commands_list = ["int vlan 5", "ip add 192.168.1.222 255.255.255.252"]
output = net_connect.send_config_set(commands_list)
print(output)