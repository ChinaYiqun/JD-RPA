import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from attr_info import closeMessagePostion, PositionModel
from pic_utils import *
from hehe_ocr import *
import datetime
import os
from paddle_ocr import PaddleOCRSingleton
def sanitize_filename(filename):
    """移除文件名中的非法字符，防止保存错误"""
    invalid_chars = r'[\\/:*?"<>|]'  # Windows系统不允许的文件名字符
    return re.sub(invalid_chars, '_', filename).strip()
def get_text_reg_position(image_base64,text,mark=False,match_type = "contains"):
    """
    获取关闭消息按钮的位置
    :param image_base64: 图片的base64编码
    :return: 关闭消息按钮的位置列表
    """
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"./text_reg_position/{(sanitize_filename(text))}_{timestamp}.jpg"
    # 确保tmp目录存在
    os.makedirs("./text_reg_position", exist_ok=True)
    base64_to_img(image_base64, filename)

    # response = CommonOcr(img_path=filename)
    #
    # result = response.get_text_position_center_list(text)
    ocr = PaddleOCRSingleton()
    ocr.recognize(filename)
    result = ocr.get_text_position_center_list(text,match_type)

    if not result:
        return PositionModel(type="None",target=[])

    if mark:
        for x,y in result:
            mark_coordinate_on_image((x,y),filename,f"./text_reg_position/{(sanitize_filename(text))}_{timestamp}_{x}_{y}.jpg")

    return PositionModel(type="click",target=result)




if __name__ == '__main__':
    image_path = r"D:\pycharmProject\JD-RPA\resource\test\zj.png"
    image_base64 = image_to_base64(image_path)
    # text = "jd_5e500c63eeec0"
    text = r"转接"
    mark = True
    position = get_text_reg_position(image_base64,text,mark,"equals")


    print(position)
