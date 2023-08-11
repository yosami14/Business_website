from django.contrib import admin
from .models import About_model,Why_choose_us_model,About_List_Item,Home_model,Service_model,Team_model,Footer_model,Contact_model,Contact_info_model
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

#Team Section
admin.site.register(Team_model)

#Footer Section
admin.site.register(Footer_model)

#contact_info Section
admin.site.register(Contact_info_model)

#Contact Section
admin.site.register(Contact_model)
