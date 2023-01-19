FROM nginx:1.23.2
RUN apt-get update
RUN apt-get install apache2-utils
ARG USERNAME
ARG PASS
RUN htpasswd -c /etc/nginx/.htpasswd -b ${USERNAME} ${PASS}