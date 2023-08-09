from django.contrib import admin
from .models import About_model,Why_choose_us_model,About_List_Item,Home_model,Service_model
# Register your models here.
#index Section
admin.site.register(Home_model)

#About Section
admin.site.register(About_model)
admin.site.register(About_List_Item)

#Why_choose_us Section
admin.site.register(Why_choose_us_model)

#Service Section
admin.site.register(Service_model)
