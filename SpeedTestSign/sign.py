
import requests
import json
import time
import hashlib
import random
from stringToJson import StringToJSON
from urllib.parse import urlencode
# auth 199
auth = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjBlOWI5NDhhNTEyNjI2ZDU1NGVlMTBhOTk0YjNiM2U4MzYwY2QyN2I2MDQxYWFlZGU2YTZjYmMwNmJlYmY5Y2VhNGEzZDdjMTUxNGQzOGQwIn0.eyJhdWQiOiIyIiwianRpIjoiMGU5Yjk0OGE1MTI2MjZkNTU0ZWUxMGE5OTRiM2IzZTgzNjBjZDI3YjYwNDFhYWVkZTZhNmNiYzA2YmViZjljZWE0YTNkN2MxNTE0ZDM4ZDAiLCJpYXQiOjE1OTE3NjgyNzMsIm5iZiI6MTU5MTc2ODI3MywiZXhwIjoxNjIzMzA0MjczLCJzdWIiOiIxMDY2NDQ3MSIsInNjb3BlcyI6W119.HSmzaRQdUgj0RuayHJWTAhasPGnObHJO68qQ7WMn0FuL4uGjgglf0pI-wvQB9J9CIuMjxe8-jxOpZSela88uPr3hZDM4qAsCpZlN5fy9G_8wblk7xJfw8JYZIoN0tu8-il-N-W-7M7Eu1yPpzA1JUCoQ1NNixrWdrlss-RExBMT7Ri9mJiUZKsTCKG-7_YIdH_3wzGHXb9a07zfvUemyoCRe_zEMskwDgBn8ksOaOs1IScPpqah_jhlpJvDpbUDSSHfOzb12cPwRtu_LJuKNWHLox8SRwtKsTj2NGOi-TOMNekDdqrfDaSb-zlDfZoeoG9bDREf-y6cjk_8zWlF8P8x-mLxHuVZlCStaq9kYCOVofgfGk39vobiCFW2990R-rhGTY-AOwoSzT7LbW6JcbaD573viM4osPcMrHxa0SI6i7OaPdFJcNR7iZl_q9fPQ4DdTiM59NQNVw9rtCU6reYDSyUjJ0sp7nuJhd2tJtFtEgNwKCxTmNH7JLcryHAEMJs3k9lg4BCMFxIoWYmqqcJkmHyPA5g9abmBx-AidciEg5PV1Gq6WM0ka98LZBE7O_1fWyiQEUsVC6lMixsVb68uQzXe_GBvyN98fwSESBO2ZbUQpxyQnlkhaCT5yVCw8I-MgCBEPlynXbP6LGwBVnnYcYHXkGScCPY1idAsNhA4"
# 185
auth2 = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjA3NTIwOTY2MzI2ZTAwMDE4ZGJlNjA5NDMyNjU3ZWQzMjQ2YjFhNWFhYjRjYTZjMmQ2YTc2NGRhYjczMmVlMzUyZDQ2YjJhZDc3Y2RmMmNjIn0.eyJhdWQiOiIyIiwianRpIjoiMDc1MjA5NjYzMjZlMDAwMThkYmU2MDk0MzI2NTdlZDMyNDZiMWE1YWFiNGNhNmMyZDZhNzY0ZGFiNzMyZWUzNTJkNDZiMmFkNzdjZGYyY2MiLCJpYXQiOjE1OTE3NjgwNDEsIm5iZiI6MTU5MTc2ODA0MSwiZXhwIjoxNjIzMzA0MDQxLCJzdWIiOiIxMDYyOTkwNyIsInNjb3BlcyI6W119.EZy2rZ-8-hZeoMlZE8uY7jY1nhvhH3X-nXgSW5nrWum8ZG0MhSI6v1DfsDB8_c2FPqgY2BnaLtk-yJuY_GlwADX2hp315484qzw19pgsKs-7oPzYDIN-0SFUMpMwpNu5m-mQmAODy-QSUdSVXnb8UkZSS7zf8SMy7YSESqIkuZ42gvKPMjxvgom6hTCUyxuWHIdgRfhkkzb2PqExJzgJREcW4bgHkAbh4J_NbPzxGhyWLLCptNQZcrimv2axZVYjh80xHfhsIjAEKp7D-BnzCLycFoNe0qCk-M7v59xyKxnESeNsiSksVAvHWZit8MNIR8YhaYcSZWmDjIFul8LuCTyushK7_Sq3QJzC7w_mbEY4_otsjLzjhtLckgDoR4rCPLH1h_4VN8nvoWKySh0ot66oO9BmW3b3eHO5dpPxwu3GXbKpGEFBa7xirkb_NBHM8MtGQOTLM-wszMlyvLRmsRd455Vvka7z4ji9rdwFBjyeJF8PhqM0Ysjo4G5uH3DXTaJW8FVuetNMFprryYqoPsygQ-dmKOD824QQG74oGi2B1tfTOtI_xf5Nx-PgW3qDYyRsvF5eKEI09Fc0zpz4bC3YnoYI4aJ1LNRVILxA47z0zxQshVnjHU58TmalPIzFjXfP52xn9D9wGwSjWEgKTWT5eqMTp8hElRPNP30hGuA'
urlDailySign = "https://forge.speedtest.cn/api/v2/signv2"
urlReplenish = "https://forge.speedtest.cn/api/v2/signv2/replenish"
urlSignRecords = "https://forge.speedtest.cn/api/v2/signv2/records"
urlDaily = "https://forge.speedtest.cn/api/v2/signv2/detail?timestamp="
urlVideo = "https://forge.speedtest.cn/api/v2/task/video-ad-finish"

