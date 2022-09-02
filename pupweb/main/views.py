from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import RegisterForm
from accounts.models import UserProfile
from datetime import date


def index(request):
    user_type = 'none'
    request.session['user_type'] = user_type
    ctx = {'user_type': user_type, 'bg_img': 'bg-image-index'}

    if request.method == 'POST':
        btn_admin = request.POST.get('btnAdmin')
        btn_student = request.POST.get('btnStudent')

        if btn_admin:
           user_type = 'admin'
        elif btn_student:
            user_type = 'student'

        request.session['user_type'] = user_type

        return redirect('account/login')

    return render(request, 'main/index.html', {'ctx': ctx})



def signup(request):
    # TODO: Finish signup view
    user_type = request.session['user_type']
    ctx = {'user_type': user_type, 'bg_img': 'bg-image-signup'}

    # BUG: form does not exist, remove forms
    if user_type == 'none':
        return redirect('/')

    if request.method == 'POST':
        
        if form.is_valid():

            user = form.save(commit=False)
            

            # calculate age
            birthday = form.cleaned_data['birthday']
            today = date.today()
            age = (today.year - birthday.year) - ((today.month, today.day) < (birthday.month, birthday.day))
            user.age = age

            # generate user id
            branch = form.cleaned_data['branch']
            is_regular = form.cleaned_data['is_regular']
            year = today.year

            users = list(UserProfile.objects.filter(user_id__startswith=year))
            if users:
                max_id_num = max([int(user.user_id.split('-')[1]) for user in users])
                max_id_num = f'{max_id_num + 1: 05.0f}'
            else:
                max_id_num = '00001'

            user_id = f'{year}-{max_id_num}-{branch}-{"0" if is_regular else "1"}'
            user.user_id = user_id
            
            is_exist = UserProfile.objects.filter(user_id=user_id).first()
            
            if not is_exist:
                user.save()
                login(request, user)

                return redirect('/home')

    return render(request, 'registration/signup.html', {'ctx': ctx})


def login_view(request):
    user_type = request.session['user_type']

    ctx = {'user_type': user_type, 'bg_img': 'bg-image-login'}

    if request.method == 'POST':
        if user_type == 'student':
            username = request.POST.get('student-num')
        elif user_type == 'admin':
            username = request.POST.get('admin-num')
        else:
            return redirect('/')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/home')
        else:
            return redirect('/account/login')
    
    return render(request, 'registration/login.html', {'ctx': ctx})
        
    
@login_required(login_url='/')
def home(request):
    # TODO: Design my home view, make it like a twitter or something
    user_type = request.session['user_type']

    return render(request, 'main/home.html', {'user_type': user_type})


@login_required(login_url='/')
def grade(request):
    # TODO: Create functionality with grade page
    pass


@login_required(login_url='/')
def enrollment(request):
    # TODO: Create fnctionality with enrollment page
    pass


@login_required(login_url='/')
def schedule(request):
    # TODO: Create functionality with schedule page
    pass


