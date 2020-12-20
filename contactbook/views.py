from django.shortcuts import render,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Contact
from django.contrib import messages
from .forms import contactbookForm
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html')

def dashboard(request):
    
    contacts = Contact.objects.filter(user_id=request.user)
    context={'contacts':contacts}
    return render(request,'dashboard.html',context)
    # return redirect('home')
    

def addcontact(request):
    if request.method=='POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        contact = Contact(first_name=fname,last_name=lname,email=email,user_id=request.user)
        contact.save()
        messages.success(request,f'Contact {fname} has been saved')
        return redirect('addcontact')
    
    return render(request,'addcontact.html')

def update(request,myid):
    contact = Contact.objects.filter(sno = myid)[0]
    form = contactbookForm(instance=contact)
    if request.method=='POST':
        form = contactbookForm(request.POST,instance=contact)
        if form.is_valid():
            form.save()
              
        return redirect('dashboard')
    context={'form':form}
    
    return render(request,'update.html',context)
   
def detail_delete(request,id):
    object = Contact.objects.filter(sno=id) 
    context={'object':object}
    return render(request,'delete.html',{'object':object})


def confirm_delete(request,id):
    object = Contact.objects.filter(sno=id)
    object.delete() 
    messages.success(request,f'Contact has been deleted')
    return redirect('dashboard')


def search(request):
    search = request.GET.get('search',"")
    object1 = Contact.objects.filter(first_name__icontains=search,user_id=request.user)
    object2 = Contact.objects.filter(last_name__icontains=search,user_id=request.user)
    object3 = Contact.objects.filter(email__icontains=search,user_id=request.user)
    all=object1.union(object2.union(object3)).order_by('sno')
    
    paginator = Paginator(all,10)
    
    page_number = request.GET.get('page',1)
    
    page_obj = paginator.get_page(page_number)

    if len(all)<1:
        messages.error(request,f'Search results for {search} not found' )
    else:
        
        messages.success(request,f'Search results for {search}')
    param = {'page_obj':page_obj}

    return render(request,'search.html',param)
    

    
def handleSignup(request):
    if request.method=='POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
       
        if password1!=password2:
            messages.error(request,'Password not matched')
            return redirect("home")
        

        myuser = User.objects.create_user(fname,email,password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,'your account has been created')
        return redirect('home')

    else:
        return HttpResponse("404 not found")

def handleLogin(request):
    if request.method=="POST":
        loginname = request.POST['login-name']
        lpassword = request.POST['login-password']
        user = authenticate(username=loginname , password=lpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"You are logged in successfully")
            return redirect('dashboard')
        else:
            messages.error(request,'Sorry crediential not match ,please try again!!!')
            return redirect('home')
    else:
        return HttpResponse("404 not found")

def handleLogout(request):
    logout(request)
    messages.success(request,'You are logged out successfully')
    return redirect('home')