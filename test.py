import base64
import json
import requests



API_HOST = "http://127.0.0.1:8000"


#API_HOST = "http://124.223.85.176:8000"

def image_to_base64(image_path):
    """将图片文件转换为base64编码字符串"""
    try:
        with open(image_path, "rb") as image_file:
            base64_str = base64.b64encode(image_file.read()).decode('utf-8')
            base64_str = f"data:image/jpeg;base64,{base64_str}"
            if ',' in base64_str:
                base64_str = base64_str.split(',')[1]
            return base64_str
    except Exception as e:
        print(f"转换图片为base64时出错: {str(e)}")
        return None


def layout(api_url=API_HOST + "/layout"):
    try:
        response = requests.get(api_url)
        result = response.json()
        print(json.dumps(result, indent=4, ensure_ascii=False))

    except requests.exceptions.RequestException as e:
        print(f"请求发生错误: {str(e)}")
    except json.JSONDecodeError as e:
        print(f"解析响应JSON时出错: {str(e)}")


def get_position(image_path, text, match_type ,api_url=API_HOST + "/get_position"):
    """测试聊天界面分析API"""
    base64_image = image_to_base64(image_path)
    if not base64_image:
        return

    # 准备请求数据
    payload = {
        "image_base64": base64_image,
        "text": text,
        "match_type" :match_type
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
# 新消息定位
get_position(r"D:\pycharmProject\JD-RPA\resource\test\left_3.png","(\d+)秒|(\d+)分|(\d{2}:\d{2})","contains")
# 用户名称定位
get_position(r"D:\pycharmProject\JD-RPA\resource\test\left_3.png","jd_563eb175d499a","contains")

# 转接系列操作参考
# get_position(r"D:\pycharmProject\JD-RPA\resource\test\0_screenshot.png", "指定咨询组","equals")
# get_position(r"D:\pycharmProject\JD-RPA\resource\test\img_1.png", "转接","equals")
# get_position(r"D:\pycharmProject\JD-RPA\resource\test\img_1.png", "兜底咨询组","contains")
