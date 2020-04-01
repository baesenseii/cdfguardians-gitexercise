FROM ubuntu:19.10

RUN apt -y update
RUN apt install -y apache2


ADD ./app-data/lol.html /var/www/html/index.html

CMD apachectl -D FOREGROUND
