from flask import Flask, render_template, request
import requests 
import json

app = Flask(__name__)

# 你的API端点和密钥
API_ENDPOINT = '/Users/apple/Documents/GitHub/Journey-To-The-Outer-Space/PaLM_API_prompt.json'
API_KEY = 'your_api_key'

@app.route('/')
def home():
    return render_template('/Users/apple/Documents/GitHub/Journey-To-The-Outer-Space/templates/main page.html')


@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['user_message']

    # 准备API请求数据（根据你的API文档）
    api_data = {
        'api_key': API_KEY,
        'message': user_message,
        # ...其他可能的字段...
    }

    # 发送POST请求到API
    response = requests.post(API_ENDPOINT, data=api_data)
    
    # 解析API响应
    if response.status_code == 200:  # 如果请求成功
        api_response = response.json()  # 解析返回的JSON数据
        bot_response = api_response.get('bot_response', '')  # 从JSON数据中获取机器人的响应
    else:
        bot_response = 'Sorry, I am unable to respond right now.'  # 如果请求失败，发送一个默认消息

    return jsonify({'bot_response': bot_response})
