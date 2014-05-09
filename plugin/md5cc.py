#coding=utf-8
import urllib2
import urllib
import pycurl
import StringIO
import mechanize
import BeautifulSoup

url = "http://www.md5.cc/"
res = [url, '']

def getAnswer(md5): 
    # [B] The code needs to change 
    rq = pycurl.Curl()
    b = StringIO.StringIO()    
    ansResponse = ''
    url_GET = "http://www.md5.cc/ShowMD5Info.asp?md5_str=" + str(md5)

    try:
        rq = pycurl.Curl()
        b = StringIO.StringIO()
        rq.setopt(pycurl.FOLLOWLOCATION, 1)
        rq.setopt(pycurl.MAXREDIRS, 5)
        rq.setopt(pycurl.CONNECTTIMEOUT, 60)
        rq.setopt(pycurl.TIMEOUT, 300)
        rq.setopt(pycurl.USERAGENT, 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:25.0) Gecko/20100101 Firefox/25.0')
        rq.setopt(pycurl.REFERER, 'http://www.md5.cc')
        rq.setopt(pycurl.URL, url_GET)
        rq.setopt(pycurl.WRITEFUNCTION, b.write)
        rq.perform()
        
        retcode = rq.getinfo(pycurl.HTTP_CODE)
        if retcode == 200:        
            ansResponse = b.getvalue()
    except Exception,e:
        print "[*] %s" % e
        pass
    finally:
        rq.close()
        b.close()

    return ansResponse
    # [E] The code needs to change 

def run(md5, *para):
    say = para[0]
    dict_attack = para[1]
    if dict_attack: res[1] = dict_attack(md5, getAnswer(md5))
    if say: say(res)
    return res

# ---------- Test Code ---------- 
if __name__ == "__main__":
    def foo(string): print string
    def dict_attack(ha, words):
        if not words: return ''
        import re,hashlib,chardet
        enc = chardet.detect(words)['encoding']
        words = words.decode(enc).encode('utf-8')

        def strip_tags(html):
            from HTMLParser import HTMLParser
            html=html.strip()
            html=html.strip("\n")
            result=[]
            parse=HTMLParser()
            parse.handle_data=result.append
            parse.feed(html)
            parse.close()
            return "".join(result)

        words = strip_tags(words)
        wordlist = re.split(r"\s+", words)
        for key in wordlist:
            if hashlib.md5(key).hexdigest() == ha: return key
        return ''

    # change this code
    run("202cb962ac59075b964b07152d234b70", foo, dict_attack)
# ---------- Test Code ---------- 
