from django.conf.urls.static import static
from django.conf import settings

from django.urls import path

import apiApp.views as views


urlpatterns = [
    
    path('index',views.index,name='index'),    
    path('createNewSurveyFromTemplate',views.createNewSurveyFromTemplate,name='createNewSurveyFromTemplate'),    
    path('userViewSurvey',views.userViewSurvey,name='userViewSurvey'),
    path('userListViewSurvey',views.userListViewSurvey,name='userListViewSurvey'),   
    path('publicSurvey',views.publicSurvey,name='publicSurvey'),   
    path('publicSurveyResponse',views.publicSurveyResponse,name='publicSurveyResponse'),   
    path('viewResponseData',views.viewResponseData,name='viewResponseData'),   
    path('addEmailToUser',views.addEmailToUser,name='addEmailToUser'),   
    path('getEmailListOfUser',views.getEmailListOfUser,name='getEmailListOfUser'),   
    path('deleteEmailFromUser',views.deleteEmailFromUser,name='deleteEmailFromUser'),   
    path('sendEmail',views.sendEmail,name='sendEmail'),   

] +static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
