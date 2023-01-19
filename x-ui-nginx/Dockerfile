FROM nginx:1.23.2
RUN apt-get update
RUN apt-get install -y apache2-utils
ARG USERNAME
ARG PASS
RUN htpasswd -b -c /etc/nginx/.htpasswd ${USERNAME} ${PASS}