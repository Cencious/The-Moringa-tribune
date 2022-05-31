from hashlib import new
from django.shortcuts import redirect, render
from django.http import Http404,HttpResponse,Http404, HttpResponseRedirect #responsible for returning a response to a user. 
import datetime as dt
from .models import Article, NewsLetterReciepients
from .forms import NewsLetterForm

# Create your views here.
# def welcome(request): 
#     # return HttpResponse('Welcome to the Moringa Tribune')
#     return render(request, 'welcome.html')

# def convert_dates(dates):
#     #function that gets the weekday number for the date.
#     day_number = dt.date.weekday(dates)

#     days =['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#     #Returning the actual days of the week
#     day = days[day_number]
#     return day

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

def search_results(request):
    if 'article'in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles =Article.search_by_title(search_term)
        message = f"{search_term}"
        return render(request,'all-news/search.html',{"message":message,"articles":searched_articles})
    else:
        message = "You haven't searched for any term"
        return render(request,'all-news/search.html',{"message":message})
    
def article(request,article_id):
    try:
        article = Article.objects.get(id = article_id)
    except:
        raise Http404()
    return render(request,'all-news/article.html',{'article':article})
        
def news_today(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            print('Valid')
    else:
        form =NewsLetterForm()
    return render(request, 'all-news/today-news.html', {"date": date,"news":news,"letterForm":form})

def news_today(request):
    if request.method =='POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recepient =NewsLetterReciepients(name = name, email= email)
            HttpResponseRedirect('news_today')
        else:
            form =NewsLetterForm()
        return render(request, 'all-news/today-news.html', {"date": date,"news":news, "letterForm": form})
        





    
