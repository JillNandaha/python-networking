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

switches = ['CoreSw', 'SW1', 'SW2']

for device in switches:
    net_connect = ConnectHandler(**device)
    net_connect.enable()

    for n in range(10,15):
        print(f'Connecting VLAN {n}')
        config_commands = ['vlan' + str(n), 'name_Devops_VLAN' + str(n)]
        output = net_connect.send_config_set(config_commands)
        print(output)