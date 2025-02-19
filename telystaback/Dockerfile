# telystaback/Dockfile
# 使用多阶段构建
# 阶段1：构建环境
FROM python:3.10 as builder

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python -m pip install --upgrade pip

COPY requirements.txt .
RUN pip install --user -r requirements.txt

# 阶段2：运行环境
FROM builder

WORKDIR /app
ENV PATH="/app/.local/bin:$PATH"

# 复制构建结果
COPY --from=builder /root/.local /root/.local
COPY . .

# 创建专用用户
RUN groupadd -r django && useradd -r -g django django && \
    chown -R django:django /app

USER django

# 运行参数
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "telystaback.wsgi:application"]