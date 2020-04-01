FROM ubuntu:19.10

RUN apt -y update
RUN apt install -y apache2
RUN systemctl enable apache2
RUN systemctl start apache2

ADD ./app-data/wtv.html /var/www/html/index.html
