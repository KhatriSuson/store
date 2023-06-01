from django.http import HttpResponse
from django.shortcuts import render
from .models import product
from .models import customer

# Create your views here.


def index(request):
    prd = product.objects.all()
    print(prd)
    params = {'products': prd}
    return render(request, 'store/index.html', params)


def signup(request):
    if request.method == 'GET':
        return render(request, 'store/signup.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        error_message = None
        # text validation in django
        if(not email):
            error_message = "Email is required!"
            params = {'error1':error_message}
            return render(request, 'store/signup.html',{'error1':error_message}) 
        elif(not password):
             error_message = "password is required!"
             return render(request, 'store/signup.html',{'error2':error_message}) 

        

        elif len(password)<8:
            error_message = "Password should be 8 characters!"
            params = {'error2':error_message}
            return render(request, 'store/signup.html',{'error2':error_message}) 

        # saving
        if not error_message:
                
            customer1 = customer(email=email, password=password)
            customer1.save()
            params = {'signup':'signup is successfull'}
            return render(request,'store/index.html',params)
           
            
        else:
            return render(request, 'store/signup.html',{'error':error_message})  
        
    
    



