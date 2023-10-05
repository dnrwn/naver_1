import json

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


print(body)