from django.shortcuts import render
from django.http import HttpResponse #responsible for returning a response to a user. 
import datetime as dt

# Create your views here.
def welcome(request): 
    return HttpResponse('Welcome to the Moringa Tribune')

def news_of_day(request):
    date=dt.date.today()
    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
    return HttpResponse(html)
    '''