import json


def GetConfig():
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
    except:
        return None

    return config
