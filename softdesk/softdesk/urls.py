"""
URL configuration for softdesk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from api.views import PersonView, TestViewset
from user.views import GetRegisterView, RegisterView, LoginView, LoginView2, LoginView0, RegisterView2

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router1 = routers.SimpleRouter()
router1.register('Test1', TestViewset, basename='test')

'''
router2 = routers.SimpleRouter()
router2.register('Test1', TestViewset, basename='test')
'''



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/Person/', PersonView.as_view()),
    path('api/', include(router1.urls)), # path http://127.0.0.1:8000/api/Test1/

    #path('user/get/', GetRegisterView.as_view()),
    path('signup/', RegisterView.as_view()),
    #path('login/', LoginView.as_view()),
    #path('login2/', LoginView2.as_view()),
    #path('login0/', LoginView0.as_view()),
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('signup2/', RegisterView2.as_view()),

]
