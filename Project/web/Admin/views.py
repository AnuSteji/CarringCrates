from django.shortcuts import render,redirect
import firebase_admin
from firebase_admin import firestore,credentials,storage,auth
import pyrebase


db = firestore.client()


# Create your views here.
def Homepage(request):
    new = db.collection("tbl_orphanageregistration").where("orphanage_status", "==", 1).stream()
    new_data=[]
    for i in new:
        newdata=i.to_dict()
        place = db.collection("tbl_place").document(newdata["place_id"]).get().to_dict()
        District= db.collection("tbl_district").document(place["District_id"]).get().to_dict()
        ddata={"new":newdata,"id":i.id,"district":District,"place":place}
        new_data.append(ddata)
    return render(request,"Admin/Homepage.html",{'orphanage':new_data})

def District(request):
    dist = db.collection("tbl_district").stream()
    dist_data=[]
    for i in dist:
        distdata=i.to_dict()
        ddata={"dist":distdata,"id":i.id}
        dist_data.append(ddata)
    if request.method=="POST":
        District=request.POST.get("txt_dis")
        data = {'district_name':District}
        db.collection("tbl_district").add(data)
        return render(request,"Admin/District.html",{'District':District})
    else:
        return render(request,"Admin/District.html",{"distdata":dist_data})

def delete_dist(request,id):
       db.collection("tbl_district").document(id).delete()
       return redirect("webadmin:District")

def edit_dist(request,id):
    dist=db.collection("tbl_district").document(id).get().to_dict()
    if request.method == "POST":
        District=request.POST.get("txt_dis")
        data =  {"district_name":District} 
        db.collection("tbl_district").document(id).update(data)
        return redirect("webadmin:District")
    else:
        return render(request,"Admin/District.html",{"dist":dist})            

def Donationtype(request):
    donation = db.collection("tbl_donationtype").stream()
    donation_data=[]
    for i in donation:
        donationdata=i.to_dict()
        ddata={"donation":donationdata,"id":i.id}
        donation_data.append(ddata)
    if request.method=="POST":
        data = {'donationtype_name':request.POST.get("txt_name")}
        db.collection("tbl_donationtype").add(data)
        return render(request,"Admin/Donationtype.html",{'Donationtype':Donationtype})
    else:
        return render(request,"Admin/Donationtype.html",{"donationdata":donation_data})

def delete_donation(request,id):
       db.collection("tbl_donationtype").document(id).delete()
       return redirect("webadmin:Donationtype")  

def edit_donation(request,id):
    donation=db.collection("tbl_donationtype").document(id).get().to_dict()
    if request.method == "POST":
        DonationtypeName=request.POST.get("txt_name")
        data =  {"donationtype_name":DonationtypeName} 
        db.collection("tbl_donationtype").document(id).update(data)
        return redirect("webadmin:Donationtype")
    else:
        return render(request,"Admin/Donationtype.html",{"donation":donation})                   

def Admin_Registration(request):
    if request.method=="POST":
        AdminName=request.POST.get("txt_name")
        AdminEmail=request.POST.get("txt_email")
        AdminContact=request.POST.get("txt_contact")
        Adminpassword=request.POST.get("txt_pass")
        try:
          admin = firebase_admin.auth.create_user(email=AdminEmail,password=Adminpassword)
        except (firebase_admin._auth_utils.EmailAlreadyExistsError,ValueError) as error:
          return render(request,"Admin/Admin_Registration.htm",{"msg":error})
        db.collection("tbl_admin").add({"admin_name":AdminName,"admin_email":AdminEmail,"admin_contact":AdminContact,"admin_id":admin.uid})
        return render(request,"Admin/Admin_Registration.html",{'msg':"Account Created"})
    else:
        return render(request,"Admin/Admin_Registration.html")


def Place(request):
    dist = db.collection("tbl_district").stream()
    dist_data=[]
    
    for i in dist:
        dist_data.append({"dist":i.to_dict(),"id":i.id})
    place = db.collection("tbl_place").stream()
    place_data=[]
    for i in place: 
        place_list=i.to_dict()
        dist=place_list["District_id"]
        distri=db.collection("tbl_district").document(dist).get()
        District=distri.to_dict()
        place_data.append({"place":place_list,"id":i.id,"distri_data":District})
    if request.method=="POST":
        District=(request.POST.get("district"))
        PlaceName=(request.POST.get("txt_placename"))
        data = {"Place_name":PlaceName,"District_id":District}
        db.collection("tbl_place").add(data)
        return render(request,"Admin/Place.html",{'District':District,'Place':Place})
    else:
        return render(request,"Admin/Place.html",{"dist":dist_data,"Place":place_data})

def delete_place(request,id):
    db.collection("tbl_place").document(id).delete()
    return redirect("webadmin:Place")
       
