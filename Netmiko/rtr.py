from netmiko import ConnectHandler

R1 = {
    "device_type": "cisco_ios",
    "ip": "192.168.121.102",
    "username": "admin",
    "password": "admin",
    "secret": "cisco",
}

net_connect = ConnectHandler(**R1)
net_connect.enable()

output = net_connect.send_command("sh ip int br")
print(output)


