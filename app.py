import requests
import hashlib
import time

url = 'XXX'
refresh_rate = 60
previous_hash = None

while True:
    try:
        response = requests.get(url)
        response.raise_for_status()  

        current_content_hash = hashlib.md5(response.content).hexdigest()
        
        if current_content_hash != previous_hash:
            print('WEBSITE CHANGED')
            previous_hash = current_content_hash  

        time.sleep(refresh_rate)

    except Exception as e:
        print(f'An error occurred: {str(e)}')