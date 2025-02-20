FROM python:3.10

COPY . /www/web

WORKDIR /www/web

RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple --timeout=300
RUN pip install uwsgi -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN sed -i 's/http:\/\/archive.ubuntu.com/http:\/\/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list
RUN apt-get update && apt-get install -y curl
COPY requirements.txt . 
RUN pip install -r requirements.txt --timeout=300 -i https://pypi.tuna.tsinghua.edu.cn/simple

RUN mkdir -p /data/log
RUN mkdir -p /data/sock

# 运行参数
EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate","uwsgi --ini uwsgi.ini"]
