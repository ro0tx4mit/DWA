# DWA - Search The Deep Web Straight From Your Terminal


## About DWA (Recent Notice - 03/04/24)
DWA is a simple script written in Python3.11 in which it allows users to enter a search term (query) in the command line and DWA will pull all the deep web sites relating to that query. DWA2.0 is here, enjoy!
## Installation
1) ``git clone https://github.com/ro0tx4mit/DWA``<br/>
2) ``cd DWA``<br/>
3) ``python3 -m pip install -r requirements.txt``<br/>
4) ``python3 dwa.py --help``<br/>
## Usage 
Example 1: ``python3 dwa.py --query programming``<br/>
Example 2: ``python3 dwa.py --query="chat rooms"``<br/>
Example 3: ``python3 dwa.py --query hackers --amount 12``<br/>

 - Note: The 'amount' argument filters the number of results outputted<br/>
  
### Usage With Increased Anonymity 
Darkdump Proxy: ``python3 dwa.py --query bitcoin -p``<br/>
  
## Menu
```

     ____    __    _    __    ___ 
    |    \   \ \  / \  / /   /   \
    |  |  |   \ \/ _ \/ /   /  -  \
    |____/     \__/ \__/   /__/ \__\
                                        
        Developed By: RO0TX4MIT
        https://github.com/ro0tx4mit 
            ro0tx4mit.github.io
              Version: 1.0

usage: dwa.py [-h] [-v] [-q QUERY] [-a AMOUNT] [-p]

options:
  -h, --help            show this help message and exit
  -v, --version         returns darkdump's version
  -q QUERY, --query QUERY
                        the keyword or string you want to search on the deepweb
  -a AMOUNT, --amount AMOUNT
                        the amount of results you want to retrieve (default: 10)
  -p, --proxy           use darkdump proxy to increase anonymity

```


## Ethical Notice
The developer of this program, Amit Kumar Bisoyi, is not resposible for misuse of this data gathering tool. Do not use DWA to navigate websites that take part in any activity that is identified as illegal under the laws and regulations of your government. May God bless you all. 

## License 
MIT License<br/>
Copyright (c) ro0tx4mit