def replenish(date,auth):
    Data = {
    "date":'{}'.format(date)
    }
    headers_urlencode = {
    "Accept-Language": "zh-CN,zh;q=0.8",
    "User-Agent": "speedtest/5.2.3",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host":"forge.speedtest.cn",
    "Connection":"Keep-Alive",
    "Accept-Encoding": "gzip",
    'Authorization': "Bearer {}".format(auth)
    }
    response = requests.post(urlReplenish,data = (urlencode(Data)),headers = headers_urlencode)
    print(response)
    response = json.loads(response.content)
    print(response)

def getRecords(auth):
    headers_json = {
    "Accept-Language": "zh-CN,zh;q=0.8",
    "User-Agent": "speedtest/5.2.3",
    "Content-Type": "application/json",
    "Host":"forge.speedtest.cn",
    "Connection":"Keep-Alive",
    "Accept-Encoding": "gzip",
    'Authorization': "Bearer {}".format(auth)
    }
    response = requests.get(urlSignRecords,headers = headers_json)
    print(response)
    response = json.loads(response.content)
    print(response['data'])
def dailyCheck(auth):
    headers_json = {
    "Accept-Language": "zh-CN,zh;q=0.8",
    "User-Agent": "speedtest/5.2.3",
    "Content-Type": "application/json",
    "Host":"forge.speedtest.cn",
    "Connection":"Keep-Alive",
    "Accept-Encoding": "gzip",
    'Authorization': "Bearer {}".format(auth)
    }
    response = requests.get(urlDaily+str(int(time.time())),headers = headers_json)
    print(response)
    response = json.loads(response.content)
    print(response)
def dailySign(auth):
    headers_json = {
    "Accept-Language": "zh-CN,zh;q=0.8",
    "User-Agent": "speedtest/5.2.3",
    "Content-Type": "application/json",
    "Host":"forge.speedtest.cn",
    "Connection":"Keep-Alive",
    "Accept-Encoding": "gzip",
    'Authorization': "Bearer {}".format(auth)
    }

    response = requests.post(urlDailySign,headers = headers_json)
    print(response)
    response = json.loads(response.content)
    print(response)
def md5sign(data):
    m = hashlib.md5()
    m.update(data.encode("utf8"))
    return m.hexdigest()
