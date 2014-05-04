import mechanize
import BeautifulSoup


url = "http://www.md5.com.cn/"
res = [url, '']

def run(string, *para): 
    say = para[0]
    try:
        br = mechanize.Browser()
        br.open(url)
        br.select_form('hash')
        br["md"] = string
        response = br.submit()
        soup = BeautifulSoup.BeautifulSoup(''.join(response.readlines()))
        reg = soup.find('div', {'id' : 'reg'})
        results = reg.findAll('span', {'class' : 'res green'})
        result = results[1].renderContents()
        if result.find('Not') == -1:
            res[1] = result.strip()       
    except:
        pass
    
    if say: say(res)
    return res

if __name__ == "__main__":
    def foo(string): print string
    run("202cb962ac59075b964b07152d234b70", foo)
