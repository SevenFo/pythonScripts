import requests
from urllib import parse
url = "http://www.fjpit.com/studentportal.php/Jxxx/xskbxx/optype/2/xn/2019-2020/xq/2/dqz/13/sybmdmstr/6265,6417,6434,6572,1002091201911/bjmc/软件技术1911"
cookies = {
    "PHPSESSID":"ST5483nCPSNyRp6ar6vDDIWoEHcas01exampleorg"
}
headers = {
    'Host': 'www.fjpit.com',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.77',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://www.fjpit.com/studentportal.php/Jxxx/xskbxx/optype/1',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
}
{
    "user":"123456"
    "psw":"123456"
}
response = requests.get(url,cookies = cookies,)
requests.post
requests.get
response = parse.unquote(response.content.decode("utf-8"))
print(response) 