def speedRecordByPC():
    auth2 = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjFmZGRmYzkxZmI0OTA4MWY4ODAzOTM0NGYzNDJkNTAzNTE0ZjUxMGI1YmQyZWI1NDc4MzU2ZDQyZmQ4OTg5Y2I5M2UyYTdjOWZkZjE2MGNjIn0.eyJhdWQiOiIyIiwianRpIjoiMWZkZGZjOTFmYjQ5MDgxZjg4MDM5MzQ0ZjM0MmQ1MDM1MTRmNTEwYjViZDJlYjU0NzgzNTZkNDJmZDg5ODljYjkzZTJhN2M5ZmRmMTYwY2MiLCJpYXQiOjE1OTA0MTkyNDIsIm5iZiI6MTU5MDQxOTI0MiwiZXhwIjoxNTkxNzE0ODAyLCJzdWIiOiIxMDYyOTkwNyIsInNjb3BlcyI6W119.d8XPDrvAS0WwVr9DAkKcJyMO6ggs8mvXEjTUvtsJALFnu9imFgtmYKifrT-EXrZrpGPwBfl23-3gjGFZlB65z2yIlcjJLJJBjvw-DySio8RoHH-8T98rFnryxRLQMf0V3D2Jtz9drgDnM1dqi8XdkzJ4hAmV9Sua0vzCf7kN6ffAMGPt4AKM-0Dlgt9K3HY5tFoIfopnG9u2b5EehGyfoIkL1-Gk_PKQNONmQUkcKMJVE7Y8l9BLIhcpYtMmo6TpNptJcTFb8QS49RsrrQhn5F43EMMQHBzgCGlAvhwRw7n4dlNoPENakRS8UI1vNsKRGemrPyCCgdr4KB_d8-xqkRwNXb6vGAjnuYGQN8dFlYmDvDont65R7lSX5rstqUKQynuzBW54NxN0A5C5kWBWLHe83LIKDTZoXVann5Z0G65LdhZY6HUXKEsMzi_ZLWUwRv-7caLPNcw8ajXllvZBswqBBOkRjuGGwDiIpaTHRwTjs85Tb0AW6_JOkss2WYuoigeks5Q718OgRevJHfeK7pSscXCoeZtzkdqfor2rmyBS9V5R7xQl6tlo6skVhRKCJTZDd2QmDUgOjJxKCQaLEKDH367fn5UwEyHCvn6J3jwiNBAeT0yHQaPjOXDg2KYmH2e7FIumsMoszFgXtrTHwVHdEq63K2Fayss1lRUkxcY'
    cookies = {
        'UM_distinctid':'170947077992af-066a23f83b6287--22c1a568-144000-1709470779a12d',
        'Hm_lvt_8decfd249e4c816635a72c825e27da1a':'1588744064,1588835592,1589520457,1590293811',
        '_ga':'GA1.2.457732882.1583038364',
        '_gid':'GA1.2.339350835.1588835592',
        'Hm_lpvt_8decfd249e4c816635a72c825e27da1a':'1590293867',
    }
    headers_json = {
    "Accept-Language": "zh-CN,zh;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 Edg/81.0.416.68",
    "Content-Type": "application/json",
    "Host":"forge.speedtest.cn",
    "Connection":"Keep-Alive",
    "Accept-Encoding": "gzip",
    'Authorization': "Bearer {}".format(auth2),
    "Authority":'forge.speedtest.cn'
    }
    md5dataWebPage = {
        "nodes":'[\"407845\",\"407845\",\"104\",\"407995\",\"100\"]',
        "download":str(random.uniform(20.2,80.6)),
        "upload":str(random.uniform(2.00,10.00)),
        "ping": str(random.uniform(1,50)),
        "loss":str(random.uniform(0,10.5)),
        "jitter":str(random.uniform(0,2)),
        'extra': 'undefined',
        "lon":'118.70214',
        "lat":'25.35072',
        "timestamp":str(int(time.time())),
        "app_id":"af5eseddhgt",
        "source":"PC",
        "network":'1',
        'buid':'1579445026169',
        "download_chart":str(random.shuffle([-2,-2,-2,22.6,20.91,26.13,26.13,26.99,27.86,100.39,29.65,29.04,30.63,34.46,35.48,35.89,36.56,50.94,36.66,35.79,36.66,37.68,39.36,38.76,38.45,39.57,38.81,38.81,38.65,40.03,39.88,39.73,39.88,39.78,39.27,39.78,40.09,40.55,40.49,40.9,40.75,41.21,40.7,41.06,41.06,40.9,40.9,40.75,41.06,41.47,41.26,41.26,41.47,41.52,41.88,41.88,41.98,41.98,41.93,42.18,42.03,42.23,42.39,42.44,42.44,42.44,42.44,42.44])),
        "upload_chart":str(random.shuffle([-2,42.44,42.44,42.44,42.44,42.10,42.44,42.44,202.44,42.44,42.64,42.44,42.44,42.44,42.24,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44])),
        "buid":"1579445026169"}
    s = ""
    for item in md5dataWebPage:
        s += md5dataWebPage[item] + '-'
        #print(s)
        #print(len(s))
    s = s[0:len(s)-1] + '94de8b90ed5673e7e8e0da9d3d0d24df'
    #s_get = '[\"407845\",\"407845\",\"104\",\"407995\",\"100\"]-8.69-4.42-26.26-0-1.00-undefined-118.70214-25.35072-1588825127-cce084120d4-www-1-[-2,-2,-2,22.6,20.91,26.13,26.13,26.99,27.86,31.39,29.65,29.04,30.63,34.46,35.48,35.89,36.66,37.94,36.66,35.79,36.66,37.68,39.16,38.76,38.45,39.57,38.81,38.81,38.65,40.03,39.88,39.73,39.88,39.78,39.27,39.78,40.09,40.55,40.49,40.9,40.75,41.21,40.7,41.06,41.06,40.9,40.9,40.75,41.06,41.47,41.26,41.26,41.47,41.52,41.88,41.88,41.98,41.98,41.93,42.18,42.03,42.23,42.39,42.44,42.44,42.44,42.44,42.44]-[-2,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44]-157944502616994de8b90ed5673e7e8e0da9d3d0d24df'
    #s_fun = "[\"407845\",\"407845\",\"104\",\"407995\",\"100\"]-8.69-4.42-26.26-0-1.00-undefined-118.70214-25.35072-1588825127-cce084120d4-www-1-[-2,-2,-2,22.6,20.91,26.13,26.13,26.99,27.86,31.39,29.65,29.04,30.63,34.46,35.48,35.89,36.66,37.94,36.66,35.79,36.66,37.68,39.16,38.76,38.45,39.57,38.81,38.81,38.65,40.03,39.88,39.73,39.88,39.78,39.27,39.78,40.09,40.55,40.49,40.9,40.75,41.21,40.7,41.06,41.06,40.9,40.9,40.75,41.06,41.47,41.26,41.26,41.47,41.52,41.88,41.88,41.98,41.98,41.93,42.18,42.03,42.23,42.39,42.44,42.44,42.44,42.44,42.44]-[-2,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44]-157944502616994de8b90ed5673e7e8e0da9d3d0d24df"
    #print(s)
    #print(md5sign(s))
    md5dataWebPage.update({'sign':s})
    response = requests.post("https://forge.speedtest.cn/api/v2/result/my-store",data=json.dumps(md5dataWebPage),headers = headers_json,cookies = cookies)
    print(response)
    response = json.loads(response.content)
    print(response)
