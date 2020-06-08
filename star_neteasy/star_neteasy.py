#encoding: utf-8
"""
待更新：1、收取黑钻数目显示  OK
               2、收取黑钻接口更新  OK
               3、cheak in 功能  OK
               POST https://star.8.163.com/api/starUser/checkIn HTTP/1.1
               2018/7/24
               1B5CDE031A2F13B1C17880AE0453AE010EF74AFE8933CE577ED90B8403502DFB335C5DD459366FEBD55A5896719ADF93575C6D7C104F785543F97F45A5ED6E16304490B48E99F3C5F38FEEFC72F0BCC13D18D482854E7EB9C868067ACE96D709537BE155383DC6C248A6D6E05E520D8ACE4562A8D38AFA5BD94EBB5CBD31544CD7483EE9BB436BFC20202185CB98B9A46105492FFF5F2E4E0D6EABCB1B4015AF0B99BC69CBFFB69BE00CB522623D144E5FA613A752C3CE7A5B981A225AA2BCD8A2753088EB5D87F61C6A9E865FF4161B8F66CF44B2DD6F37C0DF507C33C02E7CEA9C0A048902349E820B8795513A12733C90CB0573C51CCF63B2864D97D207B06B3F1CF6BACC050EA43C7B9D07DF288877D42415AA400EE1B0DDD249E81B3B13ECF39E37BD91AEC58034672A36DC0B256C997E67CE2E4C5E7256D5C9B731C1142B16A1A066830AF69B85A674A2D0D56BF9BCAACEB98294D46CC83C24FF2AD5F30AA138BFD8E5266A47B8552AF6B800D416C3DE2B3B87844B65A92A00D28F60A3F2346C6E2B92344C2B08930D42CD669242894F50DFB6B536EAF85CD25D9B2D091C6207F163CD5249A36008547F9F4F3870DA6398B346DFEAB3AA4B696CE7A7CDE209828B975F75ADF1D57267972D55624256005887F8ADB6D97F8D26760F8E4D330AC43FE2F92C526139EDB951C33BF760A9B16B719C063F7F84EE158AC10E779B180C5690861DB201C71CF8BF99F5E4328BB689F56525D973A26567FE2C428A56747EC52672529B8EB1AA042CE1278DDB635DD487F61FBCA80FD0F2B16A64AE7BA4D86B500AED6DE440040F0BF0A7646AA3B102FBE7296AB0DB9EA5C46AD12B
               1B5CDE031A2F13B1C17880AE0453AE010EF74AFE8933CE577ED90B8403502DFB335C5DD459366FEBD55A5896719ADF93575C6D7C104F785543F97F45A5ED6E16304490B48E99F3C5F38FEEFC72F0BCC13D18D482854E7EB9C868067ACE96D709537BE155383DC6C248A6D6E05E520D8ACE4562A8D38AFA5BD94EBB5CBD31544CD7483EE9BB436BFC20202185CB98B9A46105492FFF5F2E4E0D6EABCB1B4015AF0B99BC69CBFFB69BE00CB522623D144E5FA613A752C3CE7A5B981A225AA2BCD8A2753088EB5D87F61C6A9E865FF4161B2DFCAF63717EFED9E987CC94A2E0AAFCDA21B25ED28BEC83CE47386B0933F36477110A8C95EDD7D06722EC3323E0E612E6ABE4D02A5A97B176C2CBAC393C75CE90BF93DED7359814E7F7771F57DD6360ECF39E37BD91AEC58034672A36DC0B256C997E67CE2E4C5E7256D5C9B731C1142B16A1A066830AF69B85A674A2D0D56BF9BCAACEB98294D46CC83C24FF2AD5F30AA138BFD8E5266A47B8552AF6B800D416C3DE2B3B87844B65A92A00D28F60A3F2346C6E2B92344C2B08930D42CD669242894F50DFB6B536EAF85CD25D9B2D09F0AD3DAF54FEF3B39F21A1C189796454B8D91E16CED5762DFDF5AAF4FE61EB0CF5A08D947DA5E3163A5879D46E8BA33E4256005887F8ADB6D97F8D26760F8E4D330AC43FE2F92C526139EDB951C33BF760A9B16B719C063F7F84EE158AC10E773C0A58DF7E405CFE8BB8C0B202001A9E56AE65500D798AB381302B962E06D60956747EC52672529B8EB1AA042CE1278D44CF2A644A10C273686E81463EDE761D0AC5354A4D83B47C669B0643EEEA22F76AA3B102FBE7296AB0DB9EA5C46AD12B
"""
import requests
import json
import gzip
import time
import random
from urllib.parse import urlencode
from stringToJson import StringToJSON
print("hello world")

headers_1 = {
    'Host': 'star.8.163.com',

    'Accept': 'application/json, text/plain, */*',
    'Origin': 'https://star.8.163.com',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; vivo X6S A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 hybrid/1.0.0 star_client_info_begin {hybridVersion: "1.0.0",clientVersion: "1.2.1",accountId: "523b36bd1ab731a7ced0562c8bf69475440dbe76ebba9137b468d9dac99dd927",channel: "e01170002"}star_client_info_end',
    'Referer': 'https://star.8.163.com/m',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,en-US;q=0.9'
    }
    
headers = {
    'Host': 'star.8.163.com',
    'Accept': 'application/json, text/plain, */*',
    'Origin': 'https://star.8.163.com',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; vivo X6S A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 hybrid/1.0.0 star_client_info_begin {hybridVersion: "1.0.0",clientVersion: "1.2.1",accountId: "523b36bd1ab731a7ced0562c8bf69475440dbe76ebba9137b468d9dac99dd927",channel: "e01170002"}star_client_info_end',
    'Content-Type': 'application/json;charset=UTF-8',
    'Referer': 'https://star.8.163.com/m',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,en-US;q=0.9',
    }



