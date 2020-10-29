from django.urls import path, include
from . import views


urlpatterns = [

    path('assign_user_position', views.assign_user_position, name="assign_user_position"),
    path('add_shop', views.add_shop, name="add_shop"),
    path('assign_user_shop', views.assign_user_shop, name="assign_user_shop"),

]
