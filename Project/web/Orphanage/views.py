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
    orphanage=db.collection("tbl_orphanageregistration").document(request.session['opid']).get().to_dict()
    return render(request,"Orphanage/Myprofile.html",{'orphanage':orphanage})

def Editprofile(request):
    orphanage=db.collection("tbl_orphanageregistration").document(request.session['opid']).get().to_dict()
    if request.method == "POST":
        Name=request.POST.get("txt_name")
        Contact=request.POST.get("txt_contact")
        Address=request.POST.get("txt_address")
        orphanage =  {"orphanage_name":Name,"orphanage_contact":Contact,"orphanage_address":Address} 
        db.collection("tbl_orphanageregistration").document(request.session['opid']).update(orphanage)
        return redirect("weborphanage:Homepage")
    else:
        return render(request,"Orphanage/Editprofile.html",{"orphanage":orphanage})

def Changepassword(request):
    orphanage = db.collection("tbl_orphanageregistration").document(request.session["opid"]).get().to_dict()
    email = orphanage["orphanage_email"]

    rest_link = firebase_admin.auth.generate_password_reset_link(email)

    send_mail(
        'Reset your password ', #subject
        "\rHello \r\nFollow this link to reset your Project password for your " + email + "\n" + rest_link +".\n If you didn't ask to reset your password, you can ignore this email. \r\n Thanks. \r\n Your D MARKET team.",#body
        settings.EMAIL_HOST_USER,
        [email],
    )
    return redirect("weborphanage:Homepage")        

def Homepage(request):
    return render(request,"Orphanage/Homepage.html")

def Request(request):
    donation = db.collection("tbl_donationtype").stream()
    donation_data=[]
    for i in donation:
        donationdata=i.to_dict()
        ddata={"donation":donationdata,"id":i.id}
        donation_data.append(ddata)
    re = db.collection("tbl_request").where("orphnage_id", "==", request.session["opid"]).stream()
    result_data = []
    for r in re:
        rd = r.to_dict() 
        dtype = db.collection("tbl_donationtype").document(rd["donationtype_id"]).get().to_dict()
        result_data.append({"requests":r.to_dict(),"id":r.id,"dtype":dtype})

    if request.method=="POST":
        Title=request.POST.get("txt_title")
        Description=request.POST.get("txt_description")
        NumberofHead=request.POST.get("txt_head")
        Donationtype=request.POST.get("txt_donationtype")
        Amount=request.POST.get("txt_amount")
        data = {"title":Title,"description":Description,"numberofhead":NumberofHead,"donationtype_id":Donationtype,"amount":Amount,"orphnage_id":request.session["opid"],"request_date":str(date.today()),"status":0}
        db.collection("tbl_request").add(data)
        return redirect("weborphanage:Request")
    else:
        return render(request,"Orphanage/Request.html",{"donation_type":donation_data,"request":result_data})

def Complaint(request):
    complaint = db.collection("tbl_complaint").stream()
    complaint_data =[]
    for i in complaint:
        complaintdata = i.to_dict()
        cdata = {"complaint":complaintdata,"id":i.id}
        complaint_data.append(cdata)
    if request.method=="POST":
        Complaint=request.POST.get("txt_complaint")
        data = {"complaint_content":Complaint,"complaint_status":0,"complaint_reply":"","user_id":"","orphnage_id":request.session["opid"]}
        db.collection("tbl_complaint").add(data)
        return redirect('weborphanage:Homepage')
    else:
        return render(request,"Orphanage/Complaint.html",{"complaint":complaint_data})      


def Assigned_Donation(request):
    donation = db.collection("tbl_donation").where("orphnage_id", "==", request.session["opid"]).stream()
    donation_data=[]
    for i in donation:
        donationdata=i.to_dict()
        user = db.collection("tbl_userregistration").document(donationdata["user_id"]).get().to_dict()
        dtype = db.collection("tbl_donationtype").document(donationdata["donationtype_id"]).get().to_dict()
        ddata={"donation":donationdata,"id":i.id,"user":user,"dtype":dtype}
        donation_data.append(ddata)
    return render(request,"Orphanage/Assigned_Donation.html",{"donationdata":donation_data})

def View_Reply(request):
    viewreply = db.collection("tbl_complaint").where("orphnage_id", "==", request.session["opid"]).stream()
    viewreply_data=[]
    for i in viewreply:
        viewreplydata=i.to_dict()
        ddata={"viewreply":viewreplydata,"id":i.id}
        viewreply_data.append(ddata)
    return render(request,"Orphanage/View_Reply.html",{"viewreplydata":viewreply_data})        


def Feedback(request):
    feedback = db.collection("tbl_feedback").where("orphnage_id", "==", request.session["opid"]).stream()
    feedback_data=[]
    for i in feedback:
        feedbackdata=i.to_dict()
        fdata={"feedback":feedbackdata,"id":i.id}
        feedback_data.append(fdata)
    if request.method=="POST":
        Feedback=request.POST.get("txt_feedback")
        data = {'feedback':Feedback,"orphnage_id":request.session["opid"],"user_id":""}
        db.collection("tbl_feedback").add(data)
        return redirect("weborphanage:Homepage")
    else:
        return render(request,"Orphanage/Feedback.html",{"feedbackdata":feedback_data})        
