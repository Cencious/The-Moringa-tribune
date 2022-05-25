from django.urls import path
from . import views 
from django.conf.urls.static import static 
from django.conf import settings

#URLConfiguration
urlpatterns =[
    path('',views.welcome,name='welcome'),
    path('today/',views.news_of_day,name='newsToday'),
    path('archives/(\d{4}-\d{2}-\d{2})/', views.past_days_news, name='pastnews'),
    path('search/',views.search_results, name='search_results'),
    path('article/(\d+)', views.article,name='article')
    
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)