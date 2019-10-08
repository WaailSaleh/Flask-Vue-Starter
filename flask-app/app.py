from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)


@app.route("/api/message")
def get_message():
    return jsonify({
        "message": "Flask + VueJS"
    })
auth= {"Authorization" :"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2l3wRoxfQ.IUJTu87WjXRqjCMAj0zhhYvX2sFGAiU1g3YIxc3tt2I"}
@app.route("/api/p1")
def get_p1():
    response = requests.get("http://localhost:5000/DataSecure", headers=auth)
    return json.dumps(response.json()), 200