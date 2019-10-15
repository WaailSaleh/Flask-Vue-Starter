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
    response = requests.post("http://localhost:6969/token", json={'user':'dev', 'pass':'secret'})
    token = response.text
    auth['Authorization'] = 'Bearer ' + token

@app.route("/api/p1")
def get_p1():
    if token is None:
        get_token()
    response = requests.get("http://localhost:6969/DataSecure", headers=auth)
    return response.text, 200