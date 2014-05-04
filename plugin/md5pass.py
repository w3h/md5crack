import mechanize


url = "http://md5pass.info/"
res = [url, '']

def run(string, *para): 
    say = para[0]
    try:
        br = mechanize.Browser()
        br.open(url)
        br.select_form(nr=1)
        br["hash"] = string
        response = br.submit()
        for i in response.readlines():
            if "Password - " in i:
                res[1] = i.strip().replace("Password - <b>", "").replace("</b>", "")
    except:
        pass

    if say: say(res)
    return res

if __name__ == "__main__":
    def foo(string): print string
    run("7a57a5a743894a0e", foo)
    run("202cb962ac59075b964b07152d234b70", foo)
