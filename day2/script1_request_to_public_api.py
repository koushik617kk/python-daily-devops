# health check on a web service using a publiv api, stable api and verify the http status code is 200

import requests

API_URL="https://www.githubstatus.com/api/v2/status.json"

def check_health_status(url):

    print(f"checking API: {url}")
    try:
        response = requests.get(url, timeout=5)

        if response.status_code==200:
            data = response.json()
            status = data.get('status',{}).get('description', 'Status not found')
            print(f"API is Healhtyyyy Status code: {response.status_code}")
            print(f"Service Status: {status}")
        else: 
            print("API is Down move your ass and make  it work")
    except request.exceptions.Timeout:
        print(f"Error: Request Timed out after 5 secs")
    except request.exceptions.ConnectionError:
        print(f"Error:  Could not connect to {url}")
    except Exception as e:
        print(f"Unexpected error happened {e}")

check_health_status(API_URL)
