#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import os

from flask import Flask
app = Flask(__name__)

DEFAULT_PORT = 2001

host=os.environ['MYSQL_PORT_3306_TCP_ADDR']
user=os.environ['MYSQL_ENV_MYSQL_USER']
passwd=os.environ['MYSQL_ENV_MYSQL_PASSWORD']
database=os.environ['MYSQL_ENV_MYSQL_DATABASE']

def get_email_list( host, user, passwd, database):
    con = mdb.connect( host, user, passwd, database)
    with con: 
        cur = con.cursor()
        cur.execute("SELECT name,email FROM members")
        rows = cur.fetchall()
        results = []
        for row in rows:
            results.append("name: %s email: %s" %(row[0], row[1]))
    return '\n'.join(results)

def build_init (host, user, passwd, database):
    con = mdb.connect(host,user,passwd,database)
    with con:
        cur = con.cursor()
        cur.execute("create table members \
                    ( pkid int primary key auto_increment, \
                      name char(32) not null, \
                      email char(128) null);")
        cur.execute("insert into members(name,email) values('charles kim', 'hyungsok@cisco.com')")
        cur.execute("insert into members(name,email) values('woohyung choi', 'whchoi@cisco.com')")
        cur.execute("insert into members(name,email) values('jaemi lee', 'jaemlee@cisco.com')")
        cur.execute("insert into members(name,email) values('yoonwhan choi', 'yoocho@cisco.com')")

def get_port():
    if not os.environ['FLASK_PORT']:
        return DEFAULT_PORT
    else:
        return int( os.environ['FLASK_PORT'])
        
@app.route("/")
def hello():
    return get_email_list( host, user, passwd, database)



if __name__ == "__main__":
    build_init( host,user,passwd,database)
    app.run( host='0.0.0.0', port=get_port(), debug=True)
