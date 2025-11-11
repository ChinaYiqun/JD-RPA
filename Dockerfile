FROM ccr-2vdh3abv-pub.cnc.bj.baidubce.com/paddlepaddle/paddle:3.2.1

WORKDIR /app
COPY . /app
RUN pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple/
RUN uv pip install --no-cache-dir -r requirements.txt  --system   -i https://pypi.tuna.tsinghua.edu.cn/simple/
EXPOSE 6000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "6000"]

