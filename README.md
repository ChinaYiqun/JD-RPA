# JD-RPA

## 说明
当前后端仅仅提供页面布局接口 和文本坐标定位接口
RPA 的主流程由前端同学控制 ，RPA 流程参考 https://xq5s55765m8.feishu.cn/wiki/Le4mwfeMNi92OXkg3bRc6X80ni8 

## 运行指令
```shell
uvicorn main:app --host 0.0.0.0 --port 6666 --reload
```


## 打包方式 (非必要)
1. wheel 包

```shell
pip install poetry
poetry new RPA --src  
cd RPA
# 移动到项目根目录
poetry build
```
cd /etc/docker
vim daemon.json
{
  "registry-mirrors": [
    "https://registry.docker-cn.com",
    "https://mirror.aliyun.com",
    "https://docker.xuanyuan.me"

  ]
}

sudo systemctl restart docker
sudo systemctl daemon-reload
docker build -t jdrpa:latest . 
docker run -it --rm -p 6666:6000 jdrpa:latest