def edit_place(request,id):
    dist = db.collection("tbl_district").stream()
    dist_data=[]
    
    for i in dist:
        dist_data.append({"dist":i.to_dict(),"id":i.id})
    place=db.collection("tbl_place").document(id).get().to_dict()
    if request.method == "POST":
        District=(request.POST.get("district"))
        PlaceName=(request.POST.get("txt_placename"))
        data = {"Place_name":PlaceName,"District_id":District}
        db.collection("tbl_place").document(id).update(data)
        return redirect("webadmin:Place")
    else:
        return render(request,"Admin/Place.html",{"Placedata":place,"dist":dist_data})                   


def NewOrphanage(request):
    new = db.collection("tbl_orphanageregistration").where("orphanage_status", "==", 0).stream()
    new_data=[]
    for i in new:
        newdata=i.to_dict()
        place = db.collection("tbl_place").document(newdata["place_id"]).get().to_dict()
        District= db.collection("tbl_district").document(place["District_id"]).get().to_dict()
        ddata={"new":newdata,"id":i.id,"district":District,"place":place}
        new_data.append(ddata)
    return render(request,"Admin/NewOrphanage.html",{'orphanage':new_data})

def accept_orphanage(request,id):
    orphanage =db.collection("tbl_orphanageregistration").document(id).get().to_dict()
    data =  {"orphanage_status":1} 
    db.collection("tbl_orphanageregistration").document(id).update(data)
    return redirect("webadmin:Homepage") 

def reject_orphanage(request,id):
    orphanage =db.collection("tbl_orphanageregistration").document(id).get().to_dict()
    data =  {"orphanage_status":2} 
    db.collection("tbl_orphanageregistration").document(id).update(data)
    return redirect("webadmin:Homepage")  

def Accepted_Orphanage(request):
    accorph = db.collection("tbl_orphanageregistration").where("orphanage_status", "==", 1).stream()
    accorph_data=[]
    for i in accorph:
        accorphdata=i.to_dict()
        place = db.collection("tbl_place").document(accorphdata["place_id"]).get().to_dict()
        District= db.collection("tbl_district").document(place["District_id"]).get().to_dict()
        adata={"accorph":accorphdata,"id":i.id,"district":District,"place":place}
        accorph_data.append(adata)
    return render(request,"Admin/Accepted_Orphanage.html",{"accorphdata":accorph_data})


def Rejected_Orphanage(request):
    rejorph = db.collection("tbl_orphanageregistration").where("orphanage_status", "==", 2).stream()
    rejorph_data=[]
    for i in rejorph:
        rejorphdata=i.to_dict()
        place = db.collection("tbl_place").document(rejorphdata["place_id"]).get().to_dict()
        District= db.collection("tbl_district").document(place["District_id"]).get().to_dict()
        rdata={"rejorph":rejorphdata,"id":i.id,"district":District,"place":place}
        rejorph_data.append(rdata)
    return render(request,"Admin/Rejected_Orphanage.html",{"rejorphdata":rejorph_data})        

def Orphanagerequest(request):
    orphreq = db.collection("tbl_request").where("status", "==", 0).stream()
    orphreq_data=[]
    for i in orphreq:
        orphreqdata=i.to_dict()
        odata={"orphreq":orphreqdata,"id":i.id}
        orphreq_data.append(odata)
    return render(request,"Admin/Orphanagerequest.html",{"orphreqdata":orphreq_data})      

def accept_orphanagerequest(request,id):
    orphreq =db.collection("tbl_request").document(id).get().to_dict()
    data =  {"status":1} 
    db.collection("tbl_request").document(id).update(data)
    return redirect("webadmin:Homepage")  

def reject_orphanagerequest(request,id):
    orphreq =db.collection("tbl_request").document(id).get().to_dict()
    data =  {"status":2} 
    db.collection("tbl_request").document(id).update(data)
    return redirect("webadmin:Homepage")    

def accepted_orrequest(request):
    orphreq = db.collection("tbl_request").where("status", "==", 1).stream()
    orphreq_data=[]
    for i in orphreq:
        orphreqdata=i.to_dict()
        odata={"orphreq":orphreqdata,"id":i.id}
        orphreq_data.append(odata)
    return render(request,"Admin/Accepted_Orphanage_Request.html",{"orphreqdata":orphreq_data})

def rejected_orrequest(request):
    orphreq = db.collection("tbl_request").where("status", "==", 2).stream()
    orphreq_data=[]
    for i in orphreq:
        orphreqdata=i.to_dict()
        odata={"orphreq":orphreqdata,"id":i.id}
        orphreq_data.append(odata)
    return render(request,"Admin/Rejected_Orphanage_Request.html",{"orphreqdata":orphreq_data})

def View_User_Donation(request):
    donation = db.collection("tbl_donation").where("donation_status", "==", 0).stream()
    donation_data=[]
    for i in donation:
        donationdata=i.to_dict()
        user = db.collection("tbl_userregistration").document(donationdata["user_id"]).get().to_dict()
        dot = db.collection("tbl_donationtype").document(donationdata["donationtype_id"]).get().to_dict()
        ddata={"donation":donationdata,"id":i.id,"user":user,"dot":dot}
        donation_data.append(ddata)
    return render(request,"Admin/View_User_Donation.html",{"donationdata":donation_data})

