from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    # NEW PATH : path('<appname>/', include('<appname>.urls', namespace="<appname>")),
    path('authy', views.authy, name="authy"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
]