#speedRecordByWeb()
cookies1 = {
        'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d':'eyJpdiI6IjNDR1VYVHdTM2FhY3B6SzZ6YlJoWnc9PSIsInZhbHVlIjoiNmJqR0UrVnEyTmZZNm90U3FKckJNMmRIODZpS1hYMEVPZTRLQXFGbFwvdmg5RER5ekdhVHJRdVNUcTMrbUk1WHlsZHBtbllvcEU5MVwvbDFWTWhUalM3WVJhZFZadldaSDJLUGJucm0yQkFadz0iLCJtYWMiOiI0MTA1ZmY0ZWI4NGQ0YTQ2NmQzNmRiMDAzYWNlYzMxMDczZWU5OTI3NzQyNGJmY2U0Mzg0NjgyOTE3ODU2NWZjIn0%3D',
        'laravel_token':'eyJpdiI6IlhPQW14a0ZWNmVId2xFRkpxUm9EV2c9PSIsInZhbHVlIjoiUjFSa29ISXc2NHJXdjJKViswZ0l3VGpYbUllUDJ2Q3RcL096SWo4RXdkbVBqRWhMSis1VUZvRlNDeGtmbGhBajJpZEZYZ1dzY0VJQWRTSGxHaW9VcVZVV29wY1NcL1BmVFdSZE1qbkNXeEpZOTNxd21oRkV5d2xlcDhwTzRDQWRMVU1MOGNURXFhczRvNks5WVFWUEdzMnFpNXJwakVxbkcyK1NiMVpKQk9wZVc0bEgraFRzdnpaWDRcLzhHQWFqUk5kNGdcL0dHSUhxRTZwTHRuTUJ0THlXMVdMRWRDVFd2MzZ5MEkyM2pTM2lHZ2hHNEdKc3FWMnpRc1wvYjllREgzVWlmQVJZbERLdzh2YXBjeU5XQWdySGVPZz09IiwibWFjIjoiMWU3NmFiZjliMGQ3OGI2ZWVjNmYyNjFkZTRkZmQ4MWFmMjE4NzI0NGZmZGNiMDNiOWFjMTQzNTU3NWUwZDEyOSJ9',
        'speedtest_session':'eyJpdiI6IkU5NkRhKzdlRGFtcWNhVXFzSE9XMGc9PSIsInZhbHVlIjoiZVMraVVoQ0d2WmR2OUhuaktOR3ZkUGphT01CM2dlQXdCOExcL3VLTGJMTG5IQVBiVXBjeFhFYnhtXC9rSmhIVmhNIiwibWFjIjoiNzhlMmRlYjU0YzNkNzZkZGM0NzkwYTRlNTQ1MGU4M2EyY2NmYTUwNjU2YjYwOGE2MmY3ZThhOWQ1MDM0MjY0YSJ9'
    }#185
