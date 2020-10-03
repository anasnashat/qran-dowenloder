import requests
from bs4 import BeautifulSoup
import threading
import webbrowser , os
import time
import multiprocessing
def a():
    link="https://surahquran.com/mp3/Majid-Alzamil/"

    num=0
    while num < 114:
        num=num+1
        a = str(link) +str(num)+".html"
        url= a
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
        rq = requests.session()
        rq.headers.update(headers)
        r = rq.get(url)
        soub = BeautifulSoup(r.content, 'lxml')
        for fv in soub.findAll('section',{'class' ,'post-content-area single-post-area'}):
            for f1 in fv.findAll('div',{'class':'container'}):
                for f3 in f1.findAll('div',{'class':'row'}):
                    for f2 in f3.findAll('div',{'class':'col-lg-8 posts-list'}):
                        for f4 in f2.findAll('div',{'class':'single-post row'}):
                            for f5 in f4.findAll('div',{'class':'col-lg-12'}):
                                for f6 in f5.findAll('div',{'class':'feature-img'}):
                                    vv=f6.findAll({"a"})
                                    acv=link.split("/")
                                    print(acv[4])
                                    for f7 in f6.findAll('p',{'style':'text-align: center;'}):
                                        for f11 in f7.findAll({'a':'href'}):
                                            print(f11.get('href'))
                                            dowlink=f11.get('href')
                                            #webbrowser.open(dowlink)
                                            # website = https://surahquran.com/qura.html#seen
a()
