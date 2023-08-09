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
            user_name,
            user_message,
            user_email
            ['temitopeayobami995@gmail.com'],
            
        )
        
        return render(request, 'apps/contact.html', {'user_name':user_name})
    else:
        return render(request, 'apps/contact.html', {})
        
