from netmiko import ConnectHandler

S1 = {
    "device_type": "cisco_ios",
    "ip": "192.168.121.102",
    "username": "admin",
    "password": "admin",
    "secret": "cisco",
}

net_connect = ConnectHandler(**S1)
net_connect.enable()

output = net_connect.send_command("sh ip int br")
print(output)