# Generated by Django 4.2.3 on 2024-02-20 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_markaz'),
    ]

    operations = [
        migrations.CreateModel(
            name='Musoboqa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=500)),
                ('rasm', models.ImageField(upload_to='news/images')),
            ],
        ),
    ]
