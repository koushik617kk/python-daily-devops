import subprocess
import os

if os.name == 'nt':
    command_to_run = ['cmd','/c','dir']
    print("Running 'dir' command (windows)")
else:
    command_to_run = ['ls','-l']
    print("Running 'ls -l' command (Linux)")

try:

    result = subprocess.run(command_to_run, capture_output=True, text=True, check=True)
    print("-" * 30)
    print("Command Output (Standard Output)")
    print(result.stdout)
    print("-"*30)

    if result.stderr:
        print("Command Error")
        print(result.stderr)
        print("-" * 30)

except subprocess.CalledProcessError as e:
    print(f"\nError running command: {e.cmd}")
    print(f"Return Code: {e.returncode}")
    print(f"Stderr: {e.stderr}")

except FileNotFoundError:
    print(f"Error: The command '{command_to_run[0]}' was not found on you system")
    
