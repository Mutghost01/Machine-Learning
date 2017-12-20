import bs4 as bs
import urllib.request
import pandas as pd


kto=urllib.request.urlopen('http://www.bloomberght.com/doviz/dolar')
spider=bs.BeautifulSoup(kto,'lxml')

uzman_para= urllib.request.urlopen('http://uzmanpara.milliyet.com.tr/canli-borsa/').read()
soup=bs.BeautifulSoup(uzman_para,'lxml')


for spd in spider.find_all('table'):  #BeautifulSoup kütüphanesi ile döviz kurları'''
    print(spd.text)

spdr = pd.read_html('http://www.bloomberght.com/doviz/dolar')  #'''Pandas kütüphanesi ile döviz kurları'''
for fd in spdr:
    print(fd)


for paragph in soup.find_all('table'):    #'''BeautifulSoup kütüphanesi ile borsa değerleri'''
    print(paragph.text)

dfs = pd.read_html('http://uzmanpara.milliyet.com.tr/canli-borsa/')  #'''Pandas kütüphanesi borsa değerleri'''
for df in dfs:
    print(df)