cookies_seven= {
    'STAREIG':'3a63235925c59f329af9ecd73af51d3445a3bc58',
	'NTES_YD_SESS':'rF7zjd4mxinQgCvemLNuIweSkZW8DP9DlV4jXUAaC4UsZnqeiEjDRKqhwA.HPGlocUHs1LQXr5NcYXsiR.FS12f4Rf0gHZ.8Al5vVgxkyTOofNGnQBjk8XPGBYl_Uw5aP13NQZMM.nbPioMf8_ENs1thp4VIkn_M1vc0QkJIvQalEJrQO1PZ5O7YqbFihpmntQwaWvba7.FmrnUjajq4gtL6p56kad1XQ6TSXsO3KK30S',
	'STAR_YD_SESS':'rF7zjd4mxinQgCvemLNuIweSkZW8DP9DlV4jXUAaC4UsZnqeiEjDRKqhwA.HPGlocUHs1LQXr5NcYXsiR.FS12f4Rf0gHZ.8Al5vVgxkyTOofNGnQBjk8XPGBYl_Uw5aP13NQZMM.nbPioMf8_ENs1thp4VIkn_M1vc0QkJIvQalEJrQO1PZ5O7YqbFihpmntQwaWvba7.FmrnUjajq4gtL6p56kad1XQ6TSXsO3KK30S',
    'UM_distinctid':'171f231033b73-08907fd88315a2-29703570-9c4c8-171f231033c60'

}

cookies_S = {
    'STAREIG':'9b9c05018236db3d91774add61262180e99d864d',
    '_ga':'GA1.2.114177454.1532169307', 

}
cookies_f = {
    'STAREIG':'8862532468d0eebd8b952fc587156c05a2a0f42a',
	'_ga':'GA1.2.1868902040.1523759609',
    '_ntes_nnid':'ef936f68e3339b374326875c159fc30a,1523843040503',
	'_ntes_nuid':'ef936f68e3339b374326875c159fc30a',
	'ajs_user_id':'null',
	'ajs_group_id':'null',
	'NTES_YD_SESS':'0SSOd7wg_BAriSbi_6NdygB_VBpXbDO2mdNlrHu0ZlciO1zGOBYERDz4wuNlE3u44Poi5s_rU9HiZS8QQCgLhgLJqSGgK4yGRwe8qIezz9DqqavrFZNjHt9vZB2dpzT19GbaFW..wrY9Jt_ZbQpbFeqVLc8Ajrd.GbuV4biuK.Wz_PiT6KTZ19VHzmHghCPUS762FqAn8IW8UhtPw14qNIMnvpXShspzNIgrmLL_Sqf2k',
	'STAR_YD_SESS':'0SSOd7wg_BAriSbi_6NdygB_VBpXbDO2mdNlrHu0ZlciO1zGOBYERDz4wuNlE3u44Poi5s_rU9HiZS8QQCgLhgLJqSGgK4yGRwe8qIezz9DqqavrFZNjHt9vZB2dpzT19GbaFW..wrY9Jt_ZbQpbFeqVLc8Ajrd.GbuV4biuK.Wz_PiT6KTZ19VHzmHghCPUS762FqAn8IW8UhtPw14qNIMnvpXShspzNIgrmLL_Sqf2k',
	'mail_psc_fingerprint':'4e3492224e46a5e89597cb96a1bf0565',
	'mp_MA-9E66-C87EFACB60BC_hubble':'%7B%22sessionReferrer%22%3A%20%22https%3A%2F%2Fstar.8.163.com%2Fm%23%2Fmission%22%2C%22updatedTime%22%3A%201532255402469%2C%22sessionStartTime%22%3A%201532255402442%2C%22deviceUdid%22%3A%20%2280482b10-8ded-4811-ac7c-6f2221b2a44d%22%2C%22initial_referrer%22%3A%20%22%24direct%22%2C%22initial_referring_domain%22%3A%20%22%24direct%22%2C%22persistedTime%22%3A%201523758958761%2C%22LASTEVENT%22%3A%20%7B%22eventId%22%3A%20%22click%22%2C%22time%22%3A%201532255402469%7D%2C%22sessionUuid%22%3A%20%226f1ba8ca-5361-4293-8931-d290be750220%22%2C%22user_id%22%3A%202423988%7D'
    }
cheakin_data_f = {
    'k':'iav1h3Hp5YfavR+22ys8RGJIteVyz0rH2Kaj8Sq+nToFZ/6VkTn12hoNXGEfuKEY3a7wKeexkhN2BjfeeVjiinGJTRRZh3Ck20s02bvFpDAmTXTUAvM3gU7/iNgjjpOjF1aAR7MiOLDuhE7UNxKSFjQXh3RhGS1xtORaHDBeIbE=',
    'p':'hn7jofgMv88xYkH/f3Qp/6gEE6XB7+7nYNBRcHKEPtqpN9MOZjeW9z3mufp+sa5aCo+wn9Tsz5R0ibLjbDMaF97gqXHSFRgGckuz9R4aowtexFDT312/33KP99HXj+b4jabzPehJxO2kBGj9gZpQIw=='
                  }
