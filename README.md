# shell-hack

## Tribute to Chinese ant sword；

## A Powerful terminal based webshell controller；

#### Usage :

```
Usage : 
        python3 shell-hack.py --url [URL] --way [METHOD] --pwd[AUTH]
        python3 shell-hack.py --shell create --pwd [AUTH]
        (Generate kill free webshell)
Example : 
        python3 shell-hack.py --url http://challenge-d1e1be944a48fd8c.sandbox.ctfhub.com:10800/backdoor/ --way post --pwd ant
Author : 
        s1mple-SUer QQ:3513582223 Wei:w_s1mple
        
If you have connected to webshell：
===>get info(get the information from server)
===>bypass(see the bypass ways)
===>readfile(read the file from server)
===>downfile(download file from server)
===>reshell(Have a rebound shell)
===>portscan(scan the port from server)
===>mysql(connect to the mysql and Execute SQL code)

```

#### Installation:

```
git clone https://github.com/s1mple-top/shell-hack
cd shell-hack
python3 shell-hack.py
```

#### Compatibility :

```
Enviroment :
    Attacker :
        Linux;macos;windows;Unix-like
        python3(My Python version 3.8.2)
```

#### Realize function

```
1. Generate a kill free shell; (it is not ruled out that some cannot be exceeded. 2. Automatically bypass the restrictions according to the system restrictions to read files; 3. Obtain probe execution commands; 4. Automatically spy and automatically select available functions for execution; 5. Database connection operation; 6. Obtain sensitive information on the server; 7. One click rebound shell; 8. Download files; 9. Scan ports; 10. Bypass deep-seated disable_functions
```

### Operation effect diagram：

#### Effect drawing of initial operation：

[![4lWEt0.png](https://z3.ax1x.com/2021/09/18/4lWEt0.png)](https://imgtu.com/i/4lWEt0)

#### Connection success effect：

[![4lWs4P.png](https://z3.ax1x.com/2021/09/18/4lWs4P.png)](https://imgtu.com/i/4lWs4P)

#### bypass some disable_functions:（Full automatic bypass）

[![4l4ujS.png](https://z3.ax1x.com/2021/09/18/4l4ujS.png)](https://imgtu.com/i/4l4ujS)

#### Connect to the mysql:

[![4lTS5d.png](https://z3.ax1x.com/2021/09/18/4lTS5d.png)](https://imgtu.com/i/4lTS5d)

### reshell:

[![4lHQBT.png](https://z3.ax1x.com/2021/09/18/4lHQBT.png)](https://imgtu.com/i/4lHQBT)

## Contributors:

## s1mple from NCU;



## remarks：

Tools are always tools, which will have some limitations; If you want to better learn security knowledge, you need to understand the vulnerability principle and trigger mechanism; Tools are only used by the supplier; Should not rely on;

## importance：

Note that this script is not for the services enabled by phpstudy, because the local php environment is required to get the version at the beginning, otherwise an error will be reported; because phpstudy cannot use the local terminal to execute php -v






