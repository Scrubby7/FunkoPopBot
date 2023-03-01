#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from bs4 import BeautifulSoup
import requests
import time, json

import morgans

#time.sleep(60)

t = "MTA3Mzc3NzEzNDY5NjQwNzA4MA.G0rNOJ.EnnGLT6Im3bbhgieS4jMML2AoF-Mew7xedCzg0"
l = "https://discord.com/api/oauth2/authorize?client_id=1073777134696407080&permissions=1634235578432&scope=bot"

flag = 0
startime = time.time()
oldPopList = []
newPopList = []

NerdomOldList = []
NerdomNewList = []
listOfFunkoEuropeUrlToSearch = ["https://funkoeurope.com/collections/whats-new-funko", "https://funkoeurope.com/collections/back-in-stock" ]
listOfNerdomUrlToSearch = ['https://www.nerdom.gr/el/funko']

def GetPopList(base_channel):
    pop_list = []
    channel = base_channel
    for toSearchUrl in listOfFunkoEuropeUrlToSearch:
        html_text = requests.get(toSearchUrl).text
        soup = BeautifulSoup(html_text, "html.parser")
        for pop in soup.find_all('div', class_='product-item__info'):
            info = {
                'name' : pop.find('a', class_='product-item__title text--strong link').text,
                'price' : pop.find('div', class_='product-item__price-list price-list').text.replace(' ', ''),
                'link' : 'https://funkoeurope.com'+pop.find(href=True)['href'],
                'channel' : channel,
            }
            pop_list.append(info)
        channel = channel+1
    return pop_list


def GetNerdomList(base_channel):
    pop_list = []
    channel = base_channel
    for toSearchUrl in listOfNerdomUrlToSearch:
        html_text = requests.get(toSearchUrl).text
        soup = BeautifulSoup(html_text, "html.parser")
        for pop in soup.find_all('div', class_='card__product-content__mid'):
            info = {
                'name' : pop.find('a', class_='multi-ellipsis-2').text,
                'price' : pop.find('span', class_='final__price').text.replace(' ', ''),
                'link' : pop.find(href=True)['href'],
                'channel' : channel,
            }
            pop_list.append(info)
        channel = channel+1
    return pop_list

def PrintNewPop(name,price,link):
    phrase = name + "\nPreco:"+price + "\nLink:"+link
    print(phrase)
    return phrase

try:
    with open('pop_funko_list.json', 'r') as f:
        oldPopList = json.load(f)
except:
    oldPopList = GetPopList(0)
    with open('pop_funko_list.json', 'w') as f:
        json.dump(oldPopList, f, indent=2)

try:
    with open('pop_nerdom_list.json', 'r') as f:
        NerdomOldList = json.load(f)
except:
    NerdomOldList = GetNerdomList(9999)
    with open('pop_nerdom_list.json', 'w') as f:
        json.dump(NerdomOldList, f, indent=2)

print("COMEÇA")
while True:
    newPopList = GetPopList(0)
    for pop in newPopList:
        if pop not in oldPopList:
            print("*********************NOVIDADE FUNKO*********************")
            oldPopList.append(pop)
            with open('pop_funko_list.json', 'w') as f:
                json.dump(oldPopList, f, indent=2)
            msg = PrintNewPop(pop['name'], pop['price'], pop['link'])
            morgans.sendMessage(msg, pop['channel'])
            time.sleep(5)

    NerdomNewList = GetNerdomList(9999)
    for pop in NerdomNewList:
        if pop not in NerdomOldList:
            print("*********************NOVIDADE NERDOM*********************")
            NerdomOldList.append(pop)
            with open('pop_nerdom_list.json', 'w') as f:
                json.dump(NerdomOldList, f, indent=2)
            msg = PrintNewPop(pop['name'], pop['price'], pop['link'])
            morgans.sendMessage(msg, pop['channel'])

    print("GOING TO SLEEP NOW")
    time.sleep(3 *60) #5 minutes interval




