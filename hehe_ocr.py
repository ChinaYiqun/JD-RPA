import re

import requests
import json

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

class CommonOcr(object):
    def __init__(self, img_path=None, is_url=False):
        # 通用文字识别
        self._url = 'https://api.textin.com/ai/service/v2/recognize/multipage'
        # 请登录后前往 “工作台-账号设置-开发者信息” 查看 x-ti-app-id
        # 示例代码中 x-ti-app-id 非真实数据
        self._app_id = '57d9faa41dfff1deebc5ca35b3c46ef2'
        # 请登录后前往 “工作台-账号设置-开发者信息” 查看 x-ti-secret-code
        # 示例代码中 x-ti-secret-code 非真实数据
        self._secret_code = 'f3098d78152fe4538e67412b56485a78'
        self._img_path = img_path
        self._is_url = is_url

    def recognize(self):
        head = {}
        try:
            head['x-ti-app-id'] = self._app_id
            head['x-ti-secret-code'] = self._secret_code
            if self._is_url:
                head['Content-Type'] = 'text/plain'
                body = self._img_path
            else:
                image = get_file_content(self._img_path)
                head['Content-Type'] = 'application/octet-stream'
                body = image
            result = requests.post(self._url, data=body, headers=head)
            return result.text
        except Exception as e:
            return e

    def get_text_position(self, target_text):
        """
        查找目标文本在图像中的左上角坐标 (x1, y1)

        参数:
        target_text: 需精确匹配的目标文本

        返回:
        坐标元组 (x1, y1)，未找到返回 None
        """
        ocr_result = self.recognize()
        if not isinstance(ocr_result, str):
            return None

        try:
            result_dict = json.loads(ocr_result)
            # 检查 OCR 接口返回状态
            if result_dict.get('code') != 200:
                return None

            # 遍历所有页面和文本行
            for page in result_dict.get('result', {}).get('pages', []):
                for line in page.get('lines', []):
                    # 精确匹配文本内容
                    if line.get('text') == target_text:
                        position = line.get('position', [])
                        # 返回左上角坐标 (x1, y1)
                        if len(position) >= 2:
                            return (position[0], position[1])
            return None  # 未找到匹配文本
        except json.JSONDecodeError:
            return None
        except Exception as e:
            return None

    def get_text_position_center_list(self, target_text):
        """
        查找目标文本在图像中的左上角坐标 (x1, y1)

        参数:
        target_text: 需精确匹配的目标文本

        返回:
        坐标元组 (x1, y1)，未找到返回 None
        """
        ocr_result = self.recognize()
        if not isinstance(ocr_result, str):
            return None

        try:
            result_dict = json.loads(ocr_result)
            # 检查 OCR 接口返回状态
            if result_dict.get('code') != 200:
                return None

            # 遍历所有页面和文本行
            position_list = []
            for page in result_dict.get('result', {}).get('pages', []):
                for line in page.get('lines', []):
                    # 精确匹配文本内容
                    text = line.get('text')
                    if text is not None and re.findall(target_text, text):
                    #if line.get('text') == target_text:
                        position = line.get('position', [])
                        # 返回左上角坐标 (x1, y1)
                        if len(position) == 8:
                            x = (position[0]+position[4])/2
                            y = (position[1]+position[5])/2
                            position_list.append((int(x),int(y)))
            # 将   position_list   进行排序，先按照x 坐标 升序排序，再按照y 坐标 升序排序
            position_list.sort(key=lambda x: (x[1], x[0]))
            return position_list
        except json.JSONDecodeError:
            return None
        except Exception as e:
            return None


if __name__ == "__main__":
    # 示例 1：传输文件
    # response = CommonOcr(img_path=r'resource/left_1.png') # blank
    response = CommonOcr(img_path=r'resource/test/left_1.png')
    result = response.get_text_position_center_list("jd_5e500c63eeec0")
    print(result)

