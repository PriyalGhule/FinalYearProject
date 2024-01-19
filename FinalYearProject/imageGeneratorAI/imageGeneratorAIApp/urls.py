from django.urls import path

from . import views

urlpatterns=[
    # path("", views.index, name="index"),
    path("login/",views.login,name="login"),
    path("register/",views.register, name="register"),
    path("home/",views.home,name="home"),
    path("",views.landing,name="landing"),
    path("about/",views.about, name="about"),
    path("profile/",views.profile, name="profile"),
]