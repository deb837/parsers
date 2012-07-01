#!/usr/bin/python
from PIL import Image

path_folder = '/home/buhal/public_html/wordpress/wp-content/pic/'
path_small_folder =  '/home/buhal/public_html/wordpress/wp-content/small_pic/'

prefix = 'small_'


def get_small_pic(name):

    im = Image.open(path_folder+name)
    size = im.size

    max_size =  sorted(size)[1]

    if max_size > 500:

        k =  max_size/500.0
        print k

        new_size = ( int(size[0]/k), int(size[1]/k) )
#        print size
#        print new_size

        new_im = im.resize(new_size)

#        new_im.show()
        new_im.save(path_small_folder+prefix+name,'JPEG')

    else:
        print "Clone pic"
        im.save(path_small_folder+prefix+name,'JPEG')

    return prefix+name

if __name__ == '__main__':

    get_small_pic('pic3.jpg')
