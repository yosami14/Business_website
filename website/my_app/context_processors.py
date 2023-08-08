from my_app.models import Why_choose_us_model

def why_choose_us_cp(request):
    why_choose_us_data = Why_choose_us_model.objects.all() 
    return {'why_choose_us_cp': why_choose_us_data}



