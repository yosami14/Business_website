from my_app.models import Why_choose_us_model,About_model,Service_model

def why_choose_us_cp(request):
    why_choose_us_data = Why_choose_us_model.objects.all() 
    return {'why_choose_us_cp': why_choose_us_data}

def About_cp(request):
    About_data = About_model.objects.first()
    return {'About_cp': About_data}

# Service
def service_cp(request):
    service_data = Service_model.objects.all()
    return {'service_cp': service_data}


