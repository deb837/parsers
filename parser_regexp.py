#!/usr/bin/python

import sys
import urllib2
import re

def give_url(site):

    source = site[0]
    regex = site[1]
    first = site[2]
    second = site[3]

    response = urllib2.urlopen(source)
    html = response.read()

    result = re.finditer(regex,html)
    match = []

    for i in result:

        if (first == 0) and (second == 0) :
            match.append(i.group())

        elif (first == 0) and (second != 0):
            match.append(i.group()[:second])

        elif (first != 0) and (second == 0):
            match.append(i.group()[first:])

        else:
            match.append(i.group()[first:second])

    if (len(match) > 0) and (not match[0].startswith('http://')) :

        for i in range(len(match)):
            match[i] = source + match[i]

    return match


def __main__():

    for i in give_url(['http://exeypanteleev.com/','a href="i/.*.jpg" rel',8,-5]):
        print i


if __name__ == "__main__":
    __main__()
