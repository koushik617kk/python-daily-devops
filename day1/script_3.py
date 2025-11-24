import subprocess
import os

if os.name == "nt":
    command = ['cmd', '-c', 'dir']
    print(f"command is : {command}")
else:
    command = ['echo', 'Devops is great']
    print(f"command is : {command}")

def run_command_with_check(cmd_list):
    try:
        result = subprocess.run(cmd_list, capture_output=True, check=True, text=True)
        
        if result.returncode == 0 :
            print(f"Output:\n{result.stdout.strip()}")
        else:
            print(f"Output:\n{result.stderr.strip()}")

    except FileNotFoundError:
        print("Command not founf")

run_command_with_check(command)
