"""
13题
使用Sessions请求将cookie设置在会话中，再将得到的cookie继续添加在里面
"""

import requests
import re

Sessions = requests.Session()

def getcookies():
    headers = {
        "Cookie": "sessionid=wy3rgig9qry1ifd17dhdkt2acbjd3u8p"
    }
    response = Sessions.get(url='https://match.yuanrenxue.com/match/13',headers=headers)
    print(response.text)
    cookie = re.findall(r"'(.*?)'",response.text)
    print(cookie)
    cookies = ''.join(cookie[:-1])
    print(cookies)
    Sessions.cookies.set(cookies.split('=')[0],cookies.split('=')[1]) # 将获取的cookie设置在Sessions会话中
    return Sessions

def getdata():
    Sessions = getcookies()
    num = []
    for p in range(1,6):
        print(Sessions.cookies)
        print(Sessions.headers)
        headers = {
            'User-Agent': 'yuanrenxue.project'
        }
        url = f'https://match.yuanrenxue.com/api/match/13?page={p}'
        response = Sessions.get(url=url,headers=headers)
        print(response.text)

        # print(response.status_code)
        # print(response.text)
        lists = []
        data = response.json()['data']
        for da in data:
            lists.append(da['value'])
        num.append(sum(lists))
    return sum(num)

if __name__ == '__main__':
    num = getdata()
    print(num)
