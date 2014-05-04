import urllib2
import urllib

url = "http://md5.my-addr.com/"
res = [url, '']

def run(string, *para):
    say = para[0]
    dict_attack = para[1]
    try:
        site = 'http://md5.my-addr.com/'
        rest = 'md5_decrypt-md5_cracker_online/md5_decoder_tool.php'
        para = urllib.urlencode({'md5':string})
        req = urllib2.Request(site+rest)
        fd = urllib2.urlopen(req, para)
        res[1] = dict_attack(string, fd.read())
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
    run("202cb962ac59075b964b07152d234b70", foo, dict_attack)
# ---------- Test Code ---------- 
