from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'apps/home.html', {})


def contact(request):
    if request.method == "POST":
        user_name = request.POST['user_name']
        user_email = request.POST['user_email']
        user_message = request.POST['user_message']
        
        send_mail(
            'message from ' + user_name, #Subject
            user_message, # message
            #subject, # subject
            user_email, # from email
           ['temitopeayobami995@gmail.com'], # to email
        )
            
        
        
        return render(request, 'apps/contact.html', {'user_name':user_name})
    else:
        return render(request, 'apps/contact.html', {})
    
def about(request):
    return render(request, 'apps/about.html', {})

def trainer(request):
    return render(request, 'apps/trainer.html', {})

def courses(request):
    return render(request, 'apps/courses.html', {})

def service(request):
    return render(request, 'apps/service.html', {})
        
