import urllib2
import urllib
import re

url = "http://md5decryption.com/"
res = [url, '']

def run(string, *para): 
    say = para[0]
    try:
        para = urllib.urlencode({'hash':string,'submit':'Decrypt+It!'})
        req = urllib2.Request(url)
        fd = urllib2.urlopen(req, para)
        data = fd.read()
        match = re.search(r'(Decrypted Text: </b>)(.+[^>])(</font><br/><center>)', data)
        if match: 
            res[1] = match.group(2).strip()
    except:
        pass

    if say: say(res)
    return res

if __name__ == "__main__":
    def foo(string): print string
    run("7a57a5a743894a0e", foo)
    run("202cb962ac59075b964b07152d234b70", foo)
