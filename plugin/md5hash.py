import mechanize
import BeautifulSoup

url = "http://www.md5-hash.com/"
res = [url, '']

def run(string, *para): 
    say = para[0]
    try:
        br = mechanize.Browser()
        br = br.open("http://www.md5-hash.com/md5-hashing-decrypt/%s" % string)
        soup = BeautifulSoup.BeautifulSoup(''.join(br.readlines()))
        result = soup.find('strong', {'class' : 'result'})
        if result: 
            res[1] = result.renderContents().strip()
    except:
        pass

    if say: say(res)
    return res

if __name__ == "__main__":
    def foo(string): print string
    run("202cb962ac59075b964b07152d234b70", foo)
