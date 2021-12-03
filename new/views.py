from django.shortcuts import redirect, render
from .forms import Registration_form
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Register
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    
    return render(request,'new/home.html')

@login_required(login_url='login')
def Registered(request):
    form=Registration_form()

    if request.method =='POST':
        if request.POST.get('submit')=='Login':
            mail=request.POST.get('mail')
            word = request.POST.get('word')
            print(mail)
            try:
               
                user=Register.objects.get(email=mail)
                if user is not None:
                # login(request,user)
                    
                    messages.success(request,'successfully loged-in')
                

            except:
                messages.error(request,'user not exist')
            user=authenticate(request,email=mail,password=word)
             
        elif request.POST.get('submit')=='Register':
            
            email=request.POST.get('email')
            password=request.POST.get('password')
            number=request.POST.get('number')
            form=Register(email=email,password=password,mobile=number)
            # form=Registration_form(request.POST)
            print(request.POST)
            try:

                print('valid')
                
                form.save()
        
                messages.success(request,'successfully signin')
                

            except:
                print('not valid')
                messages.error(request,'please check your detailes')
                
        
    return render(request,'new/login_page.html',{'form':form})
