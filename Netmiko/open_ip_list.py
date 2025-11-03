# Demonstrates how to ssh to a list of devices from text file,
# and how to get config from file

from netmiko import ConnectHandler

with open ("device_list") as IP_LIST:
    for IP in IP_LIST:
        device = {
            "ip":IP,
            "username":"admin",
            "password": "cisco",
            "device_type": "cisco ios"
        }
        net_connect = ConnectHandler(**device)

        with open ("config_files") as CONFIG_LINES:
            CONFIG = CONFIG_LINES.read()
        output = net_connect.send_config_set(CONFIG)
        print(output)