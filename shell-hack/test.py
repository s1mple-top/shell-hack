from Result.result import results
from ways.Ways import webshell
from INFO.info import INFO
import socket
class Test:
    def __init__(self,way,url,pwd,cmd):
        self.way = way
        self.url = url
        self.pwd = pwd
        self.cmd = cmd

    def test(self):
        info = INFO(self.url, self.pwd,self.cmd,self.way)
        getshell=webshell(self.url,self.pwd,self.cmd,self.way)
        try:
            bool = getshell.connection()
        except:
            print("\n\033[0;31mconnection error;please check your url\033[0m")
            exit()
        if(bool=="success"):
            info.Printinfo()
            return results().success()
        else:
            return results().false()

    def portscan(self,address,port):
        s = socket.socket()
        try:
            s.connect((address, port))
            print("success")
        except:
            return False




