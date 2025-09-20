import getpass
import telnet

#user input for IP, username and password
IP = input('Enter IP address:')
user = input('Enter username:')
password = getpass.getpass()


#Telnet connection and authentication
tn = telnet.Telnet(IP)
tn.read_until(b'Username: ')
tn.write(user.encode('ascii') + b'\n')
if password:
    tn.read_until(b'Password:')
    tn.write(password.encode('ascii') +b'\n')

#VLAN configuration
tn.write(b'enable\n')
tn.write(b'cisco\n')
tn.write(b'conf t\n')

for n in range(2,5):
    tn.write(b"vlan " + str(n).encode("ascii") + b"\n")
    tn.write(b"name VLAN_" + str(n).encode("ascii") + b"\n")

tn.write(b'end\n')
tn.write(b'show vlan br \n\n')
tn.write(b'exit\n')
print(tn.read_all.decode('ascii'))

