#-*- coding:utf-8 –*-
import urllib
import urllib2
import re
import thread
import time

class caihaopage1:
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
        self.pageStories = []
        self.url = 'http://www.xjhr.com/job/?JobType=1000&WorkPlace=0&Trade=0&Property=0&JobProperty=0&Degree=0&WorkYears=0&JobTag=0&Weal=0&MonthPay=0&PublishDate=90&Key=&Orderid=0&Styleid=1&PageNo=1'
        self.headers = {'User-Agent': self.user_agent}

    def getpage(self, index):
        user_agant = self.user_agent
        url = self.url
        headers = {'User-Agent': user_agant}
        result = urllib2.Request( url, headers=headers )
        response = urllib2.urlopen( result )
        pageCode = response.read().decode( 'utf-8' )
        return pageCode

    def pageindex(self, index):
        pageCode = self.getpage( index )
        pattern = re.compile('<li class="seaList12">.*?<a.*?>(.*?)</a>.*?<li class="seaList13">.*?<a.*?>(.*?)</a>.*?<li class="seaList14">.*?<span.*?>(.*?)</span>.*?<li class="seaList15">.*?(.*?)</li>',re.S )
        items = re.findall( pattern, pageCode )
        for i in items:
            for g in i:
                input = raw_input()
                print g

    def start(self):
        print "--------------------------------------page1------------------------------------"
        print "-------------             i'm    Separation   line         --------------------"
        self.getpage(index=caihaopage1)
        self.pageindex(index=caihaopage1)

