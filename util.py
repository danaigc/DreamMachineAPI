import json

import requests


def dreamMachineMake(prompt, access_token):
    url = "https://internal-api.virginia.labs.lumalabs.ai/api/photon/v1/generations/"

    payload = {
        "user_prompt": prompt,
        "aspect_ratio": "16:9",
        "expand_prompt": True
    }
    headers = {
        "Cookie": "access_token=" + access_token,
        "Origin": "https://lumalabs.ai",
        "Referer": "https://lumalabs.ai",
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    response_json = json.loads(response.text)
    return response_json


# 定义刷新获取结果的异步函数
async def refreshDreamMachine(session, access_token):
    url = "https://internal-api.virginia.labs.lumalabs.ai/api/photon/v1/user/generations/"
    querystring = {"offset": "0", "limit": "10"}
    headers = {
        "Cookie": "access_token=" + access_token,
    }

    async with session.get(url, headers=headers, params=querystring) as response:
        response_text = await response.text()
        response_json = json.loads(response_text)
        return response_json


