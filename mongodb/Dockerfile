FROM ubuntu:14.04

RUN apt-get update && apt-get install python python-pip python-dev -y 
RUN pip install flask pymongo  

RUN mkdir -p /opt/app 

COPY ./app.py /opt/app
RUN chmod +x /opt/app/app.py

CMD /opt/app/app.py
