import urllib.request
import json

data = {
    "X-Naver-Client-Id": "uv_lv7I3jpwBqWkHVDOx",
    "X-Naver-Client-Secret": "2FttqJ6b99",
    "url": "https://openapi.naver.com/v1/datalab/search"
}
parameter = {
    "startDate" : "2023-10-04",
    "endDate" : "2023-10-04",
    "timeUnit" : "date",
    "keywordGroups" : [{
        "groupName" : "aaa",
        "keywords" : ["aaa", "bbb"]
    }],
    "device" : "mo",  # Optional
    "gender" : "f",  # Optional
    "ages" : ["1", "2"]  # Optional
}

body = json.dumps(parameter)

request = urllib.request.Request(data['url'])
request.add_header("X-Naver-Client-Id",data['X-Naver-Client-Id'])
request.add_header("X-Naver-Client-Secret",data['X-Naver-Client-Secret'])
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)