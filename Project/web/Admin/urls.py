from django.urls import path,include
from Admin import views

app_name="webadmin"

urlpatterns = [
    path('Homepage/',views.Homepage,name="Homepage"),
    path('District/',views.District,name="District"),
    path('delete_dist/<str:id>',views.delete_dist,name="delete_dist"),
    path('edit_dist/<str:id>',views.edit_dist,name="edit_dist"),
    path('Donationtype/',views.Donationtype,name="Donationtype"),
    path('delete_donation/<str:id>',views.delete_donation,name="delete_donation"),
    path('edit_donation/<str:id>',views.edit_donation,name="edit_donation"),
    path('Admin_Registration/',views.Admin_Registration),
    path('Place/',views.Place,name="Place"),
    path('delete_place/<str:id>',views.delete_place,name="delete_place"),
    path('edit_place/<str:id>',views.edit_place,name="edit_place"),
    path('NewOrphanage/',views.NewOrphanage,name="NewOrphanage"),
    path('accept_orphanage/<str:id>',views.accept_orphanage,name="accept_orphanage"),
    path('reject_orphanage/<str:id>',views.reject_orphanage,name="reject_orphanage"),
    path('Orphanagerequest/',views.Orphanagerequest,name="Orphanagerequest"),
    path('accept_orphanagerequest/<str:id>',views.accept_orphanagerequest,name="accept_orphanagerequest"),
    path('reject_orphanagerequest/<str:id>',views.reject_orphanagerequest,name="reject_orphanagerequest"),
    path('accepted_orrequest/',views.accepted_orrequest,name="accepted_orrequest"),
    path('rejected_orrequest/',views.rejected_orrequest,name="rejected_orrequest"),
    path('Accepted_Orphanage/',views.Accepted_Orphanage,name="Accepted_Orphanage"),
    path('Rejected_Orphanage/',views.Rejected_Orphanage,name="Rejected_Orphanage"),
    path('View_User_Donation/',views.View_User_Donation,name="View_User_Donation"),
    path('Assign_User_Request/<str:id>',views.Assign_User_Request,name="Assign_User_Request"),
    path('Assigned_Request/',views.Assigned_Request,name="Assigned_Request"),
    path('feedback/',views.feedback,name="feedback"),
    path('complaint/',views.complaint,name="complaint"),
    path('reply/<str:id>',views.reply,name="reply"),
    path('replyed_complaint/',views.replyed_complaint,name="replyed_complaint"),
    
]
