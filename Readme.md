The microservice checks a inventory list and creates notifications for all the items that are low on stock.

How to run:
1. Install dependancies:
pip install flask requests
pip install requests

3. Start microservice:
python notification.py
python test.py

The Low Stock Notification microservice checks inventory levels, sends low stock alerts, and keeps history of the notifications sent. It communicates using REST API on localhost:400. All request and responses use JSON. The main program sends POST and GET request, the microservice returns JSON data. 

To check inventory, it sends a POST request to /notification/check with a list. The service then looks through each item and returns a list of any items that are below their set lowlimit. It then POST to /notification/send with item names, quantity and lowlimit. It also saves the alert. To see the history, send GET request to /notification/histroy, and it will resond with a alert log. 

POST /notification/check: sends list, receives low stock items
POST /notification/send: sends alert, reveives alert
GET /notification/histroy: reveives all alerts
