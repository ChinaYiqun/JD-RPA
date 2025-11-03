from fastapi import FastAPI, HTTPException
from attr_info import PositionModel, LayoutModel, NewMessageRequest, generate_layout_json
from dummy.ocr_reg_postion import get_text_reg_position
from pic_utils import decode_base64_image
# 记录log
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI(title="京东RPA", description="")





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
    """
    获取文本在图片中的位置坐标

    参数:
    image_base64: 图片base64编码
    text: 需精确匹配的目标文本

    返回:
    坐标元组 (x1, y1)，未找到返回 None
    """
    if not decode_base64_image(request.image_base64):
        raise HTTPException(status_code=400, detail="无效的base64图片编码")
    return get_text_reg_position(request.image_base64,request.text,request.match_type)

@app.get("/layout",
         response_model=LayoutModel,
         tags=["布局"],
         summary="获取布局信息",
         description="获取布局信息",
         response_description="布局信息")
async def get_layout():
    return generate_layout_json()


if __name__ == '__main__':
    # 启动FastAPI应用
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


# uvicorn main:app --host 0.0.0.0 --port 8000 --reload
