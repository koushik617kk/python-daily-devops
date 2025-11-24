import os
import yaml

config_file = "config.yaml"

print(f"Reading config file: {config_file}")

try: 

    with open(config_file, 'r') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

    print("-" * 30)
    print("Print configuration")
    print(config)
    print("-" * 30)

    app_name = config['app']['name']
    app_port = config['app']['port']
    prod_enabled = config['environments'][1]['enabled']

    print(f"printing ap_name: {app_name}")
    print(f"printing app_port: {app_port}")
    print(f"printing prod_enabled: {prod_enabled}\n")

except FileNotFoundError:
    print (f"File Not found")
except KeyError as e:
    print (f"Could not find the key {e}")

except yaml.YAMLError as e:
    print (f"Error: failed to parse YAML content")
