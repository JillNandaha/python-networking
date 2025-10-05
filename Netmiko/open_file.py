from netmiko import ConnectHandler

CoreSW = {
    "device_type": "cisco_ios",
    "ip": "192.168.100.20",
    "username": "admin",
    "password": "cisco",
    "secret": "cisco",
}
SW1 = {
    "device_type": "cisco_ios",
    "ip": "192.168.100.21",
    "username": "admin",
    "password": "cisco",
    "secret": "cisco",
}
SW2 = {
    "device_type": "cisco_ios",
    "ip": "192.168.100.22",
    "username": "admin",
    "password": "cisco",
    "secret": "cisco",
}
devices = [CoreSW, SW1, SW2]

#open the file containing commands we need to execute and read the lines
with open('config_file.cfg') as file:
    lines = file.read().splitlines()
print(lines)

for device in devices:
    net_connect = ConnectHandler(**device)
    net_connect.enable()

    #call each command line by line
    output = net_connect.send_config_set(lines)
    print(output)