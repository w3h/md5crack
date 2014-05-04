import mechanize

url = "http://requnix.tk/"
res = [url, '']

def run(string, *para):
    say = para[0]
    try:
        br = mechanize.Browser()
        br = br.open("%smd5/api/txt.php?md5=%s" % (url,string))
        result = br.read().strip()
        if not result == "":
            res[1] = result
    except:
        pass

    if say: say(res)
    return res

if __name__ == "__main__":
    def foo(string): print string
    run("7a57a5a743894a0e", foo)
