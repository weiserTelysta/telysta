FROM python:3.10

COPY . /www/web

WORKDIR /www/web

RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple --timeout=300
COPY requirements.txt . 
RUN pip install -r requirements.txt --timeout=300 -i https://pypi.tuna.tsinghua.edu.cn/simple

# 运行参数
EXPOSE 8000
ENTRYPOINT python manage.py migrate;

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "telystaback.wsgi:application"]