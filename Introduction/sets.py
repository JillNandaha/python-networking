configurations = ["config1", "config2", "config3", "config1", "config4", "config2"]
unique_configs = {config for config in configurations}
print(unique_configs)
# Output: {"config1", "config2", "config3", "config4"}

#using conditionals
network_devices = {"router1", "switch1", "router2", "firewall1", "switch2"}
routers_only = {device for device in network_devices if "router" in device}
print(routers_only)
# Output: {"router1", "router2"}


#combining elements from multiple iterables
vlans = ["vlan10", "vlan20", "vlan30"]
subnets = ["192.168.10.0", "192.168.20.0", "192.168.30.0"]
vlan_subnets = {vlan + " " + subnet for vlan in vlans for subnet in subnets}
print(vlan_subnets)