cookies2 = {
    'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d':'eyJpdiI6IlJuUVVHd1wvOGF3WDE1Tk03RFJRVVVnPT0iLCJ2YWx1ZSI6Ik9JaG9TQno3eUJ0SUpDclpyXC9mWVdKblwvZUVQc3ZzeUdcL3gzOU9PYmdmejlybUIrb1F4c1AxTTVoMVlCcXZEQzBCMzRGbjB1Y1NxVEhwQkVzNUtxdjVyM0dWQk9YaHF3MTZTREpOdlk3TERNPSIsIm1hYyI6IjJiODRjODNkMTFjMDdkNzU0M2MwYTBhNWI4MzhlODE0YmM0ODYxOTg3NGE0YTVhM2QwYjM4ODgwNWM1ODE2ZWMifQ%3D%3D',
    'laravel_token':'eyJpdiI6IlkyMXhPeUZTSUJGdWhQdEdnNmVcL1BBPT0iLCJ2YWx1ZSI6IlwvekFudm1OOHBjRVhLbmVXRmdNRnFwQzUxOFwvQlF1WjFOK2VYWmhQZE92YW54N3oxc3ZjM2s0RWZ4S2pzRlUzODVcL0dLSVRpeENNTjFsV044NnRURldxNEd1YzhzbDRlK0lrREprWHM2YmdUN0FicHhkRUo2SjdNYU1wSms4bjRBaXhYQng0SXlLc0xBZFwvd01uaFFZZjJjaElZSHVoV0dWd0JSRzNmaHJsTVBOT2wzb1VqK3RIU2pQN0Y2ekhJQkF1dUc3bHVMcHJKXC9RUDdJck9qcFFRVEF6d3l1RW14UUJGTWxFdjg4NFhyOXNsQ0pVZmFZMjBxbVBnRTkwXC8wZlYwN0ZRZTQ1dmppTVdXZVVCMHFmRWpnPT0iLCJtYWMiOiJlMWM5NDg3YzBmOWMyM2EyZGNmYTgwNGU3OTI5ZGRiZTg0YTkyOGViNjdhYWZmNjdkNDlkNTAxNDgzMTI1OTZkIn0%3D',
    'speedtest_session':'eyJpdiI6IjFNV2x2XC9oSENEcllrRXFCN1pGeFpRPT0iLCJ2YWx1ZSI6InpodWZIUlVUeG1ueUlXZFo4M250bFp1eHljYkg5VUk2akJ4QlwvanA0UlpqYk5vZVwvZ2hhUUhLSVVcL1pFNDFGVk0iLCJtYWMiOiIyMTNmODVlZjYyZjUxZTYxMTA4ZTQ2N2U0YWU1MWY2ZDViMWU5NmZlY2VjOTQ0MzQxYWI5M2FhZDAzMGIzNzQ4In0%3D'
}#199
def speedRecordByWeb(cookies):
    
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding':'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-length': '1095',
    'content-type': 'application/json;charset=UTF-8',
    'dnt': '1',
    'origin':'https://www.speedtest.cn',
    'referer': 'https://www.speedtest.cn/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 Edg/81.0.416.68',
    'x-requested-with': 'XMLHttpRequest',
    }
    md5dataWebPage = {
    "nodes":'[\"407845\",\"104\",\"407995\",\"100\"]',
    "download":str(random.uniform(20.2,80.6)),
    "upload":str(random.uniform(2.00,10.00)),
    "ping": str(random.uniform(1,50)),
    "loss":str(random.uniform(0,10.5)),
    "jitter":str(random.uniform(0,2)),
    'extra': 'undefined',
    "lon":'118.70214',
    "lat":'25.35072',
    "timestamp":str(int(time.time())),
    "app_id":"cce084120d4",
    "source":"www",
    "network":'1',
    "download_chart":str(random.shuffle([-2,-2,-2,22.20,6,.91,26.113,216.131,261.991,217.816,1100.391,219.651,219.14,310.613,34.416,35.418,315.819,316.516,510.94,36.66,35.79,36.66,37.68,39.36,38.76,38.45,39.57,38.81,38.81,38.65,40.03,39.88,39.73,39.88,39.78,39.27,39.78,40.09,40.55,40.49,40.9,40.75,41.21,40.7,41.06,41.06,40.9,40.9,40.75,41.06,41.47,41.26,41.26,41.47,41.52,41.88,41.88,41.98,41.98,41.93,42.18,42.03,42.23,42.39,42.44,42.44,42.44,42.44,42.44])),
    "upload_chart":str(random.shuffle([-2,42.44,42.44,42.44,42.44,42.10,42.44,42.44,202.44,42.44,42.64,42.44,42.44,42.44,42.24,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44])),
    "buid":"1579445026169"
    }
    s = ""
    for item in md5dataWebPage:
        s += md5dataWebPage[item] + '-'
        #print(s)
        #print(len(s))
    s = s[0:len(s)-1] + '94de8b90ed5673e7e8e0da9d3d0d24df'
    #print(s)
    #print(md5sign(s))
    md5dataWebPage.update({'sign':s})
    response = requests.post("https://forge.speedtest.cn/api/v2/result/my-store",data=json.dumps(md5dataWebPage),headers = headers,cookies = cookies)
    print(response)
    response = json.loads(response.content)
    #print(response)

