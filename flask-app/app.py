from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

@app.route("/api/message")
def get_message():
    return jsonify({
        "message": "Flask + VueJS"
    })
auth = {}
token = None
@app.route("/api/token")
def get_token():
    response = requests.post("http://localhost:8181/token", json={"user":"dev", "pass":"secret"})
    token = response.text
    auth['Authorization'] =  token
    return auth['Authorization']

@app.route("/api/p1")
def get_p1():
    if token is None:
        get_token()
    response = requests.get("http://localhost:8181/DataSecure", headers=auth)
    return response.text, 200
