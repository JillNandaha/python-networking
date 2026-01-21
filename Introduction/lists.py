network_devices = [
    {"name": "Router1", "status": "active"},
    {"name": "Switch1", "status": "inactive"},
    {"name": "Firewall1", "status": "active"},
]

active_devices = [device for device in network_devices if device["status"] == "active"]
# Output: [{'name': 'Router1', 'status': 'active'}, {'name': 'Firewall1', 'status': 'active'

#extracting IP addresses
configurations = [
    "Router1: 192.168.1.1",
    "Switch1: 10.0.0.1",
    "Firewall1: 172.16.0.1",
]

ip_addresses = [config.split(": ")[1] for config in configurations]
# Output: ['192.168.1.1', '10.0.0.1', '172.16.0.1']


ip_address = [f'192.168.{x}.{y}' for x in range (3) for y in range(4)]
print(ip_address)