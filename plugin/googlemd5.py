import mechanize, sys, os, hashlib, re
from xgoogle.search import GoogleSearch
from xgoogle import BeautifulSoup
import re
import threading

url = 'http://www.google.com/'
res = [url, '']

def run(string, *para): 
    say = para[0]

#---------------Parsers definition---------------------

    class template():

        def __init__(self):
            pass #Nothing needed in __init__()

        def run(self, string):

            query = "site:ReverseIndexSite %s" % string

            #if not thread:
            #    say("Querying Google: '%s'" % query)

            gs = GoogleSearch(query)
            gs.results_per_page = 10
            results = gs.get_results()
            if len(results) >= 1:
                result = None #At the end result must be a string containing the decoded md5 hash
                result = ["ReverseIndexSite", result]
                if thread:
                    say(result)
                return result


    class googlewordlist():

        #Using an implementation of pybozo from: https://github.com/kura/pybozo
        def __init__(self):
            pass

        def crack(self, hash):
            user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/17.0.938.0 Safari/535.8"
            url = "http://www.google.com/search?sourceid=chrome&q=%s" % hash
            headers = {'User-Agent': user_agent}

            request = mechanize.Request(url, None, headers)
            response = mechanize.urlopen(request)

            #if not thread:
            #    say("Generating wordlist from: '%s'" % url)

            #Using beautifulsoup to get only text, no html tags from: http://stackoverflow.com/questions/1936466/beautifulsoup-grab-visible-webpage-text

            html = response.read()
            soup = BeautifulSoup.BeautifulSoup(html)
            texts = soup.findAll(text=True)

            def visible(element):
                if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
                    return False
                elif re.match('<!--.*-->', str(element)):
                    return False
                return True

            wordlist = filter(visible, texts)

            wordlist = [ word.encode('utf-8') for word in wordlist ]

            #if not thread:
            #    say("WordList entries: %i" % len(wordlist))
            plain_text = self.dictionary_attack(hash, wordlist)
            if plain_text:
                return plain_text

        def dictionary_attack(self, hash, wordlist):
            #if not thread:
            #    say("WordList attack: '%s'" % hash)
            for word in wordlist:
                if hashlib.md5(word).hexdigest() == hash.lower():
                    return word

        def run(self, string):
            result = self.crack(string)
            if result:
                return result


    class md5database():

        def __init__(self):
            pass

        def run(self, string):

            query = "site:http://md5-database.org/md5 %s" % string

            #if not thread:
            #    say("Querying Google: '%s'" % query)

            gs = GoogleSearch(query)
            gs.results_per_page = 10
            results = gs._get_results_page()
            texts = results.findAll(text=True)
            texts = ''.join(texts)
            results = re.findall(re.compile('MD5\}.*?MD5'),texts)
            for line in results:
                if string in line:
                    result = line[(line.find(',')+1):line.find('.')].strip()
                    return result
            
            return ''

#--------------------------------------------------------------------------


    sites = [
            googlewordlist,
            md5database
            ]

    result = []
    for site in sites:
        result.append(site().run(string))
    for index in result:
        if index != None:
            res[1] = index
            break

    if say: say(res)
    return res

if __name__ == "__main__":
    def foo(string): print string
    run("202cb962ac59075b964b07152d234b70", foo)
