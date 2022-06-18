# Generated by Django 4.0.5 on 2022-06-18 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ade4', '0005_sanction'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sanction',
            options={'ordering': ['-meeting__date'], 'verbose_name': 'Sanction', 'verbose_name_plural': 'Sanctions'},
        ),
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('reason', models.CharField(max_length=255, verbose_name='Raison')),
                ('justified', models.BooleanField(default=False, verbose_name='Justifiée?')),
                ('sanctioned', models.BooleanField(default=False, verbose_name='Sanctionné?')),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ade4.meeting', verbose_name='Séance')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ade4.member', verbose_name='Membre')),
            ],
            options={
                'verbose_name': 'Absence',
                'verbose_name_plural': 'Absences',
                'ordering': ['-meeting__date'],
            },
        ),
    ]
