from random import *
from time import *
import os,requests,bs4

#输出文字
def output(t):
    print(t)

#输入文字
def entry(t2):
    a = input()
    return a

#生成随机数
def rand(t3,t4):
    b = randint(t3,t4)
    return b

#获取当前时间
def hour():
    clock = strftime("%H:%M:%S")
    return clock

#程序等待
def wait(t5):
    sleep(t5)

#清屏
def clean():
    os.system("clear")

#关机
def s(num):
    os.system('shutdown -s -t ' + str(num))

#重启
def r(num2):
    os.system('shutdown -r -t ' + str(num))

#爬取网页文字或图片
def crawling(web,label):
    response = requests.get(web)
    response.encoding = "UTF-8"
    soup = bs4.BeautifulSoup(response.text,"lxml")
    data = soup.find_all(name = label)
    return data

def picture(web2,label2):
    response2 = requests.get(web2)
    response2.encoding = "UTF-8"
    soup2 = bs4.BeautifulSoup(response2.content,"lxml")
    data2 = soup2.find_all(name = label2)
    return data2