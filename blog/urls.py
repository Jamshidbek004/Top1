
from django.contrib import admin
from django.urls import path
from blog.views import *

urlpatterns = [
    path('',page_1,name="1_page"),
path('home',home,name="home"),
path('kids',page_kids,name="kids"),
path('kurs',kurs,name="kurs"),
path('teacher',teacher,name="teacher"),
path('tel',tel,name="tel"),
path('Adminlar',Sinov,name="adminlar"),
path('mijoz_edit/<int:pk>',Mijoz_Edit.as_view(),name="mijoz_edit"),
path('oquvchi_create/',Oquvchi_qoshish.as_view(),name="oquvchi_create"),
path('oquvchi_detele/<int:pk>',Oquvchi_Delete.as_view(),name="oquvchi_delete"),
path('oquvchi_detail/<int:pk>',Oquvchi_Detail.as_view(),name="oquvchi_detail"),
path('oquvchi_edit/<int:pk>',Oquvchi_Edit.as_view(),name="oquvchi_edit"),
path('qidiruv_detel/<int:id>/',qidiruv_detail,name="qidiruv_detel"),
path('search/',SearchResultList.as_view(), name="search"),
]