cheakin_data_seven = {
    'k':'BJZeXeo3VT4MaF/DRhd3CWpWvjEeYej49YLX41H60DZh3NGjCp3SCtRbJPDz54RSqpqy0wOYDqDz7LfH2j9S2v9lm7Z1nTZ8OgPumvpIypOP0+BM0NSk7yJzzdPm/6vF4rZwu8/GJFSMlqcgXpJPfS4u7/Bxm0vVb80pYSGroyw=',
    'p':'hT9ti8kx56El3w7ibN0SZG0ZCvlIvpthVhOXnCzLzFFUJPk5gpjJM4DLMg1APOgYWsMbJSchjFJYIAAwv2DDTlySiUUJ/h/zpzKmvy9Jx/95Cdumfa0SYqWaNmXdMSaxhYMdDLyMOP8I8FC2IKbBjg=='
                  }
appMate_seven = "eyJhbnRpU3BhbUluZm8iOiJ7XCJkYXRhdHlwZVwiOlwiYWltdF9kYXRhc1wiLFwiaWRfdmVyXCI6XCJBbmRyb2lkXzEuMC4xXCIsXCJyZGF0YVwiOlwidUZsY015MjdxQzYvd3gzMG9XdUovUHFiMnpCZUhET3RVUnZRbkhCelNZQzdRRjNDMVJaSDQvWFFaempoZTEyUU1sQW5NNE1kM0lyKzN5QkJWNlFFS1lyeDBlL1lGbS9RenBJTHhWUEJDV3dTNWhGZXlzRWVlZ1pmbTFYSy9hWWg3cDcyYnJuMkhkNUlpa3AvbnBYeXBPRVRUeWtJVEFxaW5KZFQ4Y2srL2dCRkJISUp4NHVaY05DN0o2bXFjZ09XcHpsNzBnbjliODVrMVd6ME1yZjFEaXQwSEZKM1BTMVRRMlBDdXRVQ0p3MVYvY2dnd1o1SXUraHBhSzhqRlZ0a3NGSytobk9La21PNlVnNWs0TWQ3ZW01dFV5NVhWMDFveFpvb0hMTWd1SU54bFljaFRXS3Y2eTUzV1N2NTJKNmZQTVhyMXFYNFBURloyV1Jxd3BBSzF6WVFqS2FNeHZRTkpVQkRIWFJ6U2EyWWw1TTk0SWlxYlNodUo3dlBsY01LSDJ2aUZpN2RsQzQvdXNEbEVwZTZLczRaV2FJTFlaNE5SSWxLNENvdE9WRTlvcDI5SEhudEZIcExTc1hjMzkwRnRqUFVsb3p3ZUtuY1Jvd0V5WkNHN3FzaURzZk9Cc25Uc2hGKy93Tjh2NjhsT1dHaGtqNWRBNnZIdGxOUDM2MzVKY0ZnMk04T0RSWDFFWDVaVGZFWGZVaklKK084VDAzRndPR3R5cndhbkdyVTNPM0R0WFNycWlQeTBaMEloc2FXNDlEN0ZEcUkra0dISnV5Ykl0dDRQMkZYdC9XUVY2azNWaDNoRExrcnY2VFdOVGUwR1czUkNReUdEaWUrRitITjVkVnpyOXcxNTE3dXlPQXJCRjR5Ylh1MkZ6T3E3T2RPVHZtNkxBdDh5cjBcdTAwM2RcIixcInJrXCI6XCJQY3c4QWNGQVBITGhLaGMzcWErV1A2RUt2a3ptSlF6UGxaRWxXYXQycmk2NzdFbkIyNmVOb3lWbjYrby81M2dzYlh4WTRMNTJzUkZuWmUydFFxbXhOU2dscm1DZzFGNVZGcTZLRkIyY3hZUDNhVVl0Y0Q3MkpERi82NHhGWElNckR3Mk1VOHErNFp0UWJsQ2xVUVErU3FsRDc4djVjUXRGNHB0dTRhNC9ZNXdcdTAwM2RcIn1cbiIsImFwcFZlcnNpb24iOiIxLjkuNiIsInBhY2thZ2VOYW1lIjoiY29tLm5ldGVhc2UuYmxvY2tjaGFpbiIsImFwcFZlcnNpb25Db2RlIjoiMjc5IiwibWFudWZhY3R1cmVyIjoiSFVBV0VJIiwiT1MiOiJBbmRyb2lkXzIyIiwiY2hhbm5lbCI6ImUwMTE3MDAwNiIsImFwcE5hbWUiOiLmmJ/nkIMiLCJtb2RlbCI6IkRVSy1BTDIwIn0="
appMate_f = "eyJhcHBWZXJzaW9uIjoiMS4zLjAiLCJPUyI6IkFuZHJvaWRfMjYiLCJhcHBOYW1lIjoi5pif55CDIiwiY2hhbm5lbCI6ImUwMTE3MDAwMSIsImFudGlTcGFtSW5mbyI6IntcImRhdGF0eXBlXCI6XCJhaW10X2RhdGFzXCIsXCJpZF92ZXJcIjpcIkFuZHJvaWRfMS4wLjFcIixcInJkYXRhXCI6XCJtMHlWWVlJNEQ3KzM2RllRdXVWSXBiZDlVRmgyOFpBbldDMnV3bzNEZFVoTEVaUVFYVVVCQjB4bnhYUHZzSUk0Y2RWYXhIcXZGdSt2SDN0OTFLMXl1VFBIR2VXWHdWZ2hNY2Fqd051YnhwdWl3dkRVLzllc2J5aHgxYkw5MWlkQnc0NVJPZ0JCUUk4WmM1cnhJVlFsRHdFU1d2ekp0aS9vVkVxTWpVM3ZTZUVHZUVFbDhHZGlvSjVPUnkvSHJsZ1pEQUlwZGoraHRFalhUd2l5bEtoeVNiR1d1MFR5YXdUZUJMK0ZlR1crVUNCbCtOT3E2VTZUa2haVWUvc1V2NU1uZytORlJNS0tXRU1pc01OYWlyVjAyclI5SnpFTmt6Qy9GbmJ5QTdmOFdFNGx6TTAvVlBuRXJVZWdtc2RQdGtPMDMzbjBYVWk2QjFmSHRvZnB5a0NuUWoxUUx1RFZ4TkNxajBBNjFWSkZ6YkZRa1dHUzFNTzNnb3RRa3E4a2RHYjk2aUxWWFRCM2dld2d6ZVFjMmExT3NlZ0ZVWVRTYktMY21JSENKVzNPZUhpTGtiUTMwTmJiVHVyVUpURlhFdk5HNjNuZVFTalNheWowOTZ4SXVDSVFYOXdzNkRzVFBZSTJvNzNOVlR0MTVPNVpIcWhYR1VLSEUraGRLWTJFWmN4WEczcFkzdUJMRTJPY0tnTEFtd0F2WTdPdVVBZlB4bnZQNjlXS3pseGh1ampUQ2h3UWxrK0hYWm01NDc2aENsQ1ZRK3lSeHBvbWRVWUdkZXNGN2FGcU16Mk1odGM3WlZXcGg1MUFOTEp1cXZ5aEh3VDJqMUxydG5Ub2QrbXRvMnZPXCIsXCJya1wiOlwiWE5DUUdKcXhKeHlmbjJZL1dIZVBHVkxzaUNsQi9vKzN1Q0JmZGJCMjBYajFxRW0zaEZzTkJBQmx1L1RTeG9FSGVFRENLaHVINlJkaE1majg3Q0NZNkVnSFhWK2d6SVhVV1A1OTkramxLaEE4clZnT0ttaVczV3FnSlFTcW9RMEU5Q3VWNFNpVjZlbmxneUpQbGp2WjYxVkhhMVB6MkRqM0tRWjBVVTAyUmhBXHUwMDNkXCJ9XG4iLCJtb2RlbCI6IkxPTi1BTDAwIiwicGFja2FnZU5hbWUiOiJjb20ubmV0ZWFzZS5ibG9ja2NoYWluIiwiYXBwVmVyc2lvbkNvZGUiOiIyMDEifQ=="
addr_info = 'https://star.8.163.com/api/home/v2/userInfoAndCollectCoins'
addr_collectCoin='https://star.8.163.com/api/starUserCoin/collectUserCoin'
addr_cheakIn = "https://star.8.163.com/api/checkin/h5CheckIn"
addr_checkStatus = "https://star.8.163.com/api/checkin/status"
addr_event = "https://star.8.163.com/api/realtimeorigin/event"
addr_gameList = "https://star.8.163.com/api/game/list"
addr_gameRecord = "https://star.8.163.com/api/game/record"
addr_read = "https://star.8.163.com/api/starUserOrigin/getTaskUrl"
addr_readDuration = "https://h5sdk.yuedu.163.com/action/read/duration.json"
sJson = "UM_distinctid=171f231033b73-08907fd88315a2-29703570-9c4c8-171f231033c60; YUEDU_LOGIN=d429497b376e93002bb26246fce13701; NETEASE_WDA_UID=d429497b376e93002bb26246fce13701#|#1529209691725; YUEDU_LAST_LOGIN=d429497b376e93002bb26246fce13701#6; YUEDU_V_DID=1588906668621132; JSESSIONID-WYYD=3c7edf1a0f1ebb423fb109d7973c67ff23ac0b0d8328e3e220f273b017a50aae258ed43eaf59b328c11116c48ab8cf7428392a9cfe4e175840a40d11a6e0961873ace53c25ce49161b4e1926107679a05a72fbcb4a0e9382a7962d5ce11fbea9f400bd66bcd82ac12239d6b32a19ac3bf58cfac0963ef5269cfed6e815cbf7a8ef89e384; _ydklxeinuq_=23; XSRF-TOKEN=c6979cbe-e8c8-4f49-9d81-4fa5d8c5013a; __da_ntes_utmfc=utmcsr%3D(direct)%7Cutmccn%3D(direct)%7Cutmcmd%3D(none); davisit=3; YUEDU_TD_C_LINK=atupy9xfu#0cYp92in7; YUEDU_TD_O_LINK=atupy9xfu#0cYp92in7; __da_ntes_utma=133183383.643289298.1588906541.1589111640.1589115388.6; __da_ntes_utmz=133183383.1588906541.1.1.utmcsr%3D(direct)%7Cutmccn%3D(direct)%7Cutmcmd%3D(none); NTES_YD_SESS=iwXClt_40w8Dl0gNrxYRltkMm9f2ZKwi29VbUu1BxVuf5CnFOwbg6tnPo1RDzWLs8uDfZ.dUi2Y8KUfO6RyqZEHV6HXJD5Re1L2m9JI3jhAsHYWCd7b3eUzW7KLSuo2BzZrYd5vvRC0zOsvHeSwYfZpPMV9a3CSvZfsL.NzpecqqVzBVddxRFCy.McsZ4avAMhXGlztfvaYFGr1vexY8yuTcM2c3BkZUdchqUfArttrXq; STAR_YD_SESS=iwXClt_40w8Dl0gNrxYRltkMm9f2ZKwi29VbUu1BxVuf5CnFOwbg6tnPo1RDzWLs8uDfZ.dUi2Y8KUfO6RyqZEHV6HXJD5Re1L2m9JI3jhAsHYWCd7b3eUzW7KLSuo2BzZrYd5vvRC0zOsvHeSwYfZpPMV9a3CSvZfsL.NzpecqqVzBVddxRFCy.McsZ4avAMhXGlztfvaYFGr1vexY8yuTcM2c3BkZUdchqUfArttrXq; YUEDU_TD_CHANNEL=0cYp92in7; SDK_AUTH_=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiJZbVJsTnpGbVpXSmtNR1l5WkRNek5tWTJaakkzTURnMU1EQm1ZMkk0WkRFIiwiYXBwS2V5IjoiMGNZcDkyaW43IiwiZXh0ZW5kSW5mbyI6IlRHeHVaRGh1YWpaMk5pdEhhSE5KVjJGYVZqRjNTME16YVU5VGFFODFNazVPVmsxTlkyUm1aVkpqYURnNE16RjRjVGhZVW5aaGJteEVXR1pQVUd4bVRubHRUM2RyYlhOTWJrNVFkRFZNT0VvelMxVkhMMVp0TWpSQ04wVXdSMU5XVlVWWVpraENRM2hJTUN0a09VOXFRbE5xVVc1ak5XWmthMnAxY0hsMVZpdHZaa3RXWVc5VFVWUjZRMWhaVEVKelkycElha3AwZVdwYVZUQTNjVU50YmtRck5IWkVaekIzU0ZNNFBRIiwiaWF0IjoxNTkwNzMzMTkyfQ.cweYaUC0mZU_NiHcnbGkLYqtM0I7B5vP8zLR5UCFimc; READER_U_SDK_=zji1PLZnnyoWVzaXWWePH5JPLRQdPxOQY1cO2uFxxwNMTvdEsC9ASEMTU5MDczMzE5NDc0Mw1_N_URS; _rom.us.c.v.ol=aCcnF14dfjgPS28SWzQvF1pSBUpORUtVZAFReFJfXxRIfFwfVRpTflFYVQg6145ba68"


