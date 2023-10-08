from flask import Flask, render_template, request
import requests 

app = Flask(__name__)

# 你的API端点和密钥
API_ENDPOINT = '/Users/apple/Documents/GitHub/Journey-To-The-Outer-Space/PaLM_API_prompt.json'
API_KEY = 'your_api_key'

@app.route('/')
def home():
    return render_template('main.html')

