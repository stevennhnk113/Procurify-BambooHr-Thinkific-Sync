import json
import bamboohrController
import thinkificController


def lambda_handler(event, context):
    # TODO implement

    userFromBambooHr = bamboohrController.GetEmployeeDirectory()
    # userFromThinkific = thinkificController.RetrieveAListOfUsers()

    if userFromBambooHr is None:
        return {
            'statusCode': 500,
            'body': json.dumps('Fail to get data from thinkific/bamboohr')
        }

    courses = [{
        'id': 576312,
        'name': 'Procurify Pay Certification Course',
        'customeFieldName': 'customProcurifyPay'
    }, {
        'id': 577216,
        'name': 'NetSuite Integration Certification',
        'customeFieldName': 'customNetSuiteIntegration'
    }]

    logs = []
    for course in courses:
        enrollments = thinkificController.RetrieveAListOfEnrollments(course['id'])

        for enrollment in enrollments:
            email = enrollment['user_email']

            if email in userFromBambooHr:
                percent = int(float(enrollment['percentage_completed']) * 100)
                userIdInBambooHr = userFromBambooHr[email]['id']
                success = bamboohrController.UpdateEmployeeCustomField(userIdInBambooHr, course['customeFieldName'], percent)

                if not success:
                    logs.append({
                        'error': 'cannot update user',
                        'email': email
                    })

    return {
        'statusCode': 200,
        'body': json.dumps(logs)
    }


lambda_handler(None, None)
