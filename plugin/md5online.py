import mechanize

url = "http://md5online.net/"
res = [url, '']

def run(string, *para): 
    say = para[0]
    try:
        br = mechanize.Browser()
        br.open("http://md5online.net/")
        br.select_form(nr=0)
        br["pass"] = string
        response = br.submit()
        result = response.readlines()[48].replace('<center><p>md5 :<b>' + string + '</b> <br>pass : <b>', "").replace("</b></p></table>", "").strip()
        if not "not found in our database" in result:
            res[1] = result
    except:
        pass

    if say: say(res)
    return res

if __name__ == "__main__":
    def foo(string): print string
    run("7a57a5a743894a0e", foo)
    run("202cb962ac59075b964b07152d234b70", foo)
