import mechanize

url = 'http://md5.gromweb.com/'
res = [url, '']

def run(string, *para): 
    say = para[0]
    try:
        br = mechanize.Browser()
        br = br.open("http://md5.gromweb.com/query/%s" % string)
        res[1] = br.read()
    except:
        pass

    if say: say(res)
    return res

if __name__ == "__main__":
    def foo(string): print string
    run("7a57a5a743894a0e", foo)
    run("202cb962ac59075b964b07152d234b70", foo)  
