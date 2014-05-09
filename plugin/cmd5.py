import mechanize
 
url = 'http://www.cmd5.com/'
res = [url, '']

def run(string, *para): 
    say = para[0]
    dict_attack = para[1]
    try:
        br = mechanize.Browser()
        br.open("http://www.cmd5.com/")
        br.select_form(name="aspnetForm")
        br["ctl00$ContentPlaceHolder1$TextBoxInput"] = string
        response = br.submit()
        info = ''.join(response.read())
        res[1] = dict_attack(string, info)
        '''
        for line in response.readlines():
            if 'ctl00_ContentPlaceHolder1_LabelAnswer' in line:
                line = line.replace('<span id="ctl00_ContentPlaceHolder1_LabelAnswer">', '')
                result = line[:line.find('<b')]
                result = result.strip()
                if not result:
                    break
                if "login.aspx" in result:
                    break

                res[1] = result
         '''
    except:
        pass

    if say: say(res)
    return res

if __name__ == "__main__":
    def foo(string): print string
    run("202cb962ac59075b964b07152d234b70", foo)
