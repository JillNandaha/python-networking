#HANDLING DIFFERENT CONFIGS FROM DIFFERENT FILES TO DIFFERENT DEVICES

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
switches = [CoreSW, SW1, SW2]

#open the first file with configurations
with open('file_confg.cfg') as f:
    lines = f.read().splitlines()
    print(lines)

    #send configs to the devices
    for device in switches:
        net_connect = ConnectHandler(**device)
        net_connect.enable()

        output = net_connect.send_config_set(lines)
        print(output)

#open another file with different configurations
with open('swch2_confg.cfg') as f:
    lines = f.read().splitlines()
    print(lines)

    #select devices to be configured.
    for SW2 in switches:
        net_connect = ConnectHandler(**SW2)
        net_connect.enable()

        output = net_connect.send_config_set(lines)
        print(output)