from django.shortcuts import render
from .models import Doctors, Doctors_education


def HomeView(request):
    return render(request, 'home/home.html')


def ContactsView(request):
    return render(request, 'contacts/contacts.html')


def InfoView(request):
    context = {
        'key_all_about_doctors': Doctors.objects.all()
    }
    return render(request, 'info/info.html', context)


def InfoDocView(request, num):
    context = {
        "key_all_about1doctor": Doctors.objects.filter(doctors_id=num)
    }
    return render(request, 'infodoc/infodoc.html', context)
