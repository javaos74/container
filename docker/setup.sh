#!/bin/bash

docker build -t myapp:0.6 . 

docker run --name mydb -e MYSQL_USER=admin -e MYSQL_DATABASE=dclab -e MYSQL_ROOT_PASSWORD=1234Qwer -e MYSQL_PASSWORD=1234Qwer -d mysql 

docker run --name app1 -e FLASK_PORT=3000 --link mydb:mysql -d myapp:0.6 