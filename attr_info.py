from fastapi import FastAPI
import json


from pydantic import BaseModel
from typing import List, Tuple


class NewMessageRequest(BaseModel):
    image_base64: str
    text:str


class CloseMessageRequest(BaseModel):
    image_base64: str
    userid: str = None

class LayoutModel(BaseModel):
    message_list_area: List[int]
    message_list_menu_height: int
    message_list_item_height: int
    chat_history_area: List[int]
    chat_history_search_bar_height: int
    chat_history_info_bar_height: int
    chat_history_product_info: int
    input_box_area: List[int]
    send_button: List[int]

    search_button:List[int]
    search_customer:List[int]
    search_customer_list_top:List[int]


class newMessagePostion(BaseModel):
    new_message_position: List[Tuple[int,int]]
    new_message_username: List[str]


class closeMessagePostion(BaseModel):
    close_message_position: List[Tuple[int,int]]

class PositionModel(BaseModel):
    type: str
    target: List[Tuple[int,int]]




def generate_layout_json():

    layout = LayoutModel
    layout.message_list_area = [64, 33, 280, 993] # x,y,w,h 代表：左上角横坐标, 纵坐标,宽度,高度
    layout.search_button =[431, 60] # 搜索框
    layout.search_customer = [539, 113] #搜索顾客
    layout.search_customer_list_top = [387, 161] #搜索列表第一个用户



    layout.message_list_menu_height = 198
    layout.message_list_item_height = 60

    layout.chat_history_area = [345, 36, 1210, 670]
    layout.chat_history_search_bar_height = 60
    layout.chat_history_info_bar_height = 52
    layout.chat_history_product_info = 44

    layout.input_box_area = [345, 747, 1210, 282]
    layout.send_button = [1485, 1005]

    return layout