def Assign_User_Request(request,id):
    orphnage = db.collection("tbl_orphanageregistration").stream()
    or_data = []
    for i in orphnage:
        or_data.append({"or":i.to_dict(),"id":i.id})
    ur = db.collection("tbl_donation").document(id).get().to_dict()
    dontype = db.collection("tbl_donationtype").document(ur["donationtype_id"]).get().to_dict()
    user = db.collection("tbl_userregistration").document(ur["user_id"]).get().to_dict()
    if request.method == "POST":
        db.collection("tbl_donation").document(id).update({"donation_status":1,"orphnage_id":request.POST.get("txt_donationtype")})
        return render(request,"Admin/View_User_Donation.html",{"msg":"Request Assigned"})
    else:
        return render(request,"Admin/Assign_User_Request.html",{"user_donation":ur,"dtype":dontype,"user":user,"or":or_data})                 

def Assigned_Request(request):
    assigned = db.collection("tbl_donation").where("donation_status", "==", 1).stream()
    assigned_data=[]
    for i in assigned:
        assigneddata=i.to_dict()
        user = db.collection("tbl_userregistration").document(assigneddata["user_id"]).get().to_dict()
        dtype = db.collection("tbl_donationtype").document(assigneddata["donationtype_id"]).get().to_dict()
        orph = db.collection("tbl_orphanageregistration").document(assigneddata["orphnage_id"]).get().to_dict()
        cdata={"assigned":assigneddata,"id":i.id,"user":user,"dtype":dtype,"orph":orph}
        assigned_data.append(cdata)
    return render(request,"Admin/Assigned_Request.html",{"assigneddata":assigned_data})

def feedback(request):
    userfeed = db.collection("tbl_feedback").where("user_id", "!=", "").stream()
    ufeed_data = []
    for uf in userfeed:
        u = uf.to_dict()
        user = db.collection("tbl_userregistration").document(u["user_id"]).get().to_dict()
        ufeed_data.append({"feedback":uf.to_dict,"id":uf.id,"user":user})

    orfeed = db.collection("tbl_feedback").where("orphnage_id", "!=", "").stream()
    ofeed_data = []
    for of in orfeed:
        o = of.to_dict()
        orph = db.collection("tbl_orphanageregistration").document(o["orphnage_id"]).get().to_dict()
        ofeed_data.append({"feedback":of.to_dict,"id":of.id,"orph":orph})
    return render(request,"Admin/View_feedback.html",{"user_feed":ufeed_data,"or_feed":ofeed_data})

def complaint(request):
    userc = db.collection("tbl_complaint").where("user_id", "!=", "").where("complaint_status", "==", 0 ).stream()
    userc_data = []
    for uc in userc:
        udata = uc.to_dict()
        user = db.collection("tbl_userregistration").document(udata["user_id"]).get().to_dict()
        userc_data.append({"usercomplaint":uc.to_dict(),"id":uc.id,"user":user})
    orphc = db.collection("tbl_complaint").where("orphnage_id", "!=", "").where("complaint_status", "==", 0 ).stream()
    orph_data = []
    for oc in orphc:
        udata = oc.to_dict()
        orph = db.collection("tbl_orphanageregistration").document(udata["orphnage_id"]).get().to_dict()
        orph_data.append({"orphcomplaint":oc.to_dict(),"id":oc.id,"orph":orph})
    return render(request,"Admin/View_Complaints.html",{"user_com":userc_data,"orph":orph_data})

def reply(request,id):
    if request.method == "POST":
        db.collection("tbl_complaint").document(id).update({"complaint_status":1,"complaint_reply":request.POST.get("txt_reply")})
        return render(request,"Admin/View_Complaints.html",{"msg":"Reply Sented sucessfully.."})
    else:
        return render(request,"Admin/Reply.html")

def replyed_complaint(request):
    userc = db.collection("tbl_complaint").where("user_id", "!=", "").where("complaint_status", "==", 1 ).stream()
    userc_data = []
    for uc in userc:
        udata = uc.to_dict()
        user = db.collection("tbl_userregistration").document(udata["user_id"]).get().to_dict()
        userc_data.append({"usercomplaint":uc.to_dict(),"id":uc.id,"user":user})
    orphc = db.collection("tbl_complaint").where("orphnage_id", "!=", "").where("complaint_status", "==", 1 ).stream()
    orph_data = []
    for oc in orphc:
        udata = oc.to_dict()
        orph = db.collection("tbl_orphanageregistration").document(udata["orphnage_id"]).get().to_dict()
        orph_data.append({"orphcomplaint":oc.to_dict(),"id":oc.id,"orph":orph})
    return render(request,"Admin/Replyed_Complaint.html",{"user_com":userc_data,"orph":orph_data})
