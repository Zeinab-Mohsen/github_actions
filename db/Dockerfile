FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=p@ssw0rd
ENV MYSQL_DATABASE=userdb

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 3306