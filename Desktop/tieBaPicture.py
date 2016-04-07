
# -*- coding:utf-8 -*-

import string
import urllib2
import re
from bs4 import *
import os,socket
import sys 


reload(sys)
sys.setdefaultencoding( "utf-8" )


movieurl = 'http://tieba.baidu.com/p/4456286440'



#创建文件夹
path = os.getcwd();
new_path = os.path.join(path,"moviePicture")
if not os.path.exists(new_path):
    os.mkdir(new_path)

#设置文件的当前目录
os.chdir("moviePicture")

myurl = urllib2.urlopen(movieurl).read().decode('utf-8')

soup = BeautifulSoup(myurl)

list = soup.find_all('span' , attrs={'class':'red'})
if list:
    for li in list:
        if len(li.attrs) > 1:
            continue
        else:
            endpage = int(li.string)
            break

i=1
count=1
while i <=endpage:

    print movieurl+'?pn='+str(i)
    mypage = urllib2.urlopen(movieurl +'?pn='+str(i)).read().decode('utf-8')

    print u'打开网页成功'
    listimg = soup.find_all('img',attrs={'class':'BDE_Image'})

    for li in listimg:
        src = li['src']
        print u'开始下载第 %d 幅图片' %(count)
        print src

        try:
            content = urllib2.urlopen(src).read()
            f = open('%d.jpg' % (count) ,'wb')
            print content
            f.write(content)
        except:
            print u'出现异常 下载下一张'
            continue
        f.close()
        print u'完成一幅图片'
        count +=1
    i +=1
print u'全部完成'




