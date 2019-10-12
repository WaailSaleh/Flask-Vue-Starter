from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

@app.route("/api/message")
def get_message():
    return jsonify({
        "message": "Flask + VueJS"
    })

