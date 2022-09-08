from django.core.files.images import get_image_dimensions
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import ProfileImage
# Register your models here.

@admin.register(ProfileImage)
class ProfileImageAdmin(admin.ModelAdmin):
    list_display = ["name", "image_tag", "image"]

    def image_tag(self, obj):
        width, height = get_image_dimensions(obj.image.file)
        K = width/height
        h = 200
        w = int(K * h)
        print("\n", width, height, K, w, h, "\n")
        return (
            mark_safe(
                f"""<img src="{obj.image.url}" style="width:15%;"/>""" # width="{w}" height="{h}"
            )
            if obj.image
            else ""
        )