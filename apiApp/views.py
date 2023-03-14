from import_statements import *

# Create your views here.

@api_view(['GET'])
def index(request):
    obj = survey_templates.objects.values()
    obj = pd.DataFrame(obj)
    obj['survey'] = obj['survey'].apply(lambda x : eval(x))
    obj['config'] = obj['config'].apply(lambda x : eval(x))
    obj['welcome_screen'] = obj['welcome_screen'].apply(lambda x : eval(x))
    obj = obj.to_dict(orient='records')
    return Response(obj)

@api_view(['POST'])
def createNewSurveyFromTemplate(request):
    data = request.data
    token = data['token']
    try:
        user = user_data.objects.get(uid = token)
    except:
        res = {
                'status':False,
                'message':'Authentication Failed'
              }
        return Response(res)
    survey_template_obj = survey_templates.objects.values().last()
    user_id = user.id
    data = user_surveys(
                            user_id = user_id,
                            survey = survey_template_obj['survey'],
                            config = survey_template_obj['config'],
                            welcome_screen = survey_template_obj['welcome_screen'],
                            thank_you_screen = survey_template_obj['thank_you_screen']
                       )
    data.save()
    res = {
            'status':True,
            'message':'Survey added for user',
            'survey_id':str(data.id)
          }
    return Response(res)

@api_view(['POST'])
def userViewSurvey(request):
    data = request.data
    token = data['token']
    try:
        user = user_data.objects.get(uid = token)
    except:
        res = {
                'status':False,
                'message':'Authentication Failed'
              }
        return Response(res)
    survey_id = data['survey_id']
    obj = user_surveys.objects.filter(id = survey_id).values()
    if len(obj) == 0:
        res = {
                'status':False,
                'message':'Survey does not exist'
              }
        return Response(res)
    else:
        obj = pd.DataFrame(obj)
        obj['survey'] = obj['survey'].apply(lambda x : eval(x))
        obj['config'] = obj['config'].apply(lambda x : eval(x))
        obj['welcome_screen'] = obj['welcome_screen'].apply(lambda x : eval(x))
        obj = obj.to_dict(orient='records')[0]
        return Response(obj)

@api_view(['POST'])
def userListViewSurvey(request):
    data = request.data
    token = data['token']
    try:
        user = user_data.objects.get(uid = token)
    except:
        res = {
                'status':False,
                'message':'Authentication Failed'
              }
        return Response(res)
    res = {}
    headings = ["Title", "Status", "Responses", "Created", "Actions"]
    res['headings'] = headings
    survey_obj = user_surveys.objects.filter(user_id = user.id).values()
    survey_obj = pd.DataFrame(survey_obj)
    survey_obj['id'] = survey_obj['id']
    survey_obj['title'] = survey_obj['welcome_screen'].apply(lambda x : eval(x)['heading'])
    survey_obj['status'] = survey_obj['survey_staus'].apply(lambda x : 'LIVE' if x else 'CLOSED')
    survey_obj['response'] = survey_obj['id'].apply(lambda x : survey_response.objects.filter(id = x).values().count())
    survey_obj['created'] = survey_obj['creation_date_time'].apply(lambda x : x[:10])
    survey_obj = survey_obj[['id','title','status','response','created']]
    survey_obj = survey_obj.to_dict(orient='records')
    res['content'] = survey_obj
    return Response(res)

@api_view(['GET'])
def publicSurvey(request):
    survey_id = request.GET.get('survey_id')
    obj = user_surveys.objects.filter(id = survey_id).values()
    if len(obj)>0:
        obj = pd.DataFrame(obj)
        obj['survey'] = obj['survey'].apply(lambda x : eval(x))
        obj['config'] = obj['config'].apply(lambda x : eval(x))
        obj['welcome_screen'] = obj['welcome_screen'].apply(lambda x : eval(x))
        obj = obj[['survey','config','welcome_screen','thank_you_screen']]
        obj = obj.to_dict(orient='records')[0]
        obj['thank_you_screen'] =  {
                                    'message': "Thank you for your time!",
                                    }
        return Response(obj)
    else:
        res = {
                'status':False,
                'message':"Survey doesn't exist"
              }
        return Response(res)
