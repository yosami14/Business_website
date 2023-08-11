from my_app.models import Why_choose_us_model,About_model,Service_model,Team_model,Footer_model,Contact_info_model
# Why choose us
def why_choose_us_cp(request):
    why_choose_us_data = Why_choose_us_model.objects.all() 
    return {'why_choose_us_cp': why_choose_us_data}

# About
def About_cp(request):
    About_data = About_model.objects.first()
    return {'About_cp': About_data}

# Service
def service_cp(request):
    service_data = Service_model.objects.all()
    return {'service_cp': service_data}

# Team
def team_cp(request):
    team_data = Team_model.objects.all()
    return {'team_cp': team_data}

# Footer
def footer_cp(request):
    footer_data = Footer_model.objects.first()
    return {'footer_cp': footer_data}

# contact_info
def Contact_info_cp(request):
    Contact_info_cp = Contact_info_model.objects.first()
    return {'Contact_info_cp': Contact_info_cp}



