# FreeBuff-Increased-reading
FreeBuff阅读量增加
发现在Freebuff上某些文章竟达到惊人的百万级别阅读量围观，真的有这么多人嘛？
![image](https://github.com/MY0723/FreeBuff-Increased-reading/assets/74171727/7b124d0b-df39-467b-a224-34d595a7a960)
![image](https://github.com/MY0723/FreeBuff-Increased-reading/assets/74171727/57569481-361e-4cad-877a-13740ff62a42)

明明百万级别阅读量也就几条评论感觉有点怪怪的，我尝试去发现这个数量是怎么增加的
发现每刷新一回都是十几几十不等的阅读量增加，在数量上好像也没什么规律，但是每刷新一回基本上都会增加
![image](https://github.com/MY0723/FreeBuff-Increased-reading/assets/74171727/b2f5f5e6-c5a5-4034-ba27-6f4cdf05b130)
![image](https://github.com/MY0723/FreeBuff-Increased-reading/assets/74171727/6476168e-5894-43eb-88fa-835b78af7aeb)
好像这就是一个热度的展示，并不是真实的人数
如果我们简单写一个脚本每多少秒就访问一下文章岂不是可以刷浏览量，使我们的文章热度排名靠前呢

import time
import urllib.request
import argparse

parser = argparse.ArgumentParser(description='访问指定URL')
parser.add_argument('-u', '--url', type=str, required=True, help='需要访问的URL')
args = parser.parse_args()

while True:
    try:
        response = urllib.request.urlopen(args.url)
        print(f'{args.url} 访问成功')
    except:
        print(f'{args.url} 访问失败')
    time.sleep(1.3)
    
将文件保存为visit_url.py
使用方法：python visit_url.py -u 文章链接
![image](https://github.com/MY0723/FreeBuff-Increased-reading/assets/74171727/0781233b-c3f3-4cb5-afdd-0fc1bb1e2ed2)
原先
![image](https://github.com/MY0723/FreeBuff-Increased-reading/assets/74171727/a66d6cf1-38b7-4048-ae13-9f335ffdabaf)
过了一会
![image](https://github.com/MY0723/FreeBuff-Increased-reading/assets/74171727/2fe27367-9191-4ba5-bbec-01de868dccce)

