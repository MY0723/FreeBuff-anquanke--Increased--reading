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
