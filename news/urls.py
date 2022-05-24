from django.urls import path
from . import views 

#URLConfiguration
urlpatterns =[
    path('',views.welcome,name='welcome'),
    path('today/',views.news_of_day,name='newsToday'),
    path('archives/(\d{4}-\d{2}-\d{2})/', views.past_days_news, name='pastnews')
    
    ]