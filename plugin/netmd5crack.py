import urllib2

url = 'http://www.netmd5crack.com/'
res = [url, '']

def run(string, *para): 
    say = para[0]
    attack = para[1]
    try:
        para = 'cgi-bin/Crack.py?InputHash=%s' % string
        req = urllib2.urlopen(url + para)
        data = req.read()
        res[1] = attack(string, site_wordlist)
    except:
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
    run("7a57a5a743894a0e", foo, dict_attack)
# ---------- Test Code ----------  
