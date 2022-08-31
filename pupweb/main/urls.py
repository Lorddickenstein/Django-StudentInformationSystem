from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('grade/', views.grade, name='grade'),
    path('enrollment/', views.enrollment, name='enrollment'),
    path('schedule/', views.schedule, name='schedule'),
    path('account/signup/', views.signup, name='signup'),
    path('account/login/', views.login_view, name='login'),
] + static(settings.STATIC_URL, dcoument_root=settings.STATIC_ROOT)