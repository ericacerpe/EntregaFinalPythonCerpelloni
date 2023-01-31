from django.contrib.auth.views import LogoutView
from django.urls import path
from users.views import login_view, register,update_user
from ECycling.views import index

urlpatterns=[
    path('', index, name='index'),
   # path('login/', login_view),
    path('login/', login_view , name='login'),
    path('logout/', LogoutView.as_view(template_name='Users/logout.html')),
    path('registrarse/', register , name='registrarse'),
    path('update/', update_user , name='actualiza_usuario'),

]