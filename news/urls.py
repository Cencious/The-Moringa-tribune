from django.urls import path
from . import views 


urlpatterns =[
    path('',views.welcome,name='welcome'),
    path('',views.news_of_day,name='newsToday')]