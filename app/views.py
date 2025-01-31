from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/login.html')


def login(request):
    return render(request, 'home/logikn.html')

def forgot_password(request):
    return render(request, 'home/forgot-password.html')

def dashboard_mahasiswa(request):
    return render(request, 'home/dashboard_mahasiswa.html')

def profil(request):
    return render(request, 'home/profil.html')