# Generated by Django 4.2.3 on 2024-02-19 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Gurux_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Mijoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ismi', models.CharField(max_length=200)),
                ('raqami', models.IntegerField()),
                ('etabi', models.CharField(default='lid', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sana_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Tolov_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Yonalish_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Oquvchilar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ismi_familya', models.CharField(max_length=200)),
                ('guruhi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.gurux_category')),
                ('sana', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.sana_category')),
                ('tolov', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.tolov_category')),
                ('yonalish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.yonalish_category')),
            ],
        ),
    ]