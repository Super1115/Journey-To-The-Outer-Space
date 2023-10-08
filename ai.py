import google.generativeai as palm
import requests as rq
import json


hiddenFile = open('./json/hidden.json')
hiddenData = json.load(hiddenFile)
PALM_API_KEY = api_key=hiddenData["PaLMAPIKey"]
MODEL = "models/chat-bison-001" # 模型
METHOD = "generateMessage" # 要用模型的哪個功能
DATA = { # 要使用這個method需要傳送的資料
    "prompt": {
        "text": ""  # 這邊就是放要輸入的資料!!!
     },
    "temperature": 1.0,
    "candidateCount": 1 # 這邊調整你想要的回覆數量
}
response = rq.post(f"https://generativelanguage.googleapis.com/v1beta2/{MODEL}:{METHOD}?key={PALM_API_KEY}", json=DATA)

# ----------- 上面是傳送資料跟取得回復 ----- 下面則是單純把回復印出來

for result in response.json()["candidates"]:
    print(result["output"])
    print("-"*100)