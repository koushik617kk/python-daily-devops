# Write a script that scans a log file and tdentifies the String ERROR,FATALL and extract the timestamp and those line

import re
import os

LOG_FILE = 'app.log'

LOG_PATTERN = re.compile(r"(\d{4}-\d{2}-d{2} \d{2}:\d{2}:\d{2}) \[(ERROR| FATAL)\] (.*)")

def analyze_logs(log_path):
    
    if not os.path.exists(log_path):
        print(f"Error: log file not found as {log_path}")
        return

    print(f"log file : {log_path}")
   
    critical_issues=0

    try:
        with open(log_path, 'r') as file:
            for line_number, line in enumerate(file,1):
                print(f'{line}')
                match = LOG_PATTERN.search(line)
                print(f'Matching line: {match}')
                if match:
                    timestamp = match.group(1)
                    log_level = match.group(2)
                    message = match.group(3)

                    print(f"time: {time_stamp} |  Level: {log_level:<3}) | Message: {message.strip()}")

    except Exception as e:
        print(f"An Error occuured during log processing: {e}")

analyze_logs(LOG_FILE)

