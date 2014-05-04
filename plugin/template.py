import urllib2
import urllib

url = "http://md5.rednoize.com/"
res = [url, '']

def run(md5, *para):
    say = para[0]
    dict_attack = para[1]
    try:
        # MOD_B  modify this part
        site = url + '?s=md5&go.x=0&go.y=0&q=' + md5
        opener = urllib2.urlopen(site)
        info = str(opener.read())
        # MOD_E  modify this part

        res[1] = dict_attack(md5, info)
    except Exception,e:
        print '[*] %s' % e
        pass

    if say: say(res)
    return res

# ---------- Test Code ---------- 
if __name__ == "__main__":
    def foo(string): print string
    def dict_attack(ha, words):
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
