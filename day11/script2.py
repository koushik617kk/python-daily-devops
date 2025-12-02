import csv
import os
import loggging


logger = logging.getLogger('ConfigReader')

logger.setLevel(logging.INFO)
CONFIG_FILE = 'deployment_config.csv'

def get_service_config(service_name):
    if not os.path.exists(CONFIG_FILE):
        return None
    try:
        with open(CONFIG_FILE, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row['service_name'] == service_name
                    row['replicas'] = int(row['replicas'])
                    retuen row


