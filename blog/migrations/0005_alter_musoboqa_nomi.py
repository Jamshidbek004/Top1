# Generated by Django 4.2.3 on 2024-02-20 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_musoboqa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musoboqa',
            name='nomi',
            field=models.CharField(default='Musoboqa', max_length=500),
        ),
    ]
