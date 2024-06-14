import json

import requests

# proxies = {
#     "http": "http://127.0.0.1:7890",
#     "https": "http://127.0.0.1:7890"
# }
proxies = {}


def dreamMachineMake(prompt, access_token, img_file=None):
    url = "https://internal-api.virginia.labs.lumalabs.ai/api/photon/v1/generations/"

    if img_file:
        print("uploading image")
        img_url = upload_file(access_token, img_file)
        # print(img_url)
        payload = {
            "aspect_ratio": "16:9",
            "expand_prompt": True,
            "image_url": img_url,
            "user_prompt": prompt
        }
    else:
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

    response = requests.post(url, json=payload, headers=headers, proxies=proxies)

    response_json = json.loads(response.text)
    return response_json


def refreshDreamMachine(access_token):
    url = "https://internal-api.virginia.labs.lumalabs.ai/api/photon/v1/user/generations/"
    querystring = {"offset": "0", "limit": "10"}
    headers = {
        "Cookie": "access_token=" + access_token,
    }

    response = requests.get(url, headers=headers, params=querystring, proxies=proxies)
    response_text = response.text
    response_json = json.loads(response_text)
    return response_json


def get_signed_upload(access_token):
    url = "https://internal-api.virginia.labs.lumalabs.ai/api/photon/v1/generations/file_upload"
    params = {
        'file_type': 'image',
        'filename': 'file.jpg'
    }
    headers = {
        "Cookie": "access_token=" + access_token,
    }
    response = requests.post(url, params=params, headers=headers, proxies=proxies)
    response.raise_for_status()
    return response.json()


def upload_file(access_token, file_path):
    try:
        signed_upload = get_signed_upload(access_token)
        presigned_url = signed_upload['presigned_url']
        public_url = signed_upload['public_url']

        with open(file_path, 'rb') as file:

            response = requests.put(presigned_url, data=file,
                                    headers={'Content-Type': "image/*", "Referer": "https://lumalabs.ai/",
                                             "origin": "https://lumalabs.ai"}, proxies=proxies)

        if response.status_code == 200:
            print("Upload successful:", public_url)
            return public_url
        else:
            print("Upload failed.")
    except Exception as e:
        print("Upload failed.")
        print("Error uploading image:", e)


def uploadImage(access_token, file_path):
    url = "https://internal-api.virginia.labs.lumalabs.ai/api/photon/v1/generations/file_upload?file_type=image" \
          "&filename=file.jpg"

    with open(file_path, 'rb') as file:
        files = {"file": file}

        headers = {
            "Cookie": "access_token=" + access_token,
            "User-Agent": "Apipost/8 (https://www.apipost.cn)"
        }

        response = requests.post(url, headers=headers, files=files, proxies=proxies)

    print(response.text)

    img_url = json.loads(response.text)["public_url"]
    print(img_url)
    return img_url
