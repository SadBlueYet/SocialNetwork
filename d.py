import requests
from pprint import pprint

a = requests.get("http://127.0.0.1:8000/loading_messages",
                 json={"username": "aedfw3w3f",
                       "password": "47d749de595e4fb2dc9ddc098d2b1ce740eecbdfb68809d3e846ef161d894895"}).json()
pprint(a)
