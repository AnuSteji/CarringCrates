from django.urls import path,include
from User import views

app_name = "webuser"
urlpatterns = [
    path('Myprofile/',views.Myprofile,name="Myprofile"),
    path('Changepassword/',views.Changepassword,name="Changepassword"),
    path('Editprofile/',views.Editprofile,name="Editprofile"),
    path('Editprofile/<str:id>',views.Editprofile,name="Editprofile"),
    path('Homepage/',views.Homepage,name="Homepage"),
    path('Orphanagerequest/',views.Orphanagerequest,name="Orphanagerequest"),
    path('Donation/',views.Donation,name="Donation"),
    path('Complaint/',views.Complaint,name="Complaint"),
    path('View_Reply/',views.View_Reply,name="View_Reply"),
    path('Feedback/',views.Feedback,name="Feedback"),
]
    