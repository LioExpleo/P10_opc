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
from api.views import PersonView, TestViewset, ProjectsViewset, ContributorsView, ContributorsDelView, IssueView, IssuePutView, CommentView # , ProjectsIdViewset #, ProjectsView,
from user.views import RegisterView, LoginView

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router1 = routers.SimpleRouter()
router1.register('Test1', TestViewset, basename='test')

'''
router2 = routers.SimpleRouter()
router2.register('Test1', TestViewset, basename='test')
'''

router3 = routers.SimpleRouter()
router3.register('', ProjectsViewset, basename='projects')

router4 = routers.SimpleRouter()
#router4.register('projects', ProjectsIdViewset, basename='projects_id')

router5 = routers.SimpleRouter()
router5.register('', ContributorsView, basename='contributor_projects')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('api/Person/', PersonView.as_view()),
    path('api/', include(router1.urls)), # path http://127.0.0.1:8000/api/Test1/

    path('signup/', RegisterView.as_view()),
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('PostProjects/', ProjectsView.as_view()),
    path('projects/', include(router3.urls)),
    #path('projects/<int:pk>/', include(router3.urls)),
    path('projects/<int:pk>/users/', ContributorsView.as_view()),
    path('projects/<int:pk>/users/<int:pk_contrib>', ContributorsDelView.as_view()),
    path('projects/<int:pk>/issues/', IssueView.as_view()),
    path('projects/<int:pk>/issues/<int:pk_issue>', IssuePutView.as_view()),
    path('projects/<int:pk>/issues/<int:pk_issue>/comments/', CommentView.as_view()),


]
