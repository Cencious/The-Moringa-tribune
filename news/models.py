import datetime as dt
from imp import SEARCH_ERROR
from django.db import models

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length =10, blank = True)

    def __str__(self): #returns a string representation of our model.
        return self.first_name

    class Meta:
        ordering = ('first_name',)

    def save_editor(self): 
        self.save()


    # try:
    #     editor = Editor.objects.get(email= 'example@gmail.com')
    #     print('Editor found')
    # except Editor.DoesNotExist:
    #     print('Editor was not found')

class tags(models.Model):
    name = models.CharField(max_length = 30)
    def __str__(self): #returns a string representation of our model
        return self.name

class Article(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)#many to many relationships
    pub_date = models.DateTimeField(null=True)#adds timestamp
    article_image = models.ImageField(upload_to = 'articles/' , blank=True)

    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news
    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return news
    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news

class NewsLetterReciepients(models.Model):
    name = models.CharField(max_length=30)
    email =models.EmailField()
