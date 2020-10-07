import requestHelper
import fileController


config = fileController.GetConfig()
thinkificConfig = config['thinkific']
apiKey = thinkificConfig['apiKey']
subdomain = thinkificConfig['subdomain']

headers = {
    'X-Auth-API-Key': apiKey,
    'X-Auth-Subdomain': subdomain
}


def RetrieveAListOfUsers():
    procurifyGroup = thinkificConfig['procurifyGroup']
    groupId = procurifyGroup['id']

    partialApi = '/users?limit=500&query[group_id]=' + str(groupId)
    fullApi = GetFullApi(partialApi)

    result = requestHelper.MakeRequest('get', fullApi, headers, None)

    result = requestHelper.AsDict(result['data']['items'], 'email')
    return result


def RetrieveAListOfEnrollments(courseId):
    partialApi = '/enrollments?limit=1000&query[course_id]=' + str(courseId)
    fullApi = GetFullApi(partialApi)

    result = requestHelper.MakeRequest('get', fullApi, headers, None)

    return result['data']['items']


def GetFullApi(partialApi):
    return 'https://api.thinkific.com/api/public/v1' + partialApi
