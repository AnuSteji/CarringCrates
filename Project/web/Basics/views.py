from django.shortcuts import render

# Create your views here.
def sum(request):
    if request.method=="POST":
        num1=int(request.POST.get("txt_number 1"))
        num2=int(request.POST.get("txt_number 2"))
        result=num1+num2
        return render(request,"Basics/Sum.html",{'result':sum})
    else:
        return render(request,"Basics/Sum.html")

def Calculator(request):
    if request.method=="POST":
        num1=int(request.POST.get("txt_number 1"))
        num2=int(request.POST.get("txt_number 2"))
        if request.POST.get("btn_res") == "sum":
            result=num1+num2
            return render(request,"Basics/Calculator.html",{'value':result})
        elif request.POST.get("btn_res") == "div":
            result=num1/num2
            return render(request,"Basics/Calculator.html",{'value':result})
        elif request.POST.get("btn_res") == "mul":
            result=num1*num2
            return render(request,"Basics/Calculator.html",{'value':result})
        elif request.POST.get("btn_res") == "diff":
            result=num1-num2
            return render(request,"Basics/Calculator.html",{'value':result})
    else:
        return render(request,"Basics/Calculator.html")

        
def Largest(request):
    if request.method=="POST":
        num1=int(request.POST.get("txt_number 1"))
        num2=int(request.POST.get("txt_number 2"))
        if num1>num2:
            Largest=num1
            return render(request,"Basics/Largest.html",{'result':Largest})
        else:
            Largest=num2
            return render(request,"Basics/Largest.html",{'result':Largest})
    else:
        return render(request,"Basics/Largest.html")

def Marksheet(request):
    if request.method=="POST":
        name=request.POST.get("txt_name")
        department=request.POST.get("dept")
        year=request.POST.get("txt_year")
        mark1=int(request.POST.get("txt_mark1"))
        mark2=int(request.POST.get("txt_mark2"))
        mark3=int(request.POST.get("txt_mark3"))
        TotalMark=mark1+mark2+mark3
        Average=TotalMark/3
        if Average>90:
            grade='A+'
        elif Average>80 and Average<=90:
            grade='A'
        elif Average>70 and Average<=80:
            grade='B+'
        elif Average>60 and Average<=70:
            grade='B' 
        elif Average>50 and Average<=60:
            grade='c+'
        elif Average>40 and Average<=50:
            grade='C' 
        else:
            Average<40
            grade='FAILED'
        return render(request,"Basics/Marksheet.html",{'Name':name,'Department':department,'Year':year,'Mark1':mark1,'Mark2':mark2,'Mark3':mark3,'TotalMark':TotalMark,'Average':Average,'grade':grade})
    else:
        return render(request,"Basics/Marksheet.html")  


def BasicSalary(request):
    if request.method=="POST":
        Firstname=request.POST.get("txt_firstname")
        Lastname=request.POST.get("txt_lastname")
        name=Firstname+Lastname
        Gender=request.POST.get("gender")
        Martial=request.POST.get("martial")
        Department=request.POST.get("dept")
        Basicsalary=int(request.POST.get("txt_basicsalary"))
        if Gender=='Female'and Martial=='Single':
            name="Miss."+name
        elif Gender=='Female'and Martial=='Married':
            name="Mrs."+name
        else:
            name="Mr."+name
        if Basicsalary>=10000:
            TA=0.4*Basicsalary
            DA=0.35*Basicsalary
            HRA=0.3*Basicsalary
            LIC=0.25*Basicsalary
            PF=0.2*Basicsalary
        elif Basicsalary>=500 and Basicsalary<10000:
            TA=0.35*Basicsalary
            DA=0.3*Basicsalary
            HRA=0.25*BasicSalary
            LIC=0.2*Basicsalary
            PF=0.15*Basicsalary
        elif Basicsalary<5000:
            TA=0.3*Basicsalary
            DA=0.25*Basicsalary
            HRA=0.2*BasicSalary
            LIC=0.15*Basicsalary
            PF=0.10*Basicsalary
        else:
            TA=INVALID
            DA=INVALID
            HRA=INVALID
            LIC=INVALID
            PF=INVALID
        DEDUCTION=LIC+PF
        NETAMOUNT=Basicsalary+TA+DA+HRA-(LIC+PF)    
        return render(request,"Basics/BasicSalary.html",{'name':name,'Gender':Gender,'Martial':Martial,'Department':Department,'Basicsalary':Basicsalary,'TA':TA,'DA':DA,'HRA':HRA,'LIC':LIC,'PF':PF,'DEDUCTION':DEDUCTION,'NETAMOUNT':NETAMOUNT})
    else:
        return render(request,"Basics/BasicSalary.html")
       