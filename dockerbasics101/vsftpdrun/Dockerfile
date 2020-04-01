#Dockerfile for the vsftpd on Centos
FROM CentOS:7

#updating yum repo and installing the vsftpd and ufw
RUN yum -y update && yum install -y \
  vsftpd \
  ufw

#create a copy of the conf file as back up
COPY /etc/vsftpd.conf /etc/vsftpd.conf.orig

#ENabling and starting ufw and configure their ports
RUN systemctl enable ufw
RUN systemctl start ufw

RUN ufw allow 20/tcp
RUN ufw allow 21/tcp
RUN ufw allow 990/tcp
RUN ufw allow 40000:50000/tcp

#adding a test user
RUN useradd testuser

#creating a ftp folder and setting ownership
RUN mkdir /home/testuser/ftp
RUN chown nobody:nogroup /home/testuser/ftp
chmod a-w /home/testuser/ftp

#creating directory
mkdir /home/testuser/ftp/files
chown testuser:testuser /home/testuser/ftp/files

#Get the configured vsftpd.conf file in the forvsftpd directory and replace it
ADD ./vsftpd.conf /etc/vsftpd.conf
