import google.generativeai as palm
import os
import json

hiddenFile = open('./json/hidden.json')
hiddenData = json.load(hiddenFile)


import requests as rq
import json
PALM_API_KEY = api_key=hiddenData["PaLMAPIKey"]
response = rq.post(f"https://generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generateText?key={PALM_API_KEY}", json={
    "prompt": {
        "text": input("YOU:") # 你的訊息
        },
    "temperature": 0.5,
    "candidateCount": 1 # 這邊調整你想要的回覆數量
})
for result in response.json()["candidates"]:
    print(result["output"])
    print("-"*100)