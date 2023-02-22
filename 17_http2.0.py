"""
17题
reqursts请求接口无法获取正常数据
安装httpx  pip install httpx[http2]
使用httpx模块对接口请求
"""
import requests,httpx
def getdata():
    headers = {
        # "authority": "match.yuanrenxue.com",
        # "method": "GET",
        # "scheme": "https",
        'user-agent': 'yuanrenxue.project',
        "Cookie": "sessionid=wy3rgig9qry1ifd17dhdkt2acbjd3u8p",
        # 'referer': 'https://match.yuanrenxue.com/match/17'
        }
    num = []
    for p in range(1,6):
        url = f'https://match.yuanrenxue.com/api/match/17?page={p}'
        client = httpx.Client(http2=True)
        response = client.get(url=url,headers=headers).json()
        # print(response.status_code)
        # print(response.text)
        data = response['data']
        lists = []
        for da in data:
            lists.append(da['value'])
        num.append(sum(lists))
    return sum(num)

if __name__ == '__main__':
    num = getdata()
    print(num)