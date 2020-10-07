import json
import requests
import base64


def MakeRequest(method, restApi, headers, payload):
    myPayload = None
    if payload is not None:
        myPayload = json.dumps(payload)
        headers["Content-Type"] = "application/json"

    response = None
    result = {
        "success": False,
        "data": None
    }

    # Make request
    try:
        response = requests.request(
            method, restApi, data=myPayload, headers=headers)
    except:
        return result

    if 200 <= response.status_code < 300:
        result["success"] = True

    # Decode returned data
    try:
        result['data'] = {**result, **json.loads(response.text)}
    except:
        result["data"] = None

    if "errors" in result:
        result["success"] = False

    return result


def GetBasicAuthentication(username, password):
    encodingStr = username + ":" + password
    temp = base64.b64encode(encodingStr.encode())
    return "Basic " + temp.decode()


def AsDict(arr: [], key: str):
    temp = {}
    for item in arr:
        temp[item[key]] = item

    return temp