def speedUpByPC():
    cookiesRaw = "UM_distinctid=170947077992af-066a23f83b6287--22c1a568-144000-1709470779a12d; _ga=GA1.2.457732882.1583038364; Hm_lvt_8decfd249e4c816635a72c825e27da1a=1588741864,1588741982,1588744064,1588835592; Hm_lpvt_8decfd249e4c816635a72c825e27da1a=1588835592"
    mySTJ = StringToJSON(cookiesRaw)
    headersSpeedUpAble = {
        'Host': 'tisu-api.speedtest.cn',
        'Connection': 'keep-alive',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ????/1.3.5 Chrome/73.0.3683.121 Electron/5.0.13 Safari/537.36',
        'Content-Type': 'application/json;charset=utf-8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN'
    }
    addrAble = "https://tisu-api.speedtest.cn/api/v2/speedup/trial-query?type=2&source=web&buid=1579445026169"
    addrUp = "https://tisu-api.speedtest.cn/api/v2/speedup/trial-open?type=2&source=pc-tisu-down&trial=1&buid=1579445026169"
    try:
        response = requests.get(addrAble,headers = headersSpeedUpAble,cookies = mySTJ.extractToJson())
        print(response)
        response = json.loads(response.content)
        print(response)
        if(response["data"]["trialData"]["trial_t"] == 0):
            response = requests.get(addrUp,headers = headersSpeedUpAble,cookies = mySTJ.extractToJson())
            print(response)
            response = json.loads(response.content)
            print(response)
        else:
            print("不可提速")
    except:
        print("error")

