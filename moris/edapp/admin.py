from django.contrib import admin

# Register your models here.
from . models import article,about_us,testimonials,query,course,videos,blogs



class articleadmin(admin.ModelAdmin):
    list_display =['title','written_by','subtitle']
    list_filter = ['written_by']

class testimonialsadmin(admin.ModelAdmin):
    list_display =['title','content','by_name','by_place']
    list_filter = ['by_name']

class queryadmin(admin.ModelAdmin):
    list_display =['name','email','message','phno']

class videosadmin(admin.ModelAdmin):
    list_display =['url','title','thumbnail']

class courseadmin(admin.ModelAdmin):
    list_display =['title','subtitle','content','created_at']
   


class blogsadmin(admin.ModelAdmin):
    list_display =['title','description','written_by']
    list_filter = ['written_by',]
admin.site.register(article,articleadmin)
admin.site.register(about_us)
admin.site.register(testimonials,testimonialsadmin)
admin.site.register(query,queryadmin)
admin.site.register(videos,videosadmin)
admin.site.register(course,courseadmin)
admin.site.register(blogs,blogsadmin)
