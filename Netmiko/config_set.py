from netmiko import ConnectHandler

CoreSW = {
    "ip": "192.168.100.20",
    "username": "admin",
    "password": "cisco",
    "device_type": "cisco_ios",
}

SW1 = {
    "ip": "192.168.100.21",
    "username": "admin",
    "password": "cisco",
    "device_type": "cisco_ios",
}


devices = [CoreSW,SW1]

for device in devices:
    print("Connecting to device " + device["ip"])
    net_connect = ConnectHandler(**device)


config_commands = ["int lo0", "ip add 1.1.1.1 255.255.255.0", "no shut"]
output = net_connect.send_config_set(config_commands)
print(output)

