from django.urls import path,include
from Orphanage import views
app_name = "weborphanage"
urlpatterns = [
    path('Myprofile/',views.Myprofile,name="Myprofile"),
    path('Changepassword/',views.Changepassword,name="Changepassword"),
    path('Editprofile/',views.Editprofile,name="Editprofile"),
    path('Editprofile/<str:id>',views.Editprofile,name="Editprofile"),
    path('Homepage/',views.Homepage,name="Homepage"),
    path('Request/',views.Request,name="Request"),
    path('Complaint/',views.Complaint,name="Complaint"),
    path('Assigned_Donation/',views.Assigned_Donation,name="Assigned_Donation"),
    path('View_Reply/',views.View_Reply,name="View_Reply"),
    path('Feedback/',views.Feedback,name="Feedback"),
]