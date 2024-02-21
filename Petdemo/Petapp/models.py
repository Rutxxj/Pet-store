from django.db import models

# Create your models here.
#custom manager
class CustomManager(models.Manager):
     def get_price_range(self,r1,r2):
         return self.filter(price__range=(r1,r2))
     
     def cat_list(self):
          return self.filter(category__exact="Cat")
     def dog_list(self):
          return self.filter(category__exact="Dog")
     def fish_list(self):
          return self.filter(category__exact="Fish")
     def bird_list(self):
          return self.filter(category__exact="Bird")
     def tortoise_list(self):
          return self.filter(category__exact="Tortoise")



class Pet(models.Model):
     id=models.IntegerField(primary_key=True)
     name=models.CharField(max_length=50)
     description = models.CharField(max_length=255,default='null')
     category_choices=(("Cat","Cat"),("Dog","Dog"),("Bird","Bird"),("Fish","Fish"),("Tortoise","Tortoise"))
     category=models.CharField(max_length=50,choices=category_choices, default="watch")
     image=models.ImageField(upload_to="images/", height_field=None, width_field=None, max_length=None)
     price=models.IntegerField()

     prod = CustomManager()
     objects=models.Manager()

class Cart(models.Model):
     pet = models.ForeignKey(Pet,on_delete=models.CASCADE)
     quantity= models.PositiveIntegerField(default=0)
     date_added=models.DateTimeField(auto_now_add=True)   



