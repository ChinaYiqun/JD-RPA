import base64
import json
import time

import requests
from pic_utils import image_to_base64

API_HOST = "http://127.0.0.1:8000"


# API_HOST = "http://124.223.85.176:8000"
def get_new_message_position(image_path, api_url=API_HOST + "/get_new_message_position"):
    """测试聊天界面分析API"""
    base64_image = image_to_base64(image_path)
    if not base64_image:
        return

    # 准备请求数据
    payload = {
        "image_base64": base64_image
    }

    try:
        response = requests.post(api_url, json=payload)
        result = response.json()
        print(json.dumps(result, indent=4, ensure_ascii=False))

    except requests.exceptions.RequestException as e:
        print(f"请求发生错误: {str(e)}")
    except json.JSONDecodeError as e:
        print(f"解析响应JSON时出错: {str(e)}")


def layout(api_url=API_HOST + "/layout"):
    try:
        response = requests.get(api_url)
        result = response.json()
        print(json.dumps(result, indent=4, ensure_ascii=False))

    except requests.exceptions.RequestException as e:
        print(f"请求发生错误: {str(e)}")
    except json.JSONDecodeError as e:
        print(f"解析响应JSON时出错: {str(e)}")


# for i in range(1,8):
#     get_new_message_position(f"resource/test/other{i}.png")
#     time.sleep(0.5)


def get_position(image_path, text, api_url=API_HOST + "/get_position"):
    """测试聊天界面分析API"""
    base64_image = image_to_base64(image_path)
    if not base64_image:
        return

    # 准备请求数据
    payload = {
        "image_base64": base64_image,
        "text": text
    }

    try:
        response = requests.post(api_url, json=payload)
        result = response.json()
        print(json.dumps(result, indent=4, ensure_ascii=False))

    except requests.exceptions.RequestException as e:
        print(f"请求发生错误: {str(e)}")
    except json.JSONDecodeError as e:
        print(f"解析响应JSON时出错: {str(e)}")

import re

text = "我需要等待3秒，然后再等5分，最后等10秒"
pattern = r"(\d+)秒"
result = re.findall(pattern, text)
print(result)
get_position(f"resource/test/left_3.png", "(\d+)(秒|分)")
