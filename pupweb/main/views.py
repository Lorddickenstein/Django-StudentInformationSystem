from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from accounts.forms import UserAdminCreationForm
from accounts.models import UserProfile


# Create your views here.
def index(request):
    user_type = 'none'

    if request.method == 'POST':
        btn_admin = request.POST.get('btnAdmin')
        btn_student = request.POST.get('btnStudent')

        if btn_admin:
           user_type = 'admin'
        elif btn_student:
            user_type = 'student'

        request.session['user_type'] = user_type
        
        return redirect('/login')

    return render(request, 'main/index.html', {})


def home(request):
    user_type = request.session['user_type']

    return render(request, 'main/home.html', {'user_type': user_type})


def signup(request):

    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            pass

    form = UserAdminCreationForm()
    user_type = request.session['user_type']

    return render(request, 'registration/signup.html', {'user_type': user_type, 'form': form})