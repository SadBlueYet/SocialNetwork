import requests
import httpx
from pprint import pprint

"""a = requests.post("http://127.0.0.1:8000/set_message", json={"text": "еблан", "getter_id": 3, "sender_id": 2}).json()
pprint(a)
# ["текст", sender_id, getter_id]
for i in range(10):
    if i % 2:
        a = requests.post("http://127.0.0.1:8000/set_message",
                          json={"text": f"{i}", "getter_id": 3, "sender_id": 2}).json()
    else:
        a = requests.post("http://127.0.0.1:8000/set_message",
                          json={"text": f"{i}", "getter_id": 2, "sender_id": 3}).json()
    pprint(a)"""

a = requests.get("http://127.0.0.1:8000/get_id_by_username", json={"username": "SadBlue"}).json()
pprint(a)
