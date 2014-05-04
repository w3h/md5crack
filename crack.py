# coding=utf-8
import os
import threadpuul
import sys
import threading
import socket
import hashlib
import re
import glob

mutex = threading.Lock()
initmodstr = r'__all__ = ['
for py in glob.glob(r'./plugin/*.py'):
    py = py.replace('./plugin\\', '')
    py = py.replace('.py', '')
    if py != '__init__' and py != 'BeautifulSoup':
        initmodstr += '\'%s\', \n' % py

initmodstr = initmodstr + r']' 
with open('./plugin/__init__.py', 'w') as f: f.write(initmodstr)

try:
    plugin_available = True
    from plugin import *
    from plugin import __all__ #note this is the registered plugin list
except ImportError,e:
    plugin_available = False


def banner():
  print '''
|---------------------------------------------------------------|
| [*] MD5 Online Crack by HHH QQ:2969192549                     |
|---------------------------------------------------------------|
        '''

def usage():
  if len(sys.argv) < 2 or not plugin_available:
    print ''
    print 'Usage:' 
    print '  python crack.py [MD5] [Thread] '
    print '  python crack.py [MD5] '
    sys.exit(1)

def say(string):
    global mutex
    mutex.acquire()
    if string[1] =='': string[1] = 'No Find'
    print "[+] site: %-35s password:%s" % (string[0], string[1])
    mutex.release()


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


def main():
    banner()    
    usage()

    socket.setdefaulttimeout(20)

    thread = 5
    md5 = sys.argv[1]
    if len(sys.argv) == 3: thread = sys.argv[2]

    thread = int(thread)
    if thread > 1:
        pool = threadpuul.ThreadPool(thread)
        for p in __all__:
            action_plugin = eval(p)
            pool.add_task(action_plugin.run, md5, say, dict_attack)
        pool.wait_completion()
    else:
        result = None
        for p in __all__:
            action_plugin = eval(p)
            result = action_plugin.run(md5, say, dict_attack)


if __name__ == "__main__":
    main()


