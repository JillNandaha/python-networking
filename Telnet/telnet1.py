import time
from getpass import getpass
from Paramiko.paramiko import paramiko


host = '192.168.10.2'
username = 'admin'
password = getpass('Enter password: ')

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(
    host,
    port = 22,
    password = password,
    username = username,
    look_for_keys = False,
    allow_agent = False

)

device = ssh.invoke_shell()

device.send(b'term length\n')

device.send(b'show run\n')

time.sleep(10)

output = device.recv(65000)

print(output.decode('ascii'))

ssh.close()