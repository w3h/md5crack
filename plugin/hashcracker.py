import urllib2
import BeautifulSoup


url = 'http://www.hashcracker.org/'
res = [url, '']

def run(string, *para): 
    say = para[0]
    try:
        md5url = "Index/index/md5/" + string + '.html'
        info = urllib2.urlopen(url + md5url).read()
        bt = BeautifulSoup.BeautifulSoup(info)
        linka = bt.find('a', {'href' : md5url})
        result = linka.renderContents().strip()
        if result.find('Not') == -1:
            res[1] = result[result.find(':') + 1:]
    except Exception,e:
        #print e
        pass

    if say: say(res)
    return res

if __name__ == "__main__":
    def foo(string): print string
    run("1bf3c27a4d49f617", foo)
    #run("202cb962ac59075b964b07152d234b70", foo)
    
