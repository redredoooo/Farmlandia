import requests
import uuid
import threading
import time

def draw(unique_id):
    url = f"https://hybrid.pre.infinix.club/retest/extend/seasonalEvent/spinPrize?activity=1003&unique_id={unique_id}&timezone=Asia/Shanghai"

    headers = {
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9",
        "accept-language-api": "en",
        "content-length": "0",
        "origin": "https://hybrid.pre.infinix.club",
        "priority": "u=1, i",
        "referer": "https://hybrid.pre.infinix.club/voting-mslmm?lang=en",
        "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36"
    }

    response = requests.post(url, headers=headers)
    
    if response.status_code == 200:
        responseData = response.json()
        if responseData['data']['is_win']:
            print(f"Winner! {unique_id}: {responseData['data']['prize_name']}:{responseData['data']['redeem_code']}")
            with open('winners.txt', 'a') as file:
                file.write(f"{unique_id}: {responseData['data']['prize_name']}:{responseData['data']['redeem_code']}\n")
        else:
            print(f"{unique_id}: {responseData['data']['prize_name']}:{responseData['data']['prize_type']}")
    else:
        print(f"Error: {response.status_code}, Response: {response.text}")

def run_continuously():
    while True:
        unique_id = str(uuid.uuid4())
        threading.Thread(target=draw, args=(unique_id,)).start()
        time.sleep(2)  # Prevents spamming the server

if __name__ == "__main__":
    run_continuously()
