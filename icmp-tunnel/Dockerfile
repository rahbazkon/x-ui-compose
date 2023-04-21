FROM debian

RUN apt update
RUN apt install wget unzip -y

RUN wget https://github.com/esrrhs/pingtunnel/releases/download/2.7/pingtunnel_linux_amd64.zip 
RUN unzip pingtunnel_linux_amd64.zip

WORKDIR ./