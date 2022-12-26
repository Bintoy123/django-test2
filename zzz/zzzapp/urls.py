from django.conf.urls import url
from . import views

app_name = 'application'

urlpatterns = [
    url(r'^other/$',views.other,name='other'),
    url(r'^form/$',views.form,name='form'),
    url(r'^login/$',views.user_login,name='login'),
    url(r'^special/$',views.special,name='special')
]
