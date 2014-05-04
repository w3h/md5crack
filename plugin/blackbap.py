import urllib2
import urllib

url = "http://cracker.blackbap.org/"
res = [url, '']

def run(md5, *para):
    say = para[0]
    dict_attack = para[1]
    try:
        # MOD_B  modify this part
        site = r'http://cracker.blackbap.org/?do=search'
        data = urllib.urlencode({'isajax':'1', 'md5':md5})
        request = urllib2.Request(site, data)
        res[1] = dict_attack(md5, urllib2.urlopen(request).read())
        # MOD_E  modify this part
    except Exception,e:
        print '[*] %s' % e
        pass

    if say: say(res)
    return res

# ---------- Test Code ---------- 
if __name__ == "__main__":
    def foo(string): print string
    def dict_attack(ha, words):
        import re,hashlib
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
        try: unicode(ha, "ascii")
        except UnicodeError: ha = unicode(ha, "utf-8")
        else: ha = ha.encode("utf-8")        

        occurrences = False
        wordlist = re.split(r"\s+", words)
        for key in wordlist:
            try: unicode(key, "ascii")
            except UnicodeError: key = unicode(key, "utf-8")
            else: key = key.encode("utf-8")
            if hashlib.md5(key.encode("utf-8")).hexdigest() == ha: return key
        return ''

    # change this code
    run("c96770ba9ef4402a45a04827e6fe53a0", foo, dict_attack)
# ---------- Test Code ---------- 
