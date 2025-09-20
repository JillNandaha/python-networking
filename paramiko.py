import paramiko

hostname = '192.168.0.1'
username = 'admin'
password = 'himawari'

#create an SSH client
client = paramiko.SSHClient()

#autoaccept unknown host keys
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    print(f"Connecting to {hostname}...")
    client.connect(hostname, username=username, password=password)

    #simple command to check system info
    stdin, stdout, stderr = client.exec_command("uname -a")

    print("---- Command Output ----")
    for line in stdout.readlines():
        print(line.strip())

    if stderr:
        print("---- Errors ----")
        for line in stderr.readlines():
            print(line.strip())
except Exception as e:
    print(f"Connection failed: {e}")
finally:
    client.close()
    print('Connection closed')


#using paramiko to establish a secure ssh connection to networking devices
#first create a client object, then specify parameters such as hostname,port, authentication credentials then initiate connection

import paramiko
import time

#create  SSH client
client = paramiko.SSHClient()

#set policy to automatically add hosts to known hosts file
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#connect to remote host
client.connect(
    hostname = '192.168.1.2',
    username = 'admin',
    password = 'Cisco',
    look_for_keys = False,
    allow_agents = False
)

#perform oprations on remote hosts
#execute commands on remote hosts and handle command output

#open interactive ssh session
ssh_client =client.invoke_shell()

#send command
ssh_client.send('sh ip int bri\n')

#wait for command to be finished
time.sleep(3)

#receive and process command output
output = ssh_client.recv(65000)
print(output.decode('ascii'))

#close SSH session
ssh_client.close()

#close connection
client.close()



#HANDLING EXCEPTIONS
import paramiko
import time


# Create SSH client
try:

    client = paramiko.SSHClient()

    # Set policy to automatically add hosts to known hosts file
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the remote host
    client.connect(
        hostname="172.16.10.12",
        username="admin",
        password="cisco",
        look_for_keys=False,
        allow_agent=False,
    )

    # Open an interactive SSH session
    ssh_client = client.invoke_shell()

    # Send command
    ssh_client.send("sh ip int bri\n")

    # Wait for the command to be finished
    time.sleep(3)

    # Receive and process command output
    output = ssh_client.recv(65000)
    print(output.decode("ascii"))

    # Close the SSH session
    ssh_client.close()

    # Close the connection
    client.close()

except paramiko.AuthenticationException:
    print("Authentication failed. Please verify your credentials.")



    