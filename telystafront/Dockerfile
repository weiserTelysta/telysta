FROM nginx  

COPY . /www/

RUN mkdir -p /data/sock

WORKDIR /www

RUN cp /www/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
