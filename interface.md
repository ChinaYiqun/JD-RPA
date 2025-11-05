已帮你修改接口文档，补充了 `match_type` 字段两种取值的具体含义，以下是修改后的完整文档：

### 接口文档

#### 1. `/get_position` 接口  
- **接口路径**：`/get_position`  
- **请求方法**：`POST`  
- **标签**：`["位置获取"]`  
- **摘要**：获取位置坐标  
- **描述**：  
  根据传入的图片base64编码和目标文案信息，返回匹配的位置坐标。  
  - 新消息定位：`text` 格式支持 `(\d+)秒|(\d+)分|(\d{2}:\d{2})`（如“3秒”“5分”“12:30”）  
  - 用户定位：`text` 为用户名  
  - 转接系列操作参考
    - 指定咨询组定位 `text` 为 指定咨询组 ,match_type='equals' (精准查找)
    - AI转接组定位 `text` "AI转接组" 
    - 转接定位 `text` "转接"  ,match_type='equals' (精准查找)
##### 请求参数（请求体）  
请求体模型为 `NewMessageRequest`，字段说明如下：  

| 字段名         | 类型   | 是否必填 | 默认值   | 描述                     |  
|----------------|--------|----------|----------|--------------------------|  
| image_base64   | string | 是       | -        | 图片的base64编码字符串   |  
| text           | string | 是       | -        | 目标匹配文案信息         |  
| match_type     | string | 否       | "contains" | 匹配方式，`contains`为模糊匹配，`equals`为精确匹配 |  

##### 响应数据  
响应模型为 `PositionModel`，字段说明如下：  

| 字段名   | 类型                  | 描述                 |  
|----------|-----------------------|----------------------|  
| type     | string                | 匹配类型标识         |  
| target   | List[Tuple[int, int]] | 匹配到的位置坐标列表，每个坐标为（x, y）元组 |  

响应描述：返回匹配目标的位置坐标信息  

---

#### 2. `/layout` 接口  
- **接口路径**：`/layout`  
- **请求方法**：`GET`  
- **标签**：`["布局"]`  
- **摘要**：获取布局信息  
- **描述**：返回预设的界面布局区域坐标及尺寸信息  

##### 响应数据  
响应模型为 `LayoutModel`，字段说明如下：  

| 字段名                          | 类型       | 描述                                                                 |  
|---------------------------------|------------|----------------------------------------------------------------------|  
| message_list_area               | List[int]  | 消息列表区域，格式为 `[x, y, w, h]`（左上角横坐标、纵坐标、宽度、高度） |  
| message_list_menu_height        | int        | 消息列表菜单高度                                                     |  
| message_list_item_height        | int        | 消息列表项高度                                                       |  
| chat_history_area               | List[int]  | 聊天历史区域，格式为 `[x, y, w, h]`                                  |  
| chat_history_search_bar_height  | int        | 聊天历史搜索栏高度                                                   |  
| chat_history_info_bar_height    | int        | 聊天历史信息栏高度                                                   |  
| chat_history_product_info       | int        | 聊天历史中商品信息区域高度                                           |  
| input_box_area                  | List[int]  | 输入框区域，格式为 `[x, y, w, h]`                                    |  
| send_button                     | List[int]  | 发送按钮坐标，格式为 `[x, y]`（左上角坐标）                          |  
| search_button                   | List[int]  | 搜索框坐标，格式为 `[x, y]`（左上角坐标）                            |  
| search_customer                 | List[int]  | 搜索顾客按钮坐标，格式为 `[x, y]`（左上角坐标）                      |  
| search_customer_list_top        | List[int]  | 搜索结果列表第一个用户坐标，格式为 `[x, y]`（左上角坐标）            |  

响应描述：返回界面各元素的布局区域及尺寸信息  

