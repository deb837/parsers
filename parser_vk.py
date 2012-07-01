#!/usr/bin/python

import urllib2
import hashlib
import re


def give_url(site):

    gid = site[1]

    regex = '       <src_big>.*.jpg'

    server = 'http://api.vk.com/api.php?'
    mid = '4731069'
    secret = '059a4e757d'
    sid = '1971d4787d8028b25e1f9252df69d3c66756c602e2034b3b139689ff286a86'

    data = {
        'api_id':'2986891',
        'method':'wall.get',
        'owner_id': gid,
        'fields':'photo,sex,photo_big',
        'count':'25',
        'uid':'buhal',
        'v':'3.0'
        }


    open_sig = mid

    for i in sorted(data):
        open_sig += i+'='+data[i]

    open_sig += secret

    sig = hashlib.md5(open_sig).hexdigest()

    request = ''

    for i in sorted(data):
        request += i+'='+data[i]+'&'

    request += 'sid='+ sid + '&' + 'sig=' + sig

    response = urllib2.urlopen(server+request)
    html = response.read()

    result = re.finditer(regex,html)

    match = []

    for i in result:
        match.append(i.group()[16:])


    return match


if __name__ == '__main__':
    for i in give_url(['club','-36524488']):
        print i