def getFromvideo(auth):
    headers_json = {
    "Accept-Language": "zh-CN,zh;q=0.8",
    "User-Agent": "speedtest/5.2.3",
    "Content-Type": "application/json",
    "Host":"forge.speedtest.cn",
    "Connection":"Keep-Alive",
    "Accept-Encoding": "gzip",
    'Authorization': "Bearer {}".format(auth)
    }

    response = requests.get(urlVideo,headers = headers_json)
    print(response)
    response = json.loads(response.content)
    print(response)


def suit():    
    #speedUpByPC()
    try:
        print("auth1-------------------")
        print("getRecode imformations")
        getRecords(auth)
    except:
        print("error")
    time.sleep(1)
    try:
        print("sign")
        dailySign(auth)
    except:
        print("error")
    time.sleep(1)
    try:
        print("check")
        dailyCheck(auth)
    except:
        print("error")
    time.sleep(1)
    try:
        print("auth2-----------------------")
        print("recode imformaitons")
        getRecords(auth2)
    except:
        print("error")
    time.sleep(1)
    try:
        print("sign")
        dailySign(auth2)
    except:
        print("error")
    time.sleep(1)
    try:
        print("check")
        dailyCheck(auth2)
    except:
        print("error")
    time.sleep(1)
    for i in range(3):
        try:
            print("video "+"range"+str(i)+'---------------')
            print("auth2 185")
            getFromvideo(auth2)
            print("auth1 199")
            getFromvideo(auth)
            time.sleep(40)
        except:
            print("video error")
    for i in range(3):
        try:
            print("web speed test By web---------------")
            print("185")
            speedRecordByWeb(cookies1)
        except:
            print("error")
        time.sleep(15)
        try:
            print("PC speed test By Web---------------------")
            print("199")
            speedRecordByWeb(cookies2)
        except:
            ("error")
        time.sleep(5)

suit()


















































"""
var l = {
    nodes: JSON.stringify(this.nodeId),
    download: e.dlStatus,
    upload: e.ulStatus,
    ping: "-" === e.pingStatus ? 0 : e.pingStatus,
    loss: "-" === e.lossStatus ? 0 : e.lossStatus,
    jitter: "-" === e.jitterStatus ? 0 : e.jitterStatus,
    extra: e.telemetryExtra,
    lon: this.lon,
    lat: this.lat,
    timestamp: parseInt((new Date).getTime() / 1e3),
    app_id: "cce084120d4",
    source: "www",
    network: 1,
    download_chart: JSON.stringify(n),
    upload_chart: JSON.stringify(a),
    buid: this.$root.buid
};
this.$root.resultData = l,
this.$root.download_chart = n,
this.$root.upload_chart = a,
this.hideAndShow(),
this.$root.testComplate = !0;
var s = "";
for (var c in l)
    s += l[c] + "-";
s = hex_md5(s.slice(0, s.length - 1) + "94de8b90ed5673e7e8e0da9d3d0d24df"),
l = g({}, l, {
    sign: s
}),
"""

