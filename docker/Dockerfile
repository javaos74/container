FROM ubuntu:14.04

RUN apt-get update && apt-get install python python-pip mysql-client-5.6 python-mysqldb libmysqlclient-dev python-dev -y 
RUN pip install flask mysqlclient 

RUN mkdir -p /opt/app 

COPY ./app.py /opt/app
RUN chmod +x /opt/app/app.py 

CMD /opt/app/app.py