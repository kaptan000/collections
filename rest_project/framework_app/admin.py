from django.contrib import admin
from .models import Employee,Singer,Song


# Register your models here.
class SingerModelAdmin(admin.ModelAdmin):
    list_display=['full_name','gender']

class SongModelAdmin(admin.ModelAdmin):
    list_display=['title','duration']    

admin.site.register(Employee)
admin.site.register(Singer,SingerModelAdmin)
admin.site.register(Song,SongModelAdmin)
