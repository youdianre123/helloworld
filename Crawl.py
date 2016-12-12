import urllib2
import urllib
null = ''

class Crawl:

    def __init__(self, url):
        self.url = url

    def post(self, data):
        req = urllib2.Request(self.url)
        reqData = urllib.urlencode(data)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        response = opener.open(req, reqData)
        return response.read()
    def getContent(self, data):    
        line = data['query']
        error = []
        contentList = []
        try:
            dictData = eval(self.post(data)) #print res.decode("unicode_escape")
            res = dictData['dict_result']['simple_means']['symbols'][0]
            title = line + "[" + res['ph_am'].decode("unicode_escape").encode("utf-8")+"]"
            
            content = [title]
            for i in res['parts']:
                aa = i['part']
                means = [v.decode("unicode_escape").encode("utf-8") for v in i['means']]
                content.append(aa + "".join(means))
            contentList.append(";".join(content) + "\n")       
        except:
            error.append(line)
            print line
        return contentList, error
