from django.urls import path,include
from Guest import views

app_name = "webguest"
urlpatterns = [
    path('User_Registration/',views.User_Registration,name="User_Registration"),
    path('Orphanage_Registration/',views.Orphanage_Registration,name="Orphanage_Registration"),
    path('',views.Login,name="Login"),
    path('ajaxplace/',views.ajaxplace,name="ajaxplace"),
     path('index/',views.index,name="Index"),
]