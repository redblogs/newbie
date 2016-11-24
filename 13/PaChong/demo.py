#!/usr/bin/python
#coding:utf-8

import urllib
import re,sys,os
def GetImgs():
    if not os.path.exists('douban_imgs'):
        os.mkdir('douban_imgs')
        os.chdir('douban_imgs')
    for num in 1000,1100,1200,1300:
        url = "http://www.douban.com/group/topic/73873048/?start=%d" % num
        content = urllib.urlopen(url).read()
        #print content
        #sys.exit()
        imgs = re.findall(r'<img class="pil" src="(.*)" alt="(.*)"',content)      # 图片链接如下，每个匹配项（.*）或者（.*\.jpg）都会以数组的形式保存
 #<img class="pil" src="http://img3.douban.com/icon/u56865303-6.jpg " alt="情人若寂寥">
        #print imgs 输出的结果为[('http://img3.douban.com/icon/u56865303-6.jpg ', '往事如风'),……]
        #sys.exit()
        for img in imgs:
            img_url = img[0]  # 数组的第一个元素即为第一个 （.*）的内容，
            img_name = img[1] # 数组的第二个元素即为第二个 （.*）的
            urllib.urlretrieve(img_url,"%s.jpg" % img_name)
if __name__ == "__main__":
    GetImgs()
