#!/usr/bin/python


import urllib2
import uuid
import hashlib
import os

import parser_regexp
import parser_vk

import mydb
import list_site
import spic

path = spic.path_folder

def sha256hex(filePath):
    fh = open(filePath, 'rb')
    m = hashlib.sha256()
    while True:
        data = fh.read(8192)
        if not data:
            break
        m.update(data)
    return m.hexdigest()

def downloader(list_url,db):

    for url in list_url:

        if mydb.check(db,url):
            print "Exist picture"
        else:

            mypic = urllib2.urlopen(url)

            my_uuid = str(uuid.uuid4())
            name = path + my_uuid

            out_file = open(name,'wb')
            out_file.write(mypic.read())

            sha256 = sha256hex(name)

            if mydb.check_sha256(db,sha256):
                print "Exist, sha256"

                out_file.close()
                os.remove(name)

                print "Remove "+name


            else:

                mydb.insert(db,url,my_uuid,sha256)
                out_file.close()

                name_small = spic.get_small_pic(my_uuid)
                print name_small

                sha256_small = sha256hex(spic.path_small_folder+name_small)
                mydb.insert_small(db,name_small,sha256_small)

                print "Add in table"


def load_pic(sites,give_url,db):

    for site in sites:

        print "Start download, "+site[0]

        try:    #ignore 
            list_url = give_url (site)
            downloader(list_url,db)

        except:
            print "NOT CONNECT"

        print "Ok, "+site[0]



