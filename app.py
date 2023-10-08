from flask import Flask, request, jsonify, render_template
import requests  # 导入requests库

app = Flask(__name__)

# 你的API端点和密钥
API_ENDPOINT = '/Users/apple/Documents/GitHub/Journey-To-The-Outer-Space/PaLM_API_prompt.json'
API_KEY = 'your_api_key'


@app.route('/')
def home():
    return render_template('home.html')



@app.route('/ask', methods=['POST'])
def ask():
    print(request.form)  # Log the incoming request data
    user_message = request.form['user_message'].lower()
    bot_response = "This is a test response."
    print(bot_response)  # Log the response before sending it back
    response_json = json.dumps({'bot_response': bot_response})
    return Response(response_json, content_type='json/PaLM_API_prompt.json')


if __name__ == '__main__':
    app.run(debug=True)  
