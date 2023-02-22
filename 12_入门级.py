"""
12题
参数加密 base64
"""
import requests
from lxpy import copy_headers_dict
from base64 import b64encode, b64decode
def basetrs(p):
    text = f'yuanrenxue{p}'
    return b64encode(text.encode('utf-8')).decode('utf-8')

def getdata():
    num = []
    for p in range(1,6):
        # p = 2
        m = basetrs(p)
        print(m)
        url = f'https://match.yuanrenxue.com/api/match/12?page={p}&m={m}'
        # print(url)
        headers = {'User-Agent': 'yuanrenxue.project', 'cookie': 'sessionid=wy3rgig9qry1ifd17dhdkt2acbjd3u8p'}
        response = requests.get(url=url,headers=headers)
        print(response.text)
        data = response.json()['data']
        lists = []
        for da in data:
            lists.append(da['value'])
        num.append(sum(lists))
    return sum(num)
if __name__ == '__main__':
    num = getdata()
    print(num)
