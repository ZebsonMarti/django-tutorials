from django.db import models
from django_resized import ResizedImageField
# Create your models here.


class ProfileImage(models.Model):
    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
        ordering = ["name"]

    name = models.CharField(verbose_name="Name", max_length=30, null=False, blank=False)
    image = models.ImageField(verbose_name="Photo", upload_to="images/", null=False, blank=False)
    resized_image = ResizedImageField(
        verbose_name="Resized Photo", 
        upload_to="images/", 
        size=[500, 300], quality=75,
        null=True, blank=False
    )