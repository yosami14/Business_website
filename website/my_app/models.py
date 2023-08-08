from django.db import models
from ckeditor.fields import RichTextField


#Hero 
class Home_model(models.Model):
    title = models.CharField(max_length=200) 
    description = models.CharField(max_length=200)
    button_vid = models.CharField(max_length=200,blank=True) 
    image = models.ImageField(blank=True,null=True,upload_to='hero/')

    def __str__(self):
        return self.title



#ABOUT
class About_List_Item(models.Model):
    content = models.CharField(max_length=200)
    about = models.ForeignKey('About_model', on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class About_model(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    image = models.ImageField(blank=True, null=True, upload_to='about/')
    list_items = models.ManyToManyField(About_List_Item, blank=True)

    def __str__(self):
        return self.title


#WHY CHOOSE US
class Why_choose_us_model(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField(blank=True)
    sub_description = RichTextField(blank=True)
    def __str__(self):
      return self.title
    
# Our Service

class Our_service_model(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField(blank=True)
    sub_description = RichTextField(blank=True)
    def __str__(self):
      return self.title