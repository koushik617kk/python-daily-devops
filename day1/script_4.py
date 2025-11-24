import yaml

def read_print_values(config_file_name):
    try:
        with open(config_file_name, 'r') as file:
            opened_file = yaml.load(file, Loader=yaml.FullLoader)

        print("-" * 30)
        print(opened_file)
     
        environments = opened_file.get('environments',[])

        for env in environments:
            if env.get('enabled'):
                print(f"Environemnt '{env.get('name')}'")
            else:
                print(f"diabeled")

    except Exception as e:
        print(f"An error occured: {e}")

read_print_values("config.yaml")       



