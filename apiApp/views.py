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
        obj = obj.to_dict(orient='records')[0]
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
    return Response(data)