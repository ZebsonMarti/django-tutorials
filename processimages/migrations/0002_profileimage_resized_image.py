# Generated by Django 4.0.5 on 2022-09-07 18:33

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('processimages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileimage',
            name='resized_image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, null=True, quality=75, scale=None, size=[500, 300], upload_to='images/', verbose_name='Resized Photo'),
        ),
    ]
