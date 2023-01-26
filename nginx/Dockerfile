FROM nginx:1.21-alpine

RUN apk add --no-cache apache2-utils
# RUN touch /etc/nginx/.htpasswd
# RUN "echo -n 'admin:' >> /etc/nginx/.htpasswd"
# RUN "openssl passwd -apr1 >> /etc/nginx/.htpasswd"
# RUN cat /etc/nginx/.htpasswd
RUN htpasswd -cb /etc/nginx/.htpasswd admin admin
RUN cat /etc/nginx/.htpasswd

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

# RUN mkdir -p /home/app/static
# RUN mkdir -p /home/app/media
# RUN chmod -R 755 /home/app/static
# RUN chmod -R 755 /home/app/media
