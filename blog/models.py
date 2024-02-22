from django.db import models
from audioop import reverse
# Create your models here.

class Category(models.Model):
    nomi = models.CharField(max_length=250)
    def __str__(self):
        return self.nomi
class Mijoz(models.Model):
    ismi = models.CharField(max_length=200)
    raqami = models.IntegerField()
    etabi = models.CharField(max_length=100,default='lid')

    def __str__(self):
        return self.ismi
class Yonalish_Category(models.Model):
    nomi = models.CharField(max_length=250)
    def __str__(self):
        return self.nomi
class Gurux_Category(models.Model):
    nomi = models.CharField(max_length=250)
    def __str__(self):
        return self.nomi
class Tolov_Category(models.Model):
    nomi = models.CharField(max_length=250)
    def __str__(self):
        return self.nomi
class Sana_Category(models.Model):
    nomi = models.CharField(max_length=250)
    def __str__(self):
        return self.nomi

class Oquvchilar(models.Model):
    ismi_familya = models.CharField(max_length=200)
    yonalish = models.ForeignKey(Yonalish_Category, on_delete=models.CASCADE)
    guruhi = models.ForeignKey(Gurux_Category, on_delete=models.CASCADE)
    sana = models.ForeignKey(Sana_Category, on_delete=models.CASCADE)
    tolov = models.ForeignKey(Tolov_Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.ismi_familya

    def get_absolute_url(self):
        return reverse("Oquvchi_List")
class Oqituvchilar(models.Model):
    ismi_familyasi = models.CharField(max_length=200)
    malumoti = models.TextField()
    rasm = models.ImageField(upload_to='news/images')

    def __str__(self):
        return self.ismi_familyasi
class Markaz(models.Model):
    nomi = models.CharField(max_length=500)
    text = models.TextField()
    rasm = models.ImageField(upload_to='news/images')
    def __str__(self):
        return self.nomi

class Musoboqa(models.Model):
    nomi = models.CharField(max_length=500,default='Musoboqa')
    rasm = models.ImageField(upload_to='news/images')

    def __str__(self):
        return self.nomi
class Tel_raqam(models.Model):
    telfon = models.CharField(max_length=100)

    def __str__(self):
        return self.telfon