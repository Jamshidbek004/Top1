from django.contrib import admin
from blog.models import *
# Register your models here.
@admin.register(Mijoz)
class MijozAdmin(admin.ModelAdmin):
    list_display = ['ismi']

@admin.register(Category)
class CategiryAdmin(admin.ModelAdmin):
    list_display = ['nomi']
@admin.register(Yonalish_Category)
class Yonalish_CategoryAdmin(admin.ModelAdmin):
    list_display = ['nomi']
@admin.register(Gurux_Category)
class Gurux_CategoryAdmin(admin.ModelAdmin):
    list_display = ['nomi']
@admin.register(Tolov_Category)
class Tolov_CategoryAdmin(admin.ModelAdmin):
    list_display = ['nomi']
@admin.register(Oquvchilar)
class OquvchilarAdmin(admin.ModelAdmin):
    list_display = ['ismi_familya']
@admin.register(Sana_Category)
class Sana_CategoryAdmin(admin.ModelAdmin):
    list_display = ['nomi']
@admin.register(Oqituvchilar)
class OqtuvchiAdmin(admin.ModelAdmin):
    list_display = ['ismi_familyasi']
@admin.register(Markaz)
class MarkazAdmin(admin.ModelAdmin):
    list_display = ['nomi']
@admin.register(Musoboqa)
class MusoboqaAdmin(admin.ModelAdmin):
    list_display = ['nomi']
@admin.register(Tel_raqam)
class Tel_raqamAdmin(admin.ModelAdmin):
    list_display = ['telfon']