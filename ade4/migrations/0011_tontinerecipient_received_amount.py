# Generated by Django 4.0.5 on 2022-06-10 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ade4', '0010_tontinerecipient'),
    ]

    operations = [
        migrations.AddField(
            model_name='tontinerecipient',
            name='received_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
