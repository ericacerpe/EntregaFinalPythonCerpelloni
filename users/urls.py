from django.contrib.auth.views import LogoutView
from django.urls import path
from users.views import login_view, register,update_user,update_user_profile
from ECycling.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', index, name='index'),
   # path('login/', login_view),
    path('login/', login_view , name='login'),
    path('logout/', LogoutView.as_view(template_name='Users/logout.html')),
    path('registrarse/', register , name='registrarse'),
    path('update/', update_user , name='actualiza_usuario'),
    path('update/profile/', update_user_profile, name='actualiza_perfil'),

] 
