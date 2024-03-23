from django.contrib import admin
from Gallery.models import gallery
class GalleryAdmin(admin.ModelAdmin):
    list_display=("gallery_img",)
# Register your models here.
admin.site.register(gallery,GalleryAdmin)

# Register your models here.
