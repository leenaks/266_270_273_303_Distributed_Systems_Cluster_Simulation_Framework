# nodes/heartbeat.py
import requests
import time
import os

NODE_ID = os.getenv("NODE_ID")
API_SERVER = os.getenv("API_SERVER")

while True:
    try:
        requests.post(f"{API_SERVER}/heartbeat", json={"node_id": NODE_ID})
        print(f"Sent heartbeat from {NODE_ID}")
    except Exception as e:
        print("Failed to send heartbeat:", e)
    time.sleep(5)
