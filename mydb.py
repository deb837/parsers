#!/usr/bin/python

import _mysql

user = "root"
password = "Ig9Zzyzh"
db_name = "funny_pic"
host = "localhost"

table = "tb_pictures"
table_small = "tb_small_pictures"

lol = "http://svalko.org/data/2012_06_03_16_03_cs302109_userapi_com_v302109484_15bd_7Vqp6zg473w.jpg"

def connect():
    db =_mysql.connect(host,user,password,db_name)
    return db


def check(db,source):
    #result = db.query('/"/"'+'select * from'+table+'/"/"')
    db.query("select * from "+table+" where source='"+source+"'")
    answ = db.store_result()
    return answ.num_rows()


def check_sha256(db,sha256):
    #result = db.query('/"/"'+'select * from'+table+'/"/"')
    db.query("select * from "+table+" where sha256='"+sha256+"'")
    answ = db.store_result()
    return answ.num_rows()


def insert(db,source,name, sha256):
#    print "insert into "+table+" (source,name,sha256) values ('"+source+"','"+name+"','"+sha256+"')"
    db.query("insert into "+table+" (source,name,sha256) values ('"+source+"','"+name+"','"+sha256+"')")

def insert_small(db,name, sha256):
    db.query("insert into "+table_small+" (name,sha256) values ('"+name+"','"+sha256+"')")



if __name__=='__main__':

    db = connect()

    insert(db,"http://svalko.org/data/2012_06_03_16_06_24_media_tumblr_com_tumblr_m0wpf4rxAo1qzyxjro1_500.jpg","37c79f28-ee65-44c8-a6b0-3e4a4efb477c","aaaaaaaaaaa")

    db.close()
