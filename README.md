# JD-RPA

## 说明
当前后端仅仅提供页面布局接口 和文本坐标定位接口
RPA 的主流程由前端同学控制 ，RPA 流程参考 https://xq5s55765m8.feishu.cn/wiki/Le4mwfeMNi92OXkg3bRc6X80ni8 

## 运行指令
```shell
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```


## 打包方式 (非必要)
```shell
pip install poetry
poetry new RPA --src  
cd RPA
# 移动到项目根目录
poetry build
```