def checkStatus():
    response = requests.post(addr_checkStatus,headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Host': 'star.8.163.com',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.9.1'
    },data = json.dumps({"configType":'1'}),cookies = cookies_seven)
    data = json.loads(response.text)['data']
    print("msg："+json.loads(response.text)['msg'])
    print("userStatus: "+str(data["user"]))
    return data['user']['isCheckIn']

def collectcoins(coinId,cookie,vircount):
    print(coinId)
    data = {
        'serialNumber':coinId
        }
    data = json.dumps(data)
    print(data)
    #print(json.loads(data))
    response = requests.post(addr_collectCoin,headers = headers,cookies =cookie,data =data)
    response = json.loads(response.text)
    code = response['code']
    msg = response['msg']
    if(code == 200):
        print("成功收取黑钻：{}个！".format(vircount))
    else:
        print(code)
        print(msg)
def cheakin():
    response = requests.post(addr_cheakIn,headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Host': 'star.8.163.com',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.9.1'
    },data = json.dumps({"configType":'1'}),cookies = cookies_seven)
    data = json.loads(response.text)
    print("cheak in 结果："+json.loads(response.text)['msg'])
    # if(data['data']['isCheckIn'] == 1):
    #     print('已签到')
def gameList():
    try:
        response = requests.post(addr_gameList,headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Host': 'star.8.163.com',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.9.1'
        },cookies = cookies_seven)
        data = json.loads(response.text)
        print("gameList请求结果："+json.loads(response.text)['msg'])
    except:
        print("gameList 请求失败")
    # if(data['data']['isCheckIn'] == 1):
    #     print('已签到')
