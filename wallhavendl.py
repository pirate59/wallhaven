# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 16:25:57 2015

@author: andrew
"""

#!/usr/bin/env python2


"""

Original program from reddit

#!/usr/bin/env python2

import Tkinter

#PATH = '/home/mohamed/wallpapers'
#PAGES = 5

def screenRes() :
	return { 'height' : Tkinter.Tk().winfo_screenheight(),
	         'width' : Tkinter.Tk().winfo_screenwidth() }

def save(url, filename) :
	import urllib
	from os import path
	sv = path.join(pt.get(), filename + '.' + 'jpg')
	urllib.urlretrieve(url, sv)

def crawl(height, width, page) :
	import urllib2
	from bs4 import BeautifulSoup
	import re
	url = 'http://alpha.wallhaven.cc/search?categories=111&purity=100&resolutions=%sx%s&sorting=random&order=desc&page=%s' % (width, height, page)
	#print url
	html = urllib2.urlopen(url)
	soup = BeautifulSoup(html, 'html')
	ss = soup.findAll('a', {'class' : 'preview' })
	for s in ss :
		filename = re.search(r'\d+', s['href']).group(0)
		url = 'http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-%s.jpg' % filename
		#print url
		save(url, filename)

def doit() :
	for i in range(1, int(pg.get())+1) :
		dic = screenRes()
		crawl(dic['height'], dic['width'], i)

root = Tkinter.Tk()
root.wm_title('randomWall')

Tkinter.Label(root, text="PATH").grid(row=0)
pt = Tkinter.Entry(root)
pt.insert(0, '/home/mohamed/wallpapers')
pt.grid(row=0, column=1)

Tkinter.Label(root, text="PAGES").grid(row=1)
pg = Tkinter.Entry(root)
pg.grid(row=1, column=1)

Tkinter.Button(root, text='GO !', command=doit).grid(row=3, columnspan=2)
root.mainloop()

"""











import Tkinter

tracker = 0
def screenRes() :
     return { 'height': 768, 'width': 1366}   
#	return { 'height' : Tkinter.Tk().winfo_screenheight(),
#	         'width' : Tkinter.Tk().winfo_screenwidth() }

def save(url, filename) :
    import urllib
    print 'imported'    
    from os import path
    sv = path.join(pt.get(), filename + '.' + 'jpg')
    print 'sv = '+  sv    
    urllib.urlretrieve(url ,sv)
#    print 'x = ' + x
#    out = open(filename,'r+')
#    print 'out writing'    
#    out.write(x.read())
#    print 'out written'
#    out.close()
#    print 'completed'
def crawl(height, width, page, z) :
    global tracker	
    import urllib2
    from bs4 import BeautifulSoup
    import re
    if search.get() == "":
 #	url = 'http://alpha.wallhaven.cc/search?categories=111&purity=100&resolutions=%sx%s&sorting=random&order=desc&page=%s' % (width, height, page)
        url = 'http://alpha.wallhaven.cc/search?categories=101&purity=111&sorting=random&order=desc&page=%s' % (page)
    else:
        url = 'http://alpha.wallhaven.cc/search?q=%s&categories=101&purity=111&sorting=relevance&order=desc&page=%s' % (z, page)
#	print url
    html = urllib2.urlopen(url)
    print html    
    soup = BeautifulSoup(html, 'html')
    print soup
    ss = soup.findAll('a', {'class' : 'preview' })
    for s in ss :
        filename = re.search(r'\d+', s['href']).group(0)
        url = 'http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-%s.jpg' % filename
        print url 		
        tracker += 1        
        print tracker        
        clabel.config(text = url)
        tracked.config(text ="Total Downloaded = %s" % str(tracker))
        
                    
        root.update()
        print 'saving file'
        save(url, filename)
        print 'saved'

def doit() :
   global tracker 
   z = ""
   for x in search.get():
        if x != " ":
            z = z + x
        else:
            z = z + "%20"
            
   tracker = 0        
   tracked.config(text ="Total Downloaded = %s" % str(tracker))            
#        print z
   for i in range(1, int(pg.get())+1) :
#        print i
        dic = screenRes()
        crawl(dic['height'], dic['width'], i, z)
        clabel.config(text = "Done")

root = Tkinter.Tk()
root.wm_title('randomWall')

x = Tkinter.Label(root, text="WALL HAVEN image downloader", font = ("Arial", 15)).grid(row=0, column = 1)

Tkinter.Label(root, text="PATH").grid(row=1)
pt = Tkinter.Entry(root, width = 60)
pt.insert(0, '/home/andrew/Desktop/paper')
pt.grid(row=1, column=1)

Tkinter.Label(root, text="PAGES").grid(row=4)
pg = Tkinter.Spinbox(root, from_=1, to_=10)
pg.grid(row=4, column=1)

Tkinter.Label(root, text="up to 24 images per page").grid(row=4, column = 3)

Tkinter.Button(root, text='GO !', command=doit).grid(row=5, columnspan=2)
Tkinter.Label(root, text="Search Criteria").grid(row=3)
Tkinter.Label(root, text="Leave Blank for random images").grid(row=3, column =3)
search = Tkinter.Entry(root, width = 60)
search.grid(row=3, column=1)
tracked = Tkinter.Label(root, text="Total Downloaded = %s" % str(tracker))
tracked.grid(row=6, column =3)
Tkinter.Label(root, text="Status").grid(row=6, column = 0)
clabel = Tkinter.Label(root, text="")
clabel.grid(row=6, column = 1)


root.mainloop()

"""

http://alpha.wallhaven.cc/search?q=monkey&categories=111&purity=100&resolutions=1024x768,1280x800,1366x768,1280x960,1440x900,1600x900,1280x1024,1600x1200,1680x1050,1920x1080,1920x1200,2560x1440,2560x1600,3840x1080,5760x1080&ratios=4x3,5x4,16x9,16x10,32x9,48x9&sorting=relevance&order=desc
http://alpha.wallhaven.cc/search?q=monkey&categories=111&purity=100&sorting=relevance&order=desc

http://alpha.wallhaven.cc/search?q=mario%20luigi&categories=111&purity=100&resolutions=1024x768,1280x800,1366x768,1280x960,1440x900,1600x900,1280x1024,1600x1200,1680x1050,1920x1080,1920x1200,2560x1440,2560x1600,3840x1080,5760x1080&ratios=4x3,5x4,16x9,16x10,32x9,48x9&sorting=relevance&order=desc
http://alpha.wallhaven.cc/search?q=mario%20luigi&categories=111&purity=100&sorting=relevance&order=desc
"""
