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
            '''
    return HttpResponse(html)

def convert_dates(dates):
    #function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)
    
    days =['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    #Returning the actual days of the week
    day = days[day_number]
    return day
