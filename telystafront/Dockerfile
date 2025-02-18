# telystafront/Docakfile
# 多阶段构建
# 阶段1：构建环境
FROM node:18-alpine as builder

WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# 阶段2：生产服务器
FROM nginx:alpine

# 复制构建结果
COPY --from=builder /app/dist /usr/share/nginx/html
# 自定义 Nginx 配置
COPY nginx.conf /etc/nginx/conf.d/default.conf

# 设置权限
RUN chown -R nginx:nginx /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]