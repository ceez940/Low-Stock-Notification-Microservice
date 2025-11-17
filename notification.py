from flask import Flask, request, jsonify
import time

app = Flask("notification")
alertHistory = []

@app.post("/notification/check")
def check_inventory():
    data = request.get_json()
    inv = data["inventory"]
    lowItems = []

    for item in inv:
        if item["quantity"] < item["lowLimit"]:
            alert = {
                "itemName": item["name"],
                "quantity": item["quantity"],
                "lowLimit": item["lowLimit"],
                "notiSent": True,
                "timestamp": time.ctime()
            }
            alertHistory.append(alert)
            lowItems.append(alert)

    return jsonify({"lowItems": lowItems, "timestamp": time.ctime()})

@app.post("/notification/send")
def send_noti():
    data = request.get_json()
    alert = {
        "itemName": data["itemName"],
        "quantity": data["quantity"],
        "lowLimit": data["lowLimit"],
        "notiSent": True,
        "timestamp": time.ctime()
    }
    alertHistory.append(alert)
    return jsonify({"alert": alert})

@app.get("/notification/history")
def history():
    return jsonify({"history": alertHistory})

app.run(port=4000)