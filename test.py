import requests
import json

def display(title, data):
    print("\n--- " + title + " ---")
    print(json.dumps(data, indent=4))

def test_check():
    r = requests.post("http://localhost:4000/notification/check", json={
        "inventory": [
            {"name": "Tomatoes", "quantity": 3, "lowLimit": 5},
            {"name": "Limes", "quantity": 2, "lowLimit": 5},
            {"name": "Onions", "quantity": 10, "lowLimit": 4}
        ]
    })
    display("Results", r.json())
    test_send()

def test_send():
    r = requests.post("http://localhost:4000/notification/send", json={
        "itemName": "Garlic",
        "quantity": 1,
        "lowLimit": 3
    })
    display("Notification Sent", r.json())
    test_history()

def test_history():
    r = requests.get("http://localhost:4000/notification/history")
    display("History", r.json())

test_check()