"""
dataApp={
    'nodes':'[2006,2034,1292,407845]',
    'download':'0.00',
    'upload':'4.53',
    'ping':'13',
    'jitter':'4',
    'loss':'0.0',
    'network':'2',
    'os':'Android',
    'source':'android',
    'log':"",
    'extra':"",
    'buid':'1579445026169',
    'lon':'121.492479',
    'lat':'31.247221',
    'wifi_name':'jnnlehv055',
    'wifi_dbm':'-55',
    'device_brand':'HUAWEI',
    'device_model':'DUK-AL20',
    'system_language':'zh',
    'system_version':'5.1.1',
    'system_ui_version':'',
    'IMEI':'865143751762578',
    'app_id':'cf70b3f0b852',
    'timestamp':'1588832631'
}
sign=80949d259a0374322a98218772778735
"""
""" dataApp={
    'nodes':'[2006,2034,1292,407845]',
    'download':'0.00',
    'upload':'4.53',
    'ping':'13',
    'jitter':'4',
    'loss':'0.0',
    'network':'2',
    'os':'Android',
    'source':'android',
    'log':"None",
    'extra':"None",
    'buid':'1579445026169',
    'lon':'121.492479',
    'lat':'31.247221',
    'wifi_name':'jnnlehv055',
    'wifi_dbm':'-55',
    'device_brand':'HUAWEI',
    'device_model':'DUK-AL20',
    'system_language':'zh',
    'system_version':'5.1.1',
    'system_ui_version':'None',
    'IMEI':'865143751762578',
    'app_id':'cf70b3f0b852',
    'timestamp':'1588832631'
}
s = ""
for item in dataApp:
    s += dataApp[item] + '-'
    print(s)
    print(len(s))
s = s[0:len(s)-1] + '94de8b90ed5673e7e8e0da9d3d0d24df'
#s_get = '[\"407845\",\"407845\",\"104\",\"407995\",\"100\"]-8.69-4.42-26.26-0-1.00-undefined-118.70214-25.35072-1588825127-cce084120d4-www-1-[-2,-2,-2,22.6,20.91,26.13,26.13,26.99,27.86,31.39,29.65,29.04,30.63,34.46,35.48,35.89,36.66,37.94,36.66,35.79,36.66,37.68,39.16,38.76,38.45,39.57,38.81,38.81,38.65,40.03,39.88,39.73,39.88,39.78,39.27,39.78,40.09,40.55,40.49,40.9,40.75,41.21,40.7,41.06,41.06,40.9,40.9,40.75,41.06,41.47,41.26,41.26,41.47,41.52,41.88,41.88,41.98,41.98,41.93,42.18,42.03,42.23,42.39,42.44,42.44,42.44,42.44,42.44]-[-2,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44]-157944502616994de8b90ed5673e7e8e0da9d3d0d24df'
#s_fun = "[\"407845\",\"407845\",\"104\",\"407995\",\"100\"]-8.69-4.42-26.26-0-1.00-undefined-118.70214-25.35072-1588825127-cce084120d4-www-1-[-2,-2,-2,22.6,20.91,26.13,26.13,26.99,27.86,31.39,29.65,29.04,30.63,34.46,35.48,35.89,36.66,37.94,36.66,35.79,36.66,37.68,39.16,38.76,38.45,39.57,38.81,38.81,38.65,40.03,39.88,39.73,39.88,39.78,39.27,39.78,40.09,40.55,40.49,40.9,40.75,41.21,40.7,41.06,41.06,40.9,40.9,40.75,41.06,41.47,41.26,41.26,41.47,41.52,41.88,41.88,41.98,41.98,41.93,42.18,42.03,42.23,42.39,42.44,42.44,42.44,42.44,42.44]-[-2,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44,42.44]-157944502616994de8b90ed5673e7e8e0da9d3d0d24df"
print(s)
#print(s_get)
print(md5sign(s))
#print(md5sign(s_get))
#print(md5sign(s_fun)) """

