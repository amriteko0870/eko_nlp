from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apiApp.urls')),
    path('auth/',include('apiAppAuth.urls'))
]