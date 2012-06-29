#!/usr/bin/python
# -*- coding: utf-8 -*-

import os


path_pic = 'small_pic/'
full_pic = 'pic/'
path_html = '/home/buhal/public_html/'

name = 'index.html'

files = os.listdir(path_html+path_pic)

page = open(path_html+name,'w')

page.write('<html> \n')
page.write('<head>')
page.write('<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />')
page.write('<link href="css/jquery.lightbox-0.5.css" rel="stylesheet" type="text/css" />')
page.write('<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.4.3/jquery.min.js"></script>')
page.write('<script type="text/javascript" src="js/jquery.lightbox-0.5.js"></script>')

page.write('<script type="text/javascript">')
page.write('jQuery(function()')
page.write('{')
page.write('    jQuery("a").lightBox')
page.write('    (')
page.write('     { ')
page.write('        overlayBgColor: \'#FFF\',')
page.write('        overlayOpacity: 0.6,')
page.write('        imageLoading: \'img/lightbox-ico-loading.gif\',')
page.write('        imageBtnClose: \'img/lightbox-btn-close.gif\',')
page.write('        imageBtnPrev: \'img/lightbox-btn-prev.gif\',')
page.write('        imageBtnNext: \'img/lightbox-btn-next.gif\',')
page.write('        containerResizeSpeed: 350')
page.write('     }')
page.write('    );')
page.write('});')
page.write('</script>')
#page.write('')

page.write('</head>')




page.write('<body> \n')

i=1

    
page.write('<p> <center> <p>')
page.write('<p> <h3> Нажмите F11 и медленно опускайтесь до конца страницы </h3>  <p>')
page.write('<p> </center> <p>')


for pic in files:
    page.write('<hr> \n')

    page.write('<p> <center> <p>')
    page.write(str(i)+'<b> \n')
    page.write('<a href="'+full_pic+pic[6:]+'"><img src="'+path_pic+pic+'"/></a>') 

    page.write('<p> <input type="button" value="delete" onclick="location.href=\'/delete.php?name='+pic +'\';" />')

#    page.write('<p> <form action="/delete.php?name='+pic+'">')
#    page.write('<p> <form action="non.html">')
#    page.write('<input type="button" name="delete" value="Delete">' )
#    page.write('</form>')

    page.write('<p> </center> <p>')
    i=i+1        

page.write('</body> \n')
page.write('</html>')

page.close()
