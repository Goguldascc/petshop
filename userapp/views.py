from django.shortcuts import render,redirect
from . models import reg_tbl,pro_tbl,cart_tbl
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings 
from.forms import regform


# Create your views here.

def index(request):
    return render(request,"index.html")
def about(req):
    return render(req,"about.html")
def service(r):
    return render(r,"service.html")
def price(price):
    return render(price,"price.html")
def booking(book):
    return render(book,"booking.html")
def contact(contact):
    return render(contact,"contact.html")
def blog(blo):
    return render(blo,"blog.html")
def reg(request):
    if request.method=='POST':
        fname = request.POST.get('fn')
        mobile =request.POST.get('mb')
        email = request.POST.get('em')
        passw =request.POST.get('ps')
        cpassw =request.POST.get('cps')
        obj=reg_tbl.objects.create(fn=fname,mb=mobile,em=email,ps=passw,cps=cpassw)
        obj.save()
        if obj:
            return render(request,"log.html")
        else:
            return render (request,"reg.html")
    else:
        return render(request,"reg.html")
def log (request):
    if request.method=='POST':
        email =request.POST.get('em')
        Passw =request.POST.get('pas')
        obj=reg_tbl.objects.filter(em=email,ps=Passw)
        if obj:
            request.session['ema']=email
            request.session['password1']=Passw
            for m in obj:
                idl=m.id
                request.session['idno']=idl
            return render(request,"home.html")
        else:
            msg="invaild  email and password"
            return render(request,"log.html",{"error":msg})
    
    return render(request,"log.html")
    
def details(request):
    obj=reg_tbl.objects.all()
    return render(request,"details.html",{"data":obj})

def edit(request):
    idno = request.GET.get('idn')
    obj = reg_tbl.objects.filter(id=idno)
    return render (request,"details2.html",{"data":obj}) 

def update (request):
    if request.method=="POST":
        fn = request.POST.get('un')
        idno= request.POST.get('idl')
        ema = request.POST.get('eml')
        mob= request.POST.get('mob')
        pasw= request.POST.get('psw')
        reg_tbl.objects.filter(id=idno).update(fn=fn,em=ema,mb=mob,ps=pasw)
        return redirect("/details")
    return render(request,"details2.html")
def upload (request):
    if request.method=='POST':
        pname = request.POST.get('fn')
        pimg= request.FILES.get('pi')
        price= request.POST.get('pr')
        dis=request.POST.get('ds')
        obj = pro_tbl.objects. create(pnm=pname,pim=pimg,prc=price,des=dis)
        obj.save()
        if obj:
            msg="Upload successful..."
            return render(request,"prodact.html",{"success":msg})
    return render(request,"prodact.html")
def cards (req):
    obj=pro_tbl.objects.all()
    return render(req,"cards.html",{"prodact":obj})
   
def cart (request,idn):
       cid = request.session['idno']
       cartcustomer = reg_tbl.objects.get(id=cid)
       cartproduct = pro_tbl.objects.get(id=idn)
       cartitem,created = cart_tbl.objects.get_or_create(customer=cartcustomer,product=cartproduct)
       if not created:
           cartitem.qty+=1
           cartitem.save()
           messages.success(request,"Item add to cart....")
       return redirect("/cards")

def viewcart(request):
    cid=request.session['idno']
    cobj =reg_tbl.objects.get(id=cid)
    cartobj =cart_tbl.objects.filter(customer=cobj)
    if cartobj:
        total_price =0
        for i in cartobj:
            pro =i.product.prc * i.qty
            total_price+=pro
        return render(request,"cart.html",{"total":total_price,"cart":cartobj})
    else:
        return render (request,"cart.html",{"msg":"cart is empty"})
        
def cartdelete(request,pid):
    obj =cart_tbl.objects.get(id=pid)
    obj.delete()
    return redirect('/viewcart')
def email(request):
    if request.method=='POST':
        to = request.POST.get('em')
        sub=request.POST.get('sub')
        msg =request.POST.get('msg')
        send_mail(sub,msg,settings.EMAIL_HOST_USER,[to],fail_silently=False)
        messages.success(request,"mail send successful....")
        return redirect('/email')
    return render(request,"email.html")
def e2(req):
    idno = req.GET.get('em')
    obj=reg_tbl.objects.filter(id=idno)
    return render(req,"email2.html",{"data":obj})

def regview(request):
    f=regform()
    if request.method=="POST":
        f=regform(request.POST)
        if f.is_valid():
         fname=f.cleaned_data.get('fn')
         mobile=f.cleaned_data.get('mb')
         email=f.cleaned_data.get('em')
         password=f.cleaned_data.get('ps')
         cpassword=f.cleaned_data.get('cps')
         obj=reg_tbl.objects.create(fn=fname,mb=mobile,em=email,ps=password,cps=cpassword)
         obj.save()
         if obj:
             msg="registretion successful...."
             return render(request,"regform.html",{'form':f,'success':msg})       
    
    return render(request,"regform.html",{'form':f})
    
    
