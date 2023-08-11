from django.shortcuts import render
from django.http import HttpResponse
from .models import Home_model,Service_model,Contact_model

# Create your views here.
def Home_view(request):
    home_data = Home_model.objects.first()
    return render(request, 'index.html', {'hero_data': home_data})


# def About_view(request):
#     about_data = About_model.objects.first()
#     context = {'content': about_data,}
#     return render(request, 'about.html', context)

def About_view(request):
    return render(request, 'about.html')

def Service_view(request):
    return render(request, 'service.html')

def Team_view(request):
    return render (request,'team.html')

from django.shortcuts import render, HttpResponse
from .models import Contact_model

def Contact_view(request):
    success_message = None
    error_message = None

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            # Create and save the Contact_model instance
            contact = Contact_model(name=name, email=email, subject=subject, message=message)
            contact.save()
            success_message = "Your message has been sent. Thank you!"
        else:
            error_message = "All fields are required."

    context = {
        'success_message': success_message,
        'error_message': error_message
    }

    return render(request, 'contact.html', context)

# def Service_view(request):
#     service_data = Service_model.objects.all()
#     context = {'service_data': service_data}
#     return render(request, 'service.html', context)


# def Why_choose_us_view(request):
#     wcu_data = Why_choose_us.objects.all()
#     return render(request, 'why_choose_us.html',{'wcu_data': wcu_data})