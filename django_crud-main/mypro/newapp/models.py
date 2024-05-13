from django.db import models

class Book(models.Model):
    BookName=models.CharField(max_length=100) #string
    AuthorName=models.CharField(max_length=100) #string
    Price=models.IntegerField() #int