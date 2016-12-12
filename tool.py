import os
import Crawl
import time
path = "/media/youdianre/project/com/English/new/a/"

def test():
    url = 'http://fanyi.baidu.com/v2transapi'
    data = {'from':'en','to':'zh','transtype':'translang','simple_means_flag':'3'}
    crawl = Crawl.Crawl(url)
    for i in range(10,50):
        with open("testNew/" + str(i) + ".txt", 'r') as test:
            print "=======" + str(i) + "=========="
            with open("testA/wordlist" + str(i) + ".txt", 'ab+') as file:
                for line in test.readlines():
                    data['query'] = line.strip()
                    dict_api, error = crawl.getContent(data)
                    for i in dict_api:
                        file.write(i)
        time.sleep(10)

def testError():
    
    list = ['maim','makeshift','malediction','malefactor','maleficent','malice','malignant','mallet','malodor','manacle','maneuver','mangy','maraud']

    url = 'http://fanyi.baidu.com/v2transapi'
    data = {'from':'en','to':'zh','transtype':'translang','simple_means_flag':'3'}
    crawl = Crawl.Crawl(url)
    with open("testA/wordlist44.txt", 'ab+') as file:
        for v in list:
            data['query'] = v
            res, error = crawl.getContent(data)
            for i in res:
                file.write(i)
