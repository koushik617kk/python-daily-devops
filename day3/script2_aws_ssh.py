#connect a server 
import paramiko
import time

HOSTNAME = ""
USERNAME = ""
PASSWORD = ""
REMOTE_COMMAND = "uptime && df -h"

def run_remote_command(hostname, username, password, command):
    ssh_client = paramiko.SSHClient()

    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh_client.connect(hostname=hostname, username=username, password=password)
        stdin, stdout, stderr = ssh_client.exec_command(command)

        output = stdout.read().decode().strip()
        error = stderr.read().decode().strip()

        if error:
            print(error)


    finally:
        if ssh_client: 
            ssh_client.close()
            print(connection closed)

