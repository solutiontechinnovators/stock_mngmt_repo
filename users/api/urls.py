from django.urls import path
from users.api import views
from rest_framework.authtoken.views import obtain_auth_token
from .views import CustomObtainAuthToken
app_name = 'users'

urlpatterns = [
    path('registration', views.registration_view, name='registration'),
    # path('login_ty', obtain_auth_token, name='login_ty'),
    path('login', CustomObtainAuthToken.as_view()),

]
