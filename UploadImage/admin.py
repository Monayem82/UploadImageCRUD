from django.contrib import admin
from .models import ImageStore

class ImageStoreAdmin(admin.ModelAdmin):
    list_display=('id','image_name','image')

admin.site.register(ImageStore,ImageStoreAdmin)