def gameRecord():
    try:
        response = requests.post(addr_gameRecord,headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Host': 'star.8.163.com',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.9.1'
        },data = json.dumps({"gameId":random.randint(0,20),"gameChannel":"0"}),cookies = cookies_seven)
        data = json.loads(response.text)
        print("gameR请求结果："+json.loads(response.text)['msg'])
    except:
        print("gameR 请求失败")
def eventOrigin():
    events = [{"category":"taobao","triggerBy":"detail"},
    {"category":"taobao","triggerBy":"listPage"},
    {"category":"game","triggerBy":"listPage"},
    {"category":"game","triggerBy":"detail"},
    #{"category":"book","triggerBy":"detail"}
    ]
    for event in events:
        if(event=={"category":"game","triggerBy":"listPage"}):
            gameList()
        elif(event == {"category":"game","triggerBy":"detail"}):
            gameRecord()
        response = requests.post(addr_event,headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Host': 'star.8.163.com',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.9.1'
        },data = json.dumps(event),cookies = cookies_seven)
        print("时间模拟请求结果："+json.loads(response.text)['msg'])
        data = json.loads(response.text)['data']
        print("获得原力 "+str(data['origin']))
def getCRFTToken():
    import requests
    addr_1 = "https://h5sdk.yuedu.163.com/"
    addr_2 = "https://h5sdk.yuedu.163.com/index/popup.json?_tdchannel=0cYp92in7"
    addr_3 = "https://h5sdk.yuedu.163.com/shelf/recentRead.json"
    addr_4 = "https://h5sdk.yuedu.163.com/login/context.json"
    try:
        response = requests.post(addr_read,headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Host': 'star.8.163.com',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.9.1'
        },data = json.dumps({"task":18}),cookies = cookies_seven)
        data = json.loads(response.text)['data']
        print("readLink请求结果："+json.loads(response.text)['msg'])
        readLinkUrl = data['url']
        webForm = readLinkUrl[readLinkUrl.find("?"):]
    
    except:
        print("readLink 请求失败")
    headers = {
        'Host': 'h5sdk.yuedu.163.com',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; DUK-AL20 Build/LMY48Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Safari/537.36 hybrid/1.0.0 star_client_info_begin {hybridVersion: "1.0.0",clientVersion: "1.9.6",accountId: "523b36bd1ab731a7ced0562c8bf69475440dbe76ebba9137b468d9dac99dd927",channel: "e01170006"}star_client_info_end',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,en-US;q=0.8',
        'X-Requested-With': 'com.netease.blockchain'

    }
    try:
        cookies = StringToJSON(sJson)
        response = requests.get(addr_1+webForm,headers =headers,cookies = cookies.extractToJson())
        print(response)
        headers["Accept"] = "application/json"
        response = requests.get(addr_2,headers = headers,cookies = cookies.extractToJson())
        print(response)
        response = requests.get(addr_3,headers = headers,cookies = cookies.extractToJson())
        print(response)
        response = requests.get(addr_4+webForm,headers = headers,cookies = cookies.extractToJson())
        print(response)
        response = json.loads(response.content)
        print(response)
        return response["data"]["csrf_token"]
    except:
        print("csrf_token 请求失败")
        return -1


def read():
    JSON = StringToJSON(sJson)
    try:
        response = requests.post(addr_read,headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Host': 'star.8.163.com',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.9.1'
        },data = json.dumps({"task":18}),cookies = cookies_seven)
        data = json.loads(response.text)['data']
        print("readLink请求结果："+json.loads(response.text)['msg'])
        readLinkUrl = data['url']
        webForm = readLinkUrl[readLinkUrl.find("?"):]

    except:
        print("readLink 请求失败")

    try:
        response = requests.get(addr_GetBookId+webForm,headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Host': 'h5sdk.yuedu.163.com',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; DUK-AL20 Build/LMY48Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Safari/537.36 hybrid/1.0.0 star_client_info_begin {hybridVersion: "1.0.0",clientVersion: "1.9.6",accountId: "523b36bd1ab731a7ced0562c8bf69475440dbe76ebba9137b468d9dac99dd927",channel: "e01170006"}star_client_info_end'
        },cookies = cookies_seven)
        data = response.text
        print(response)
        bookId = data[data.find("<a href=/reader/book/")+len("<a href=/reader/book/"):]
        BookId = bookId[0:bookId.find(" "):]
        crftToken = getCRFTToken()
        for i in range(1,30):   #readDuration 模拟
            print("进入阅读模拟")
            beginTime = time.time()
            endTime = time.time()
            tempForClock = 0
            while(endTime-beginTime<60):
                
                endTime = time.time()
                if(int(endTime) - int(beginTime) == tempForClock):
                    print("clock..."+str(tempForClock))
                    tempForClock += 1
                time.sleep(0.5)
            try:

                dataTemp = {
                'sourceUuid':BookId,#bookID
                'endTime':int(endTime),
                'duration':int(endTime-beginTime),
                'isEnd':0,
                'csrf_token':crftToken
                }
                print(dataTemp["duration"])
                response = requests.post(addr_readDuration,headers = {
                'Host': 'h5sdk.yuedu.163.com',
                'Connection': 'keep-alive',
                'Content-Length': '131',
                'Accept': 'application/json',
                'Origin': 'https://h5sdk.yuedu.163.com',
                'X-Requested-With': 'XMLHttpRequest',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; DUK-AL20 Build/LMY48Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Safari/537.36 hybrid/1.0.0 star_client_info_begin {hybridVersion: "1.0.0",clientVersion: "1.9.6",accountId: "523b36bd1ab731a7ced0562c8bf69475440dbe76ebba9137b468d9dac99dd927",channel: "e01170006"}star_client_info_end',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Referer': 'https://h5sdk.yuedu.163.com/reader/book/'+BookId,
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,en-US;q=0.8'
                },data = urlencode(dataTemp),cookies = JSON.extractToJson())
                data = json.loads(response.text)
                print("readDuration 请求结果：successful = "+str(data['successful']))
            except:
                print("readDuration 请求失败")
                print(response)
    except:
        print("BookId 请求失败")
