import requests
import json
url = "https://jinshuju.net/graphql/f/kxrHuH"
Data = {
    "operationName":"CreatePublishedFormEntry",
    "variables":{
        "input":{
            "formId":"kxrHuH",
            "entryAttributes":{
                "field_27":"2020-05-01",
                "field_9":"余李墨",#姓名
                "field_4":"",#学号
                "field_23":"15080119671",
                "field_19":"6MYv",
                "field_24":"福建省莆田市",
                "field_11":{
                    "latitude":"25.408979",
                    "longitude":"118.580948",
                    "address":"福建省莆田市仙游县度尾镇"
                },
                "field_25":{
                    "province":"福建省",
                    "city":"莆田",
                    "district":"仙游县",
                    "street":"度尾镇度峰北街"
                },
                "field_16":"36.5",
                "field_6":"cM1t",
                "field_13":"cM1t",
                "field_14":["2pG2"],
                "field_26":"无",
                # "field_20":{
                #     "province":"北京市",
                #     "city":"北京市",
                #     "district":"昌平区",
                #     "street":"外出地址"
                # },
                "field_17":"无"
            },
            "captchaData":'null',
            "weixinAccessToken":'null',
            "xFieldWeixinOpenid":'null',
            "weixinInfo":'null',
            "embedded":'false',
            "backgroundImage":'false',
            "formMargin":'false'
        }
    },
    "extensions":{
        "persistedQuery":{
            "version":'1',
            "sha256Hash":"4cd6a9aef2820b2c3215f6ddfa87093869461f76f3f2016738f4307268a7df98"
        }
    }
}
headers_urlencode = {
    "accept":"*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.72",
    "Content-Type": "application/json;charset=UTF-8",
    "DNT":"1",
    "Referer":"https://jinshuju.net/f/kxrHuH",
    "X-CSRF-TOKEN":"zjIi5bfz8NpIuumaQs8mFeCoylgbhmIfpDDmtn/yMHpuEuqW5YcjFbV9TQFp8RGwwePjw+SZI62S/M7jNfCZxw==",
    "Connection":"Keep-Alive",
    "Accept-Encoding": "gzip"
}
response = requests.post(url,data = json.dumps(Data),headers = headers_urlencode)
print(response)
response = json.loads(response.content)
print(response)