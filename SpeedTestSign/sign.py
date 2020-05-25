
import requests
import json
import time
import hashlib
import random
from stringToJson import StringToJSON
from urllib.parse import urlencode
# auth 199
auth = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImZlMDBkMDI5Mzk3MWE0ZDc3M2ExMWYwMWIxYTRjMWMyMmNhYjhlZDhiZDYyNzg1Y2RhYjYyY2M1NzM4NWEwNmExZDg0ZWY4ODE4YTM1MTY1In0.eyJhdWQiOiIyIiwianRpIjoiZmUwMGQwMjkzOTcxYTRkNzczYTExZjAxYjFhNGMxYzIyY2FiOGVkOGJkNjI3ODVjZGFiNjJjYzU3Mzg1YTA2YTFkODRlZjg4MThhMzUxNjUiLCJpYXQiOjE1OTAxMzI3NTEsIm5iZiI6MTU5MDEzMjc1MSwiZXhwIjoxNTkxNDI2ODA5LCJzdWIiOiIxMDY2NDQ3MSIsInNjb3BlcyI6W119.PcV2AC_9QcfWwWlGGI6enHIHfuC_pFZwaj9v391zhsFNevBnp-kV-jYgHrHCxHBJ26kWxQW_KMaWR3T0KVz6wvnQqsMryCKmZpDJbCnWymST7cbQwG4NH4YyikgXr1K_OIZ6bw80R60zdS1ND5LMJM5FdnK2TJvB6a3CFrtoyR8rOsJOuWzL3EmOszkl9WjkRbF1Dbvj0skdaTcNK9fY0aIMUssWpDow0OhkX4pUvq16qLkt_ScnPOtNS5QRmpqdRMo3-E792PUaFCRrT7e8rRHDg6GdYBVR8mSbVYJnIj9_eDicoMta28BTpW1-2Ca5bJJcwl6m-e03u8PiMfixG1jBUEWI8ODlbguiGYZiBEAmRlF57a8cuYYAYftOg5aUdxiWORmVMRq1AzH6d-CRrQe2fb5vFWpn9RMLKI9TBgNsXjjZ9cXJ5d-6pUrqNZMkW3-2I8c6bhjy8VxZNcgV37djWI9fVkKK-Abjt_IUOEbLgkwv7lGkin2Xr5tPEPhYViUrp8zs8g0reZM9Ztg3bwqflkwm2AT6peoXep8PraMANsPOSp9scM3O6-qpUWoqUAHJbJx0pP9MmAhN7v99FI1X0U-rHSEn4Iz0T3jPAWIPrUFTWwPoPv91IgvpfzZ1AWF9IIwlkMIAEvgt-0VIR6jnyG1ovUn8tHVA0BwRN_g"
# 185
auth2 = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjgzN2M4MGQyYWE0MGVhMDZjMWE0YTc4MTNiOGQzNjRhZmVmZDcwNjc2Nzg2NWYzZGU0Y2U1OWM5YzJmZTgyYzE3MGI4N2JhNzM1MjA1MDM2In0.eyJhdWQiOiIyIiwianRpIjoiODM3YzgwZDJhYTQwZWEwNmMxYTRhNzgxM2I4ZDM2NGFmZWZkNzA2NzY3ODY1ZjNkZTRjZTU5YzljMmZlODJjMTcwYjg3YmE3MzUyMDUwMzYiLCJpYXQiOjE1OTA0MTgyNzUsIm5iZiI6MTU5MDQxODI3NSwiZXhwIjoxNTkxNzExMjA2LCJzdWIiOiIxMDYyOTkwNyIsInNjb3BlcyI6W119.hdPEmJJ4hHUMjO7HwyTFh5XmOg0HRgH8uU9BamjJKUSZ7hjEgQRme83pn1KAGEsVIugKBU2huyuLpa_y1dimrwDta0JkwBICNORXSJ4Eovc4GwzXkfa-ftqYI6F-3ICMcsruQfjvMhRcwn1uvk5cR9BQ6R2XUSfBJFdUv3QWaumAmt0Jh8rFeaT2sA9M_JDsvn_zn2jWmPb1LT8OqtYTOh9YSxoC5lkR66D5hCir2CQUtjSBRYXrjHn76DfAi5gW5I0UkH7Xw8FXC1gBC6Ae84cfsCgFbr7LD9_0rl5VwbcdhJLMODVcdwyWDc6YZJ4EXy5JBGHT4WpqIlkQb1gGyEFiA__rJBEUHurD-CA0GcD8RqbW14PQ6DBpJh2mlrGhOUFKx58CCFYczUgxH7pJqsf-RW6rCtJ8DA7IBp-ikmNTNIxNOW6ynKeYE56NBkW6_G4ufiY8mNFxqURnS_Jdo5peJOU7p5akh1pY70B_n57BQQQQ3_dWjb61svfOVF69Bc8UHjaSg0Fc_MjMSYecLgzWVXjzfCUDtmWMv_YCeQTMrnLhv8tuJwHRv7FiI-tsfM2QyhZlF-kUUZ58WyuvVRwI0WVioxi2Umdx672D9zIlCOKzUJEffhLuUQ4KsF94ImahB_cxdgaY_LC4pLGoAh5rogS9IMAmCkMS0pz43h8'
urlDailySign = "https://forge.speedtest.cn/api/v2/signv2"
urlReplenish = "https://forge.speedtest.cn/api/v2/signv2/replenish"
urlSignRecords = "https://forge.speedtest.cn/api/v2/signv2/records"
urlDaily = "https://forge.speedtest.cn/api/v2/signv2/detail?timestamp="
urlVideo = "https://forge.speedtest.cn/api/v2/task/video-ad-finish"
# auth2 无效

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

