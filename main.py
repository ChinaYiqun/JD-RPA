from fastapi import FastAPI, HTTPException
from attr_info import PositionModel, LayoutModel, NewMessageRequest, generate_layout_json
from dummy.ocr_reg_postion import get_text_reg_position
from myloger import setup_logger
from pic_utils import decode_base64_image




app = FastAPI(title="京东RPA", description="")


logging = setup_logger("myname")


@app.get("/health", tags=["系统"])
def health_check():
    """健康检查接口"""
    return {"status": "healthy", "service": "京东RPA-API"}

@app.post("/get_position",
          tags=["位置获取"],
          response_model=PositionModel,
          summary="获取位置坐标",
          description='''image_base64 图片base64编码,text 文案信息
          新消息定位传入：text (\d+)秒|(\d+)分|(\d{2}:\d{2})
          用户定位传入：text 用户名
          ''',
          response_description = '''position 位置坐标''')
def api_get_text_reg_position(request: NewMessageRequest):
    if not decode_base64_image(request.image_base64):
        raise HTTPException(status_code=400, detail="无效的base64图片编码")
    # 提取请求数据并排除image_base64字段后记录日志
    request_data = dict(request)
    del request_data['image_base64']
    logging.info(f"get_position Request data : {request_data}")
    result = get_text_reg_position(request.image_base64, request.text, request.match_type,True)
    logging.info(f"get_position result data : {result}")
    return result

@app.get("/layout",
         response_model=LayoutModel,
         tags=["布局"],
         summary="获取布局信息",
         description="获取布局信息",
         response_description="布局信息")
async def get_layout():
    return generate_layout_json()



# uvicorn main:app --host 0.0.0.0 --port 6666 --reload
