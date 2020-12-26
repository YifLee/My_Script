# -- coding: utf-8 --
import requests
from pyquery import PyQuery as pq

cookie=""
if not cookie:
    cookie = input("cookie")
sckey = input("sckey")
url = 'https://www.52pojie.cn/home.php?mod=task&do=draw&id=2'
url1 = 'https://www.52pojie.cn/home.php?mod=task&do=apply&id=2'
headers = {'cookie':cookie,
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4265.0 Safari/537.36 Edg/87.0.644.4'}
requests.get(url1, headers=headers)
req = requests.get(url, headers=headers).text
    
doc = pq(req)
msg = doc('.vwmy a').text() + '\t' + doc('#messagetext p').text()
print(msg)
if not cookie:
    print('cookie为空')
if sckey:
    send_url = f'https://sc.ftqq.com/{sckey}.send?text={msg}'
    requests.get(send_url)
