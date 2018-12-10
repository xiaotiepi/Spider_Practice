import requests
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 如果状态码不是200，引发HTTPError异常
        r.enconding = r.apparent_encoding
        r2 = requests.post(url)
        return r.text, r2
    except:
        return '产生异常'

if __name__ =='__main__':
    url = 'http://www.baidu.com'
    print(getHTMLText(url))