import requestHelper
import fileController

config = fileController.GetConfig()
bamboohrConfig = config['bamboohr']

username = bamboohrConfig['username']
password = bamboohrConfig['password']

headers = {
    'Accept': 'application/json',
    'Authorization': requestHelper.GetBasicAuthentication(username, password)
}


def GetEmployeeDirectory():
    partialApi = '/v1/employees/directory'
    fullApi = GetFullApi(partialApi)

    result = requestHelper.MakeRequest('get', fullApi, headers, None)

    if not result['success']:
        return None

    result = requestHelper.AsDict(result['data']['employees'], 'workEmail')
    return result


def UpdateEmployeeCustomField(userId, field: str, val: str):
    body = {
        field: val
    }

    partialApi = '/v1/employees/' + str(userId) + '/'
    fullApi = GetFullApi(partialApi)

    result = requestHelper.MakeRequest('post', fullApi, headers, body)

    return result['success']


def GetFullApi(partialApi):
    return 'https://api.bamboohr.com/api/gateway.php/procurify' + partialApi

