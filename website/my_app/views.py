from django.shortcuts import render
from .models import Home_model,Service_model,Contact_model

# Home_view
def Home_view(request):
    home_data = Home_model.objects.first()
    return render(request, 'index.html', {'hero_data': home_data})

# About_view
def About_view(request):
    return render(request, 'about.html')

# Service_view
def Service_view(request):
    return render(request, 'service.html')

# Team_view
def Team_view(request):
    return render (request,'team.html')

# Contact_view
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
        'error_message': error_message,

    }

    return render(request, 'contact.html', context)

