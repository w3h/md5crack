import mechanize
import BeautifulSoup


url = "http://www.md5this.com/"
res = [url, '']

def run(string, *para): 
    say = para[0]
    try:
        br = mechanize.Browser()
        br.open("%scrackit.php" % url)
        br.select_form(nr=0)
        br["h"] = string
        response = br.submit()
        soup = BeautifulSoup.BeautifulSoup(''.join(response.readlines()))
        fonts = soup.findAll('font')
        for font in fonts:
            result = font.renderContents()
            if result.find(string) == -1:
                continue
            soup = BeautifulSoup.BeautifulSoup(result)
            bs = soup.findAll('b')
            res[1] = bs[1].renderContents().strip()     
    except:
        pass
    
    if say: say(res)
    return res

if __name__ == "__main__":
    def foo(string): print string
    run("202cb962ac59075b964b07152d234b70", foo)