#     try:
#         response = requests.get(addr_GetCRFTToken+BookId,headers = {
#         'Host': 'h5sdk.yuedu.163.com',
#         'Connection': 'keep-alive',
#         'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; DUK-AL20 Build/LMY48Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Safari/537.36 hybrid/1.0.0 star_client_info_begin {hybridVersion: "1.0.0",clientVersion: "1.9.6",accountId: "523b36bd1ab731a7ced0562c8bf69475440dbe76ebba9137b468d9dac99dd927",channel: "e01170006"}star_client_info_end',
#         'X-Requested-With': 'XMLHttpRequest',
#         'Accept': '*/*',
#         'Referer': 'https://h5sdk.yuedu.163.com/?_tdchannel=0cYp92in7&sdkAuth=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiJZbVJsTnpGbVpXSmtNR1l5WkRNek5tWTJaakkzTURnMU1EQm1ZMkk0WkRFIiwiYXBwS2V5IjoiMGNZcDkyaW43IiwiZXh0ZW5kSW5mbyI6IlIyUkhXREJLYTFOTVdtbGlibVZyV0hnMFUzaE1hbFk0Uld4NE1reHFiRTh5VDFVelYyVjVXR1Y2UkdKMFRtWlBTamRDSzJSeFFXTjBVSHBFZGpkVlRpOUxWVEJYZWpkclZtRTFkMlp4UVVRd05XaDFLMkpsSzFaQk9XWllVRGxHT1ZCVFFuZEVMelpsZGtnclNGbHlRVWR3TWpCelZVRjFWMHgzT0RJNE1GSXhWQ3R5ZDJKUFZEQlVjVE5PVjBKeFUwWk9iemhVZEhWRFEya3lhelJYUTJGaFJuWXlabTluYUZrMFBRIiwiaWF0IjoxNTg5MTE1ODExfQ.1Mg5iuSmTf63WuaSV8wmdNGj2EAhrx32-At5nRYe_jQ',
#         'Accept-Encoding': 'gzip, deflate',
#         'Accept-Language': 'zh-CN,en-US;q=0.8'
#         },cookies = cookies_seven)
#         print(response)
#         data = response.text
#         data = data[data.find('<input id="j-csrf-value" type="hidden" value="')+len('<input id="j-csrf-value" type="hidden" value="'):]
#         data = data[:data.find('"')]
#         crftToken = data
# #<a href=/reader/book/
#     except:
#         print("readLogin 请求失败")


                
# def video():
#     addr = "http://service.cocounion.com/core/wangyi/mars/force?acrationx=-0.192379&acrationy=8.710103&acrationz=4.610334&adtype=40&adowner=5009&uniqid=ffffffff-ed4d-209d-0000-0171f20d2984&placeid=807875237pbfb2k&bt=bde9fcc23a263b003fea44a14847fb28&ca=China+Mobile+GSM&cc=CN&dn=Android&dt=Android_Pad&jb=1&mt=gsm&os=Android&rm=d6%3A65%3A52%3A26%3A54%3Aab&rs=%22jnnlehv055%22&ua=Mozilla%2F5.0+%28Linux%3B+Android+5.1.1%3B+DUK-AL20+Build%2FLMY48Z%3B+wv%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Version%2F4.0+Chrome%2F52.0.2743.100+Safari%2F537.36&cvr=5.3.11&den=288&evt=350&isp=46000&kst=37173122&lac=6311&mcc=460&mnc=000&net=1&ofl=0&ori=1&osv=5.1.1&pid=807875237-1C8144-623D-8214-9ECCF21EF&rnd=1588919666898&srh=1920&srw=1080&adid=5009fb8c2480-4b&anid=2c59cfd743f4bf1c&appv=1.9.6&asdk=1.0.7&bsdk=1.0.7&cell=53185&imei=865143751762578&imsi=460005437528445&lang=zh&sdkv=5.3.11&time="+str(int(time.time()*1000))+"&wmac=c630142c9321&brand=HUAWEI&model=DUK-AL20&siact=1&wymsg=anROdDQwN3NWZEhCUjYzRElGWjNpRFRQNERnRUNPZVFibzl4VTJ0N2JodkFXaE05S3Rsb2lDSElRK2dLenJDMFhKcnFoMlczY21iVk1mMnhWSjhsUE81WGR6d01KUzZqTVRlcmxqMGxYdFFDUUZSbHBLRXZEM2c4WXNZR1ExOHNJVjN4bmc0bDhaWDlKS2Q4Y0k4NUpKNTJTTm5IMUR1QkJzTUF6d1BkbUY0PQ&wyruleid=28&wyuserid=b368bddc58d796fe7fd2a2ddfad3a021&androidosv=5.1.1&hostpkg=com.netease.blockchain&motionx=-0.026179&motiony=0.033084&motionz=0.200488&clickeffect=1&sdktype=2"
#     response = requests.get(addr,headers = {
#         'Accept-Encoding': 'gzip',
#         'DEVICE-KEY': '97a5c9608c8ba7f7',
#         'Host': 'service.cocounion.com',
#         'Connection': 'Keep-Alive'
#         })
#     print("video1："+json.loads(response.text)['msg'])
#     data = json.loads(response.text)['data']
#     headers = {
#         'User-Agent': 'VADNetAgent/0',
#         'Content-Type': 'application/json; charset=utf-8',
#         'Host': 'is.snssdk.com',
#         'Connection': 'Keep-Alive',
#         'Accept-Encoding': 'gzip',
#        'Content-Length':'2531'

