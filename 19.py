import requests

def getdata():
    url = 'https://match.yuanrenxue.com/api/match/19?page=3'
    headers = {
        'User-Agent': 'yuanrenxue.project',
        'Cookies':'sessionid=ptw5wg40b0h0shakbiezpmv8iy7y9ttb'
    }
    respponse = requests.get(url=url,headers=headers)
    print(respponse.status_code)
    print(respponse.text)

if __name__ == '__main__':
    getdata()