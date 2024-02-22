from django.shortcuts import render
from django.shortcuts import render
from .forms import MijozForm,mijozForm,OquvchiForm
from .models import *
from django.views.generic import UpdateView, DeleteView, DetailView, CreateView,ListView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    t = Yonalish_Category.objects.all()
    o = Oqituvchilar.objects.all()
    markaz = Markaz.objects.all()
    musobaqa = Musoboqa.objects.all()
    tel = Tel_raqam.objects.all()
    form = MijozForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
    context = {
        'form': form,
        "yonalish": t,
        "oqtuvchi": o,
        "markaz": markaz,
        "musoboqa": musobaqa,
        "tel": tel
    }
    return render(request,"home-page/index.html",context=context)
@login_required
def Sinov(request):
    h = Oquvchilar.objects.all()
    guruh = Gurux_Category.objects.all()
    t = Yonalish_Category.objects.all()
    u = Sana_Category.objects.all()
    context = {
        "oquvchi": h,
        "grux": guruh,
        "yonalish": t,
        "sana": u
    }
    return render(request, 'Admin1/index.html', context=context)
@login_required
def tel(request):
    lid = Mijoz.objects.filter(etabi='lid')
    brak= Mijoz.objects.filter(etabi='brak')
    nedazon = Mijoz.objects.filter(etabi='nedazon')
    royxatga_olindi = Mijoz.objects.filter(etabi='royxatga_olindi')
    context = {
        'lid': lid,
        'brak':brak,
        'nedazon':nedazon,
        'royxatga_olindi': royxatga_olindi
    }
    return render(request,'mijoz/index.html',context=context)

class Mijoz_Edit(UpdateView):
    model = Mijoz
    form_class = mijozForm
    template_name = 'mijoz_edit.html'
    success_url = reverse_lazy("tel")

def qidiruv_detail(request,id=id):
    news = Oquvchilar.objects.filter(guruhi=id)
    context = {
        "detel": news,
    }
    return render(request, 'qidiruv_detel.html', context=context)

class Oquvchi_qoshish(CreateView):
    model = Oquvchilar
    form_class = OquvchiForm
    template_name = 'oquvchi_create.html'
    success_url = reverse_lazy("adminlar")
class Oquvchi_Detail(DetailView):
    model = Oquvchilar
    context_object_name= 'oquvchi'
    template_name= 'oquvchi_detail.html'
class Oquvchi_Delete(DeleteView):
    model = Oquvchilar
    template_name= 'oquvchi_delete.html'
    success_url = reverse_lazy("adminlar")
class Oquvchi_Edit(UpdateView):
    model = Oquvchilar
    form_class = OquvchiForm
    template_name = 'oquvchi_edit.html'
    success_url = reverse_lazy("adminlar")
class SearchResultList(ListView):
    model = Oquvchilar
    template_name = 'search_result.html'
    context_object_name = 'OQUVCHI'
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Oquvchilar.objects.filter(
            Q(ismi_familya__icontains=query)

        )
def kurs(request):
    return render(request,'Kurslar.html',context={})
def page_1(request):
    return render(request,'1-page/index.html',context={})
def page_kids(request):
    return render(request,'Home-kids/index.html',context={})
def teacher(request):
    o = Oqituvchilar.objects.all()
    context = {
        "oqtuvchi":o
    }
    return render(request,'Teachers/index.html',context=context)