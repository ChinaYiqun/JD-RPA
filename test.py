import base64
import json
import time

import requests

from pic_utils import mark_coordinate_on_image
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
        return result

    except requests.exceptions.RequestException as e:
        print(f"请求发生错误: {str(e)}")
    except json.JSONDecodeError as e:
        print(f"解析响应JSON时出错: {str(e)}")

import re

# text = "我需要等待3秒，然后再等5分，最后等10秒"
# pattern = r"(\d+)秒"
# result = re.findall(pattern, text)
# print(result)
# get_position(r"D:\pycharmProject\JD-RPA\resource\test\zj.png", "(\d+)(秒|分)")
get_position(r"D:\pycharmProject\JD-RPA\resource\test\zj.png", "转接")

# 遍历 resource/test 图片，获取图片文件名
# import os
# for filename in os.listdir("resource/test"):
#     if filename.endswith(".png"):
#         # result = get_position(f"resource/test/{filename}", "(\d+)秒|(\d+)分|(\d{2}:\d{2})")
#         result = get_position(f"resource/test/{filename}", "jd_5e500c63eeec0")
#         if result:  # 确保请求返回了结果
#             if result.get("type") == "click" and result.get("target"):  # 检查类型和目标列表
#                 # 提取target中第一个元素的x,y坐标
#                 x, y = result["target"][0]
#                 print(f"图片 {filename} 找到目标坐标: x={x}, y={y}")
#                 mark_coordinate_on_image( (x, y), f"resource/test/{filename}",f"resource/result_tmp/{filename}_mark.png")
#             else:
#                 print(
#                     f"图片 {filename} 未找到有效目标 (类型: {result.get('type')}, 目标数量: {len(result.get('target', []))})")
#         else:
#             print(f"图片 {filename} 处理失败，未返回结果")

