from django.shortcuts import render
from .models import Home_model,Service_model

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



# def Service_view(request):
#     service_data = Service_model.objects.all()
#     context = {'service_data': service_data}
#     return render(request, 'service.html', context)


# def Why_choose_us_view(request):
#     wcu_data = Why_choose_us.objects.all()
#     return render(request, 'why_choose_us.html',{'wcu_data': wcu_data})