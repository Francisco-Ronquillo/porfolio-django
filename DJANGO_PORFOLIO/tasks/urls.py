from django.urls import path
from.views import signup, signin,base,signout

app_name = "tasks"
urlpatterns = [
    path("signup/",signup, name="signup"),
    path("",base,name='base'),
    path("signin/",signin,name='signin'),
    path("signout/",signout,name='signout')
]
