"""payticket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
#from main.views import
from django.conf import settings
from django.conf.urls.static import static

from main.views import AgencyList,StationList,TripList

from core.views import AuthRegister
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

router= routers.DefaultRouter()
router.register(r"agencies",AgencyList)
router.register(r"stations",StationList)
router.register(r"trips",TripList)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('api/registration',AuthRegister.as_view(), name="registration"),
    path('api/token/', obtain_jwt_token, name='token_obtain_pair'),
    path('api/token/refresh/', refresh_jwt_token, name='token_refresh'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
