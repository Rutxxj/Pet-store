from django.contrib import admin
from .models import Pet,Cart

# Register your models here.
class PetAdmin(admin.ModelAdmin):
    list_display=['id','name','category','price']

admin.site.register(Pet,PetAdmin)
admin.site.register(Cart)
