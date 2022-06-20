# Generated by Django 4.0.5 on 2022-06-20 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ade4', '0010_rename_accounttype_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='title',
            field=models.CharField(choices=[('assistance', 'assistance'), ('savings', 'savings'), ('scholar_savings', 'scholar_savings'), ('project', 'project'), ('sanction', 'sanction'), ('inscription', 'inscription'), ('operation_fees', 'operation_fees'), ('other', 'other')], max_length=30, unique=True, verbose_name='Name'),
        ),
    ]