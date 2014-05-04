import mechanize

url = "http://www.2d5.net/"
res = [url, '']

def run(string, *para): 
    say = para[0]
    try:
        br = mechanize.Browser()
        br.open(url)
        br.select_form(name="chkmd5")
        br["md5"] = string
        response = br.submit()
        for line in response.readlines():
            line = line.replace('http://', '')
            if string in line and ':' in line:
                res[1] = line[line.find(':')+1:line.find('</font>')].strip()
    except:
        pass

    if say: say(res)
    return res 

if __name__ == "__main__":
    def foo(string): print string    
    run("7a57a5a743894a0e", foo)
