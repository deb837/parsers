#!/usr/bin/python

from lib_loader import load_pic  

import parser_regexp
import parser_vk

import mydb

from list_site import sites_rg
from list_site import sites_vk


if __name__ == '__main__':

    db = mydb.connect()
    
    load_pic ( sites = sites_rg, give_url = parser_regexp.give_url, db = db )
    load_pic ( sites = sites_vk, give_url = parser_vk.give_url, db = db )


    db.close()
