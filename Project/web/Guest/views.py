from django.shortcuts import render,redirect
import firebase_admin
from firebase_admin import firestore,credentials,storage,auth
import pyrebase
db = firestore.client()
# Create your views here.

config = {
  "apiKey": "AIzaSyC2UcoK1NsZZINSpTkU6fShSRirUF1NqMA",
  "authDomain": "orphanage-6412e.firebaseapp.com",
  "projectId": "orphanage-6412e",
  "storageBucket": "orphanage-6412e.appspot.com",
  "messagingSenderId": "919245946536",
  "appId": "1:919245946536:web:13759302d0d84263fecc9d",
  "measurementId": "G-ZH2T9M1K5M",
  "databaseURL": ""
}

firebase = pyrebase.initialize_app(config)
st = firebase.storage()
authe = firebase.auth()

def User_Registration(request):

      dist = db.collection("tbl_district").stream()
      dist_data=[]
      for i in dist:
        dist_data.append({"dist":i.to_dict(),"id":i.id})
      if request.method=="POST":
        Useremail=(request.POST.get("txt_email"))
        Password=(request.POST.get("txt_pass"))
        try:
          user = firebase_admin.auth.create_user(email=Useremail,password=Password)
        except (firebase_admin._auth_utils.EmailAlreadyExistsError,ValueError) as error:
          return render(request,"Guest/User_Registration.html",{"msg":error})

        Photo=request.FILES.get("txt_photo")
        if Photo:
          path ="User_photo/" + Photo.name
          st.child(path).put(Photo)
          d_url = st.child(path).get_url(None)
        Proof=request.FILES.get("txt_proof")
        if Proof:
          path ="User_proof/" + Proof.name
          st.child(path).put(Proof)
          dwn_url = st.child(path).get_url(None)
        data = {"User_id":user.uid,"user_name":request.POST.get("txt_name"),"user_email":request.POST.get("txt_email"),"user_contact":request.POST.get("txt_contact"),"user_address":request.POST.get("txt_address"),"place_id":request.POST.get("sel_place"),"user_photo":d_url,"user_proof":dwn_url}
        db.collection("tbl_userregistration").add(data)   

        return render(request,"Guest/User_Registration.html",{"msg":"Account Created.."})
      else:
        return render(request,"Guest/User_Registration.html",{'dist':dist_data})

def Orphanage_Registration(request):
  dist = db.collection("tbl_district").stream()
  dist_data=[]
  for i in dist:
    dist_data.append({"dist":i.to_dict(),"id":i.id})
  if request.method=="POST":
        
        Orphanageemail=(request.POST.get("txt_email"))
        Password=(request.POST.get("txt_password"))
        try:
          orphanage = firebase_admin.auth.create_user(email=Orphanageemail,password=Password)
        except (firebase_admin._auth_utils.EmailAlreadyExistsError,ValueError) as error:
          return render(request,"Guest/Orphanage_Registration.html",{"msg":error})
        Photo=request.FILES.get("txt_photo")
        if Photo:
          path ="Orphanage_photo/" + Photo.name
          st.child(path).put(Photo)
          d_url = st.child(path).get_url(None)
        data = {"Orphanage_id":orphanage.uid,"orphanage_name":request.POST.get("txt_name"),"orphanage_contact":request.POST.get("txt_contact"),"orphanage_email":request.POST.get("txt_email"),"orphanage_address":request.POST.get("txt_address"),"place_id":request.POST.get("sel_place"),"orphanage_photo":d_url,"orphanage_count":request.POST.get("txt_count"),"orphanage_status":0}
        db.collection("tbl_orphanageregistration").add(data) 


        return render(request,"Guest/Orphanage_Registration.html",)
  else:
        return render(request,"Guest/Orphanage_Registration.html",{'dist':dist_data})

def Login(request):
  us_id = ""
  op_id = ""
  if request.method=="POST":
      Email=request.POST.get("txt_email")
      Password=request.POST.get("txt_password")

     
      try:
        data = authe.sign_in_with_email_and_password(Email,Password)
        print(data)

      except:
        return render(request,"Guest/Login.html",{"msg":"error in Email or Password"})
      data_id = data["localId"]
      user = db.collection("tbl_userregistration").where("User_id", "==", data_id).stream()
      for u in user:
        us_id = u.id
      orphanage = db.collection("tbl_orphanageregistration").where("Orphanage_id", "==", data_id).where("orphanage_status", "==", 1).stream()
      for o in orphanage:
        op_id = o.id
      
    
      if us_id:
        request.session["usid"] = us_id
        return redirect("webuser:Homepage")
      elif op_id:
        request.session["opid"] =op_id
        return redirect("weborphanage:Homepage")
      else:
        return render(request,"Guest/Login.html",{"msg":"Error"})
  
  else:
    return render(request,"Guest/Login.html")        

def ajaxplace(request):
    place = db.collection("tbl_place").where("District_id", "==", request.GET.get("disid")).stream()
    place_data = []
    for i in place:
        place_data.append({"place":i.to_dict(),"id":i.id})
    return render(request,"Guest/Ajaxplace.html",{"place":place_data})

def index(request):
  return render(request,"Guest/index.html")
