# telystafront/Dockerfile

FROM node:18 AS builder

COPY . /www/web
WORKDIR /www/web


COPY package*.json ./
RUN npm ci
COPY . .


FROM nginx
COPY ./dist /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
