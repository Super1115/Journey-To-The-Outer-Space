from flask import Flask, render_template, request, Response
import json
import ai

app = Flask(__name__)

# 你的API端点和密钥
API_ENDPOINT = '/Users/apple/Documents/GitHub/Journey-To-The-Outer-Space/PaLM_API_prompt.json'
API_KEY = 'your_api_key'

with open('/Users/apple/Documents/GitHub/Journey-To-The-Outer-Space/json/PaLM_API_prompt.json', 'r') as file:
    responses = json.load(file)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/get_response', methods=['POST'])  # 假设你使用 POST 方法发送数据
def get_response():
    user_input = request.form['user_input']  # 从表单中获取用户输入
    response = ai.get_ai_response(user_input)  # 从 ai_module 获取响应
    return render_template('response.html', response=response)  # 渲染响应


if __name__ == '__main__':
    app.run(debug=True)  