@api_view(['POST'])
def publicSurveyResponse(request):
    data = request.data
    survey_id = request.GET.get('survey_id')
    res_obj = survey_response(
                                survey_id = survey_id,
                                survey = data['survey']
                             )
    res_obj.save()
    res = {
            'status':True,
            'message':'Response submitted'
    }
    return Response(data)
@api_view(['POST'])
def viewResponseData(request):
    data = request.data
    token = data['token']
    try:
        user = user_data.objects.get(uid = token)
    except:
        res = {
                'status':False,
                'message':'Authentication Failed'
              }
        return Response(res)
    res = {}
    survey_id = data['survey_id']
    survey_obj = survey_response.objects.filter(survey_id = survey_id).values('survey')
    if len(survey_obj) == 0:
        res = {
                'status':False,
                'message':'No surveys found'
              }
        return Response(res)
    survey_obj = pd.DataFrame(survey_obj)
    survey_obj['all_answers'] = survey_obj['survey'].apply(lambda x : eval(x))
    survey_obj = survey_obj[['all_answers']].to_dict(orient='records')
    res['answers'] = survey_obj
    questions = pd.DataFrame(survey_obj[0]['all_answers'])['question']
    res['questions'] = questions

    config = {
                'rows': len(survey_obj),
                'column': len(questions),
             }
    res['config'] = config
    return Response(res)

@api_view(['POST'])
def addEmailToUser(request):
    data = request.data
    token = data['token']
    try:
        user = user_data.objects.get(uid = token)
    except:
        res = {
                'status':False,
                'message':'Authentication Failed'
              }
        return Response(res)
    email = data['email']
    emails = email_list.objects.filter(user_id = user.id).values_list('email',flat=True)
    if email == '':
        res = {
                'status':False,
                'message':'Invalid Email'
              }
        return Response(res)
    if email in emails:
        res = {
                'status':False,
                'message':'Email already in address book'
              }
        return Response(res)
    email_obj = email_list(
                            user_id = user.id,
                            email = email,
                          )
    email_obj.save()
    res = {
            'status':True,
            'message':'Email added to address book'
            }
    return Response(res)

@api_view(['POST'])
def getEmailListOfUser(request):
    data = request.data
    token = data['token']
    try:
        user = user_data.objects.get(uid = token)
    except:
        res = {
                'status':False,
                'message':'Authentication Failed'
              }
        return Response(res)
    emails = email_list.objects.filter(user_id = user.id).values_list('email',flat=True)
    res = {
            'status':True,
            'message':'Email list generated',
            'email_list':emails
            }
    return Response(res)

@api_view(['POST'])
def deleteEmailFromUser(request):
    data = request.data
    token = data['token']
    try:
        user = user_data.objects.get(uid = token)
    except:
        res = {
                'status':False,
                'message':'Authentication Failed'
              }
        return Response(res)
    email = data['email']
    emails = email_list.objects.filter(user_id = user.id).values_list('email',flat=True)
    if email not in emails:
        res = {
                'status':False,
                'message':'Email does not exist'
              }
        return Response(res)
    email_list.objects.filter(user_id = user.id,email = email).delete()
    res = {
            'status':True,
            'message':'Email deleted successfully',
            }
    return Response(res)

@api_view(['POST'])
def sendEmail(request):
    data = request.data
    token = data['token']
    try:
        user = user_data.objects.get(uid = token)
    except:
        res = {
                'status':False,
                'message':'Authentication Failed'
              }
        return Response(res)
    emails = data['emails']
    subject = data['subject']
    msg = data['message']
    send_email = sendEmailFunc(emails,subject,msg)
    if send_email:
        res = {
                'status':True,
                'message':'Email sent successfully'
              }
    else:
        res = {
                'status':False,
                'message':'Something went wrong'
              }
    return Response(res)

@api_view(['POST'])
def npsCalculate(request):
    data = request.data
    survey_id = data['survey_id']
    survey_obj = survey_response.objects.filter(survey_id = survey_id).values('survey')
    if len(survey_obj) == 0:
        res = {
                'status':False,
                'message':'No surveys found'
              }
        return Response(res)
    survey_obj = pd.DataFrame(survey_obj)
    survey_obj['all_answers'] = survey_obj['survey'].apply(lambda x : eval(x))
    survey_obj['nps'] = survey_obj['all_answers'].apply(lambda x : x[5]['answer'] if x[5]['answer'] != "" else 0)
    res = {}
    res['answers'] = list(survey_obj['nps'])
    return Response(res)