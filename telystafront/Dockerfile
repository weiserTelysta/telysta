# telystafront/Docakfile
# 多阶段构建
# 阶段1：构建环境
FROM node:18 AS builder

COPY . /www/web
WORKDIR /www/web


COPY package*.json ./
RUN npm ci
COPY ./telystafront/ .
RUN npm run build


FROM nginx
COPY --from=builder /www/web/telysta/telystafront/dist /usr/share/nginx/html 
COPY ./telystafront/nginx.conf /etc/nginx/conf.d/default.conf

# 自定义 Nginx 配置
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