def speedRecordByWeb():
    cookies1 = {
        'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d':'eyJpdiI6IkczTWVCWFViSDJncStLc0s0ZE5Ub0E9PSIsInZhbHVlIjoiZGhPaWE5cVZcL0Z0aWFJT3pnWWZMNGxIa29Xa2krUUcrQWxYcWhTTk0rQ2dNRURrdnljd1ZPVEhnYjdWWFhHN2ZSektVT2JrdTd6TFArb0ZmK3ZmbDIyakoxdG1LMHM4aUVHZXBDZittSVZzPSIsIm1hYyI6IjhmYWE4MjAzZjFmYmE3ZTYxOTU3NWI0MTU0NDUwZTc4NWY4OTU2OWExNDJhNjBkMGEwZTIwMjAyNjJlYzQ5MjgifQ',
        'laravel_token':'eyJpdiI6IktMM0dRZHpQRWRnaGMxNHg1RDNaREE9PSIsInZhbHVlIjoiVWl4Z2dvVVhJRnA2NWs0cmJFbjdqXC80OWgwb0hMb3ZzdzRPTzg0WG9vY2xMZWNoYnRkMitFWVwvaWpyTTJQektyOVdtZ09ZWjhvdlZ5TU9qQjQrOFVvMDhCdjd0eFpQNHllRnhpR2t6QnBJQTM5cUVDUUZoM1VXVFJqajh6Zm5kT0xsK0VMWnpmYW9UTFNLVEV3czNlT21MWnViUzVuU1RBNHI4UFNpQmJ5XC9jejQ3MWZrdCt0VEVDVWtLVjUzbGlsWEI4MFF4TGQ3MGxIR2VJSzUrajAwSlpxV1pqbjE3c1Q0WkF6cVI0UkF3dHZQM3B0TktPYWpIWmwrcE9LcFNmeTJzZTgyYWFoZUpPbzVDeGN1ZkZiaGc9PSIsIm1hYyI6ImMxYzlhNzVhYTA1Y2M5YzliZGZlYjkzODNhZGU0ZmJjOTA3YzNlN2M5Njk4OWI0N2VhYjRmODY1MTVkMjcyMWEifQ',
        'speedtest_session':'eyJpdiI6Ik1aeGhCN0JWQmFBUjRtUkJwUVdaTGc9PSIsInZhbHVlIjoiQXBhd1RyVmJKaHJDaFlGYllEVzJkRVhqUnRDektKR1drdVwvb2xINDJ6VndsVVFyTjNYdnNiaStVekFDY0VwVFAiLCJtYWMiOiIyOTI4Y2U1NTdlNzRiNDI2NTIwOWFiODdjNjhiMWE5YTEzNDExYTVhOTc1ZTIwNjczZGRkYTNmMTI3NWQyMjIzIn0'
    }
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
    response = requests.post("https://forge.speedtest.cn/api/v2/result/my-store",data=json.dumps(md5dataWebPage),headers = headers,cookies = cookies1)
    print(response)
    response = json.loads(response.content)
    print(response)

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
        print("auth1")
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
        print("auth2")
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
            print("video"+"range"+str(i))
            print("auth2")
            getFromvideo(auth2)
            print("auth1")
            getFromvideo(auth)
            time.sleep(40)
        except:
            print("video error")
    for i in range(3):
        try:
            print("web speed test")
            speedRecordByWeb()
        except:
            print("error")
        time.sleep(15)
        try:
            print("PC speed test")
            speedRecordByPC()
        except:
            ("error")
        time.sleep(5)
#getFromvideo(auth2)
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

