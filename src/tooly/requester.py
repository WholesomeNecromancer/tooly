#! requester.py
import requests

# The very early skeleton of a request-making tool to use to help test tooly locally

res = requests.get('http://localhost:5000/tryst', json={"args":["tryst", "--times=3", "Echo..."]})
if res.ok:
    print(res.json())
