from django.shortcuts import render,redirect
import firebase_admin
from firebase_admin import firestore,credentials,storage,auth
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import pyrebase
from datetime import date
db = firestore.client()
# Create your views here.
def Myprofile(request):
    user=db.collection("tbl_userregistration").document(request.session['usid']).get().to_dict()
    return render(request,"User/Myprofile.html",{'user':user})
    
def Editprofile(request):
    user=db.collection("tbl_userregistration").document(request.session['usid']).get().to_dict()
    if request.method == "POST":
        Name=request.POST.get("txt_name")
        Contact=request.POST.get("txt_contact")
        Address=request.POST.get("txt_address")
        user =  {"user_name":Name,"user_contact":Contact,"user_address":Address} 
        db.collection("tbl_userregistration").document(request.session['usid']).update(user)
        return redirect("webuser:Homepage")
    else:
        return render(request,"User/Editprofile.html",{"user":user}) 

def Changepassword(request):
    user = db.collection("tbl_userregistration").document(request.session["usid"]).get().to_dict()
    email = user["user_email"]

    rest_link = firebase_admin.auth.generate_password_reset_link(email)

    send_mail(
        'Reset your password ', #subject
        "\rHello \r\nFollow this link to reset your Project password for your " + email + "\n" + rest_link +".\n If you didn't ask to reset your password, you can ignore this email. \r\n Thanks. \r\n Your D MARKET team.",#body
        settings.EMAIL_HOST_USER,
        [email],
    )
    return redirect("webuser:Homepage")        

def Homepage(request):
    return render(request,"User/Homepage.html")


def Orphanagerequest(request):
    orphreq = db.collection("tbl_request").where("status", "==", 1).stream()
    orphreq_data=[]
    for i in orphreq:
        orphreqdata=i.to_dict()
        dt = db.collection("tbl_donationtype").document(orphreqdata["donationtype_id"]).get().to_dict()
        odata={"orphreq":orphreqdata,"id":i.id,"dtype":dt}
        orphreq_data.append(odata)
    return render(request,"User/Orphanagerequest.html",{"orphreqdata":orphreq_data})


def Donation(request):
    donation = db.collection("tbl_donationtype").stream()
    donation_data=[]
    for i in donation:
        donationdata=i.to_dict()
        ddata={"donation":donationdata,"id":i.id}
        donation_data.append(ddata)
    do = db.collection("tbl_donation").where("user_id", "==", request.session["usid"]).stream()
    don_data = []
    for don in do:
        ddata = don.to_dict()
        don_type = db.collection("tbl_donationtype").document(ddata["donationtype_id"]).get().to_dict()
        orph = db.collection("tbl_orphanageregistration").document(ddata["orphnage_id"]).get().to_dict()
        don_data.append({"donation":don.to_dict(),"id":don.id,"dtype":don_type,"orphnage":orph})
    if request.method=="POST":
        Title=request.POST.get("txt_title")
        Description=request.POST.get("txt_description")
        Donationtype=request.POST.get("txt_donationtype")
        data = {"title":Title,"description":Description,"donationtype_id":Donationtype,"user_id":request.session["usid"],"date":str(date.today()),"orphnage_id":"null","donation_status":0}
        db.collection("tbl_donation").add(data)
        return redirect("webuser:Donation")
    else:
        return render(request,"User/Donation.html",{"donation_type":donation_data,"donation":don_data})


def Complaint(request):
    if request.method=="POST":
        db.collection("tbl_complaint").add({"complaint_content":request.POST.get("txt_complaint"),"complaint_status":0,"complaint_reply":"","user_id":request.session["usid"],"orphnage_id":""})
        return render(request,"User/Homepage.html",{"msg":"Complaint sended..."})
    else:
        return render(request,"User/Complaint.html")


def View_Reply(request):
    reply = db.collection("tbl_complaint").where("user_id", "==", request.session["usid"]).stream()
    r_data = []
    for i in reply:
        r_data.append({"reply":i.to_dict(),"id":i.id})
    return render(request,"User/View_Reply.html",{"reply":r_data})   


def Feedback(request):
    feedback = db.collection("tbl_feedback").where("user_id", "==", request.session["usid"]).stream()
    feedback_data=[]
    for i in feedback:
        feedbackdata=i.to_dict()
        fdata={"feedback":feedbackdata,"id":i.id}
        feedback_data.append(fdata)
    if request.method=="POST":
        Feedback=request.POST.get("txt_feedback")
        data = {'feedback':Feedback,"user_id":request.session["usid"],"orphnage_id":""}
        db.collection("tbl_feedback").add(data)
        return redirect("webuser:Homepage")
    else:
        return render(request,"User/Feedback.html",{"feedbackdata":feedback_data})        