#     }
#     jsonData = {"cipher":1,"message":"jsR9IDqJc8QkY4cY8fPDqHF0mV9g7+8kRUF4m\/Z1REzFKcnliT8si194fBdOvne9H9aqV+\/RznqR\nR6hDN\/cWeiQ04zJWP4JQhalE+hSPAV8fZt7U2qlIvPwrrMoItlvTauI4ncLZoUromLDI8k3W\/vVe\nbrnS1J+YgIvncYNp9e7nmFL6yPI0cN0UGNfERy0ndae9yvocC48V5INHS\/nAjI2A2iyajxuAhOv0\nGA+XQLo5uZqIrM\/1NLDLVubseJZ9EI18fX4TGJJJtYuvIAUD7xnkKEqLAGKPmwsOfnLgHvNh9NGt\nOQQWdi\/l6AqobhRck2U+QFMnQif0irVpbrMMGzNM6UrnyzwGAMB8QSmokL0RaYnRzAd+f2XVU0WU\nf3iOiso83sITKwGWHR9AZAxjDiHPyNO8uz7ODrOlHhLrOXSqR6AOb8pWRzZFInDb3oDiYcUywxS0\n6jdGPuPlWt9wyYqgaRex3GIOSPQ2pODZ1vyLtztaK\/0JSiTicwmjQX1o6biEfF6J6nPPy24ih5u6\n9hTwCuMpdZcG+9yBHiR0VNnuni4AT3gupYC3POBl5F0NDUPRIA53aDRQRdKprXoEk2PW8LM2qBo2\nQYeDkSm5NKMz4fjnTrVSel3Jp2MrdRMN88i6O55DM4f8EHRLFFsiPq73Sp4OlsRxz\/5bgwMaDZ9p\nDPBprcUNMkjEFMYwZbilDOjS9dz1tLX5Zo7SgMuEhC7WME1kGsyWYWtGa1pZc2l2rUtPIByVY9fw\nfph8cLKlVvKE0dlJttJV2tCMQy8mSUVkuRG5fbaJJQo3N8nX2hAaIZy4bgv0FDfwsGu7qXuFuEVD\ngm94YFNU\/WB2rAuoSLag9tGndxPYL9alMyjCjCYrGJU4S8IgLYgqrxKUHFYC6+Cx9KO+AsXPMCrC\nfgPU3t0mfJ4P9tqkWtJBapuUhsSSkimOWLQfjrBbf+Ijo89+WA0fE5TAY2uc1Xw3o91UFdePGrkZ\nwUGbUw2MApfAkNfrSkmbF88J16RMP4+VAiVZrDRNGhHwivihWQ1Zvrzj1ngn56TbePnVHBgEVStR\nfT39JYQYsJ5XXVReNsAFr23Y9yN4WO4Mdhh4psGQJz4eMEVuk69VcXNJQunhfw\/d0TEatf7r79lg\n0OZimSfGMTjqUPv2oCJFHkBZH3mBc\/WgJfupuIPj3B70JP6VbTeKqx6HOvR+gUCeUX5znUok2pe4\nJyYfypdfT\/9S1ZAtZTMRvdN\/LaTMeAYOqiKgTEgBbpIMDXBd6TyW3+tMtvO95v2+VePcuOe2Tbyc\ndVwB0iTF1lhlmJHFszDxd36awCkOuxtFZyp5JAQdz70N7ElHmQl7GqrUI35XgrxF4lTKE7W+rx64\nJnhcBMnSXMMsc24tJ6MxgJ+4SzYHx\/2rBlzjYZgvhzESdhSDmcNjLjzR1fruYZA++CXr5s0CHQh1\nI3IkecS0O76290MexxC93mtsTQmxbIdFB536\/jhS1OH3ZxxARG5D6j46Y409\/zrEqAwcqkAJTPdW\nSVt1rk1Fz4uWIKIkvb3QhZ1TaMcqOSl+LXmuk3IQFndNUZMV2wIXHzjPbJcqLNyuXuxwU1tNhIFK\niu\/JI7GDhzotItddAjJispK7lpwW2o6iHFtuFlDG0HGC+JwmyuGc5\/qZyFrVlk+WU66XWuo35x96\nDGSeUnV64j43SufZLW1i8C2MG6TCFaFHhDmXyp0olUpQlJMKt4NkvL454xGCFx2d8YnhsWA0PIxK\nJBOMSKM\/+2P\/xfH3cuAgCJ4a9QzonAPaqqNdFmeIedEYSo0Cj8mXvvNdWB7kpaFr7rwjHXkGr27e\nf7EXrgtijzUipzR\/2qgUEkD89SnZsuQmUj+oxyYu5Y8zuMjkdCzQU1DHs5VfDp1L391HkycCLfIC\n5X9h9Ugua9+l40d0uA+CI4SwDkHAOwiPFHG0ZfbN+RW9dMAtF43xJ9H5dWI556MX9yEdZ0H7\/NVX\n\/TTNCZN0GMwA1\/qAXZWkf\/JTtiMLW1jYVdOh8D49ydw6I1M9odR29iNYnpkXQKSQbZNu9JwrZV9i\nEZ30g4+S6jstQLkYUzjrwWfcw8HtA+3PR6EJJ+7PLgIXmUgHEwJwDlrgX\/9F1WNDd3cbNyhlqYk1\n8g1cz13i3zy5qqxSGZPEU5EYwAWF+fSJHKNuw2Yk3Pk7h1KbU6H+tNI1usaeX8PGV1\/9Whun4sPa\nJflBoMs2hUBJ0tG9o8rx\/7e1EzVJkPWIa4YVqgq2VNN5A5apBlOG4XWnLObOowDfJV8AOC4QH66x\ncVrDY+2DDusFs0s19P0Dj13i6nV+Zl7OknZLROIXdfSABQUhxu7PEpCJY5mns7u183XjM9JkTsA1\nVwKc15oExE07CJRFUhtV5XbneEf5h7eGUK8g\/C2mvZQJy3Uz17tE4zs=\n"}
#     try:
#         response = requests.post("https://is.snssdk.com/api/ad/union/sdk/reward_video/reward/",headers = headers,data = json.dumps(jsonData))
#         data = json.loads(response.text)['data']
#         print("video结果："+str(json.loads(response.text)['verify']))
#         print("data："+str(data))
#     except:
#         print("video请求失败")
def star(cookie,userMate,cheakInData):
    try: 
        if(checkStatus() == 0):
            cheakin()
        else:
            print("checkInEd")
    except:
        print('请求失败、')
    data_info = {
        'type':0}
    data_info = json.dumps(data_info)
    response = requests.post(addr_info,headers = headers,cookies = cookie,data = data_info)
    jsondata = json.loads(response.text)
   # print(jsondata)
    msg = jsondata['msg']
    code = jsondata['code']
    print(msg)
    if(code == 200):
        nickName = jsondata['data']['userInfo']['nickName']
        yuanLi = jsondata['data']['origin']
        coin = jsondata['data']['coin']


        collectCoinsList = jsondata['data']['collectCoins']
        print("用户名:{name}\n原力值:{origin}\n黑钻值{coins}\n".format(name = nickName,origin = yuanLi,coins = coin))
        if len(collectCoinsList) == 0:
            print("当前没有黑钻可以领取\n")
            print("--------------------------------------------------\n")
        else:
            for collectCoinItem in collectCoinsList:
                #print(collectCoinItem)
                collectcoins(collectCoinItem['serialNumber'],cookie,collectCoinItem['virCount'])

        try:
            read()
            for i in range(1,10):
                # video()
                eventOrigin()
                time.sleep(1)
        except:
            print("事件模拟请求失败")
    else:
        print("登入失败")

star(cookies_seven,appMate_seven,cheakin_data_seven)
#
# star(cookies_f,appMate_f,cheakin_data_f)
