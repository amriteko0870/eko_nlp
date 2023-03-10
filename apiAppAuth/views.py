from import_statements import *

# Create your views here.

@api_view(['POST'])
def createOrLogin(request):
    data = request.data
    uid = data['user']['uid'] 
    try:
        user = user_data.objects.get(uid = uid)
        res  = { 
                    'status':True,
                    'token':user.uid,
                    'message':'login sucessfull',
                    'creation_status':'old'
                }
        return Response(res)
    except: 
        email = data['user']['email'] 
        displayName = data['user']['displayName']

        data = user_data(
                            name = displayName,
                            email = email,
                            uid = uid,
                        )
        data.save()
        res  = { 
                    'status':True,
                    'token':data.uid,
                    'message':'login sucessfull',
                    'creation_status':'new'
                }

        return Response(res)
    
