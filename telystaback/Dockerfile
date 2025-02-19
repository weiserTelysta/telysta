FROM python:3.10

COPY . /www/web

WORKDIR /www/web

RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple --timeout=300
RUN apt-get update && apt-get install -y curl
COPY requirements.txt . 
RUN pip install -r requirements.txt --timeout=300 -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY . .

# 运行参数
EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && gunicorn --bind 0.0.0.0:8000 telystaback.wsgi:application"]
