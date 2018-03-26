from django.conf.urls import url
from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views
app_name = 'accounts'
urlpatterns = [
    path('committee/login/' , auth_views.login , {'template_name':'registration/committee_login.html'} ,name='committee_login' ) ,
    path('student/login/' , auth_views.login , {'template_name':'registration/student_login.html'} ,name='login' ) ,
    path('logout/' , auth_views.logout , {'next_page': '/'} ,name = 'logout' ) ,
    path('signup/' , views.signup , name = 'signup' ) ,
    path('' , views.index , name = 'index') ,
    path('event/' , views.event , name = 'event') ,
    url(r'^profile/(?P<pk>\d+)/update/$' ,views.StudentProfileUpdate.as_view() , name = 'update_profile' )
]