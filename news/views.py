from django.shortcuts import redirect, render
from django.http import Http404,HttpResponse #responsible for returning a response to a user. 
import datetime as dt
from .models import Article



# Create your views here.
def welcome(request): 
    # return HttpResponse('Welcome to the Moringa Tribune')
    return render(request, 'welcome.html')

def convert_dates(dates):
    #function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days =['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    #Returning the actual days of the week
    day = days[day_number]
    return day

def news_of_day(request):
    date = dt.date.today()
    #Function to convert date object to find exact day
    # day = convert_dates(date)

    news = Article.todays_news()
    return render(request, 'all-news/today-news.html', {"date": date,"news":news})

def past_days_news (request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        #raise 404 error when ValueError is thrown
        raise Http404()
        assert False
    if date == dt.date.today():
        return redirect(news_of_day)
        
    news = Article.days_news(date)
    return render(request, 'all-news/past-news.html',{"date": date,"news":news})

    
   





    
