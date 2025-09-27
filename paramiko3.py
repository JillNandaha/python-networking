#CREATING LOOPBACK INTERFACES
import paramiko
import time

#create SSH client 
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#connect to a remote device
client.connect(
    host = '192.168.3.80',
    username = 'admin',
    password = 'Cisco',
    look_for_keys = False,
    allow_agent = False
)

#start an interactive shell
ssh_client = client.invoke_shell()
print("###### Creating loopback interfaces ######")

#send a command
ssh_client.send('conf t\n')

#use a for loop and range() to create a loopback intercace
for interface_number in range(0,1):
    ssh_client.send(f'int lo {interface_number}\n')
    ssh_client.send(f'ip address 1.1.1.{interface_number} 255.255.255.255\n')

#wait for configuration to take effect
time.sleep(1)

ssh_client.send('end\n')
ssh_client.send('show ip interface brief\n')

#wait for output and retrieve
time.sleep(3)
output = ssh_client.recv(65000)
print(output.decode('ascii'))

#close SSH connection
client.close()


#CONNECTING TO MULTIPLE DEVICES WITH A LIST
import paramiko
import time 

username = 'admin'
password = 'CCNA'

#IP list for network devices
devices = ['192.168.10.2', '192.168.10.3']

for device in devices:
    print("\n #### Connecting to the device " + device + " ####\n")

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(
        hostname = device,
        port = 22,
        username = username,
        password = password,
        look_for_keys = False,
        allow_agent = False
    )

    ssh_client = client.invoke_shell
    ssh_client.send('conf t\n')

    

    #create a loopback interface
    for num in range(2,5):
        ssh_client.send("int loop " + str(num) + "\n")
        ssh_client.send("ip address 1.1.1." + str(num) + " 255.255.255.255\n")

    time.sleep(1)
    ssh_client.send('end\n')
    ssh_client.send('show ip interface brief')

    time.sleep(3)
    output = ssh_client.recv(65000)
    print(output.decode('ascii'))

    client.close()