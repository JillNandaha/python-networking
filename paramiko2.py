import paramiko
import time

#create ssh client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#connect to remote device
client.connect(
    hostname = '192.168.1.3',
    username = 'admin',
    password = 'CISCO',
    look_for_keys = False,
    allow_agent = False
)

#start an interactive shell
ssh_client = client.invoke_shell()
print('###Creating loopback interfaces###')

#send command
ssh_client.send('conf t\n')

#use a for loop and range to create loopback interfaces
for interface_number in range(0,1):
    ssh_client.send(f'int lo{interface_number}\n')
    ssh_client.send(f'ip address 1.1.1.{interface_number} 255.255.255.255\n')

#wait for configurations to take effect
time.sleep(1)

ssh_client.send('end\n')
ssh_client.send('show ip int bri\n')

#wait for the output and retrieve it

time.sleep(3)
output = ssh_client.recv(65000)
print(output.decode('ascii'))

client.close()

