import time
from getpass import getpass
import Paramiko.paramiko as paramiko

host = '192.168.7.20'
username = 'admin'
password = getpass('Enter SSH password: ')

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(
    host,
    port = 22,
    username = username,
    password = password,
    look_for_keys = False,
    allow_agent = False

)
#invoke the interactive shell session on remote device
device = ssh.invoke_shell()

#send commands
device.send(b'term length0\n')

device.send(b'show run\n')

#wait for command to complete
time.sleep(10)

output = device.recv(65000)

print(output.decode('ascii'))

ssh.close
