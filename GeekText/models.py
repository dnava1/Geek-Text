from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

from django.http import HttpResponse

class Author(models.Model):
    id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    biography = models.CharField(max_length=250)
    publisher = models.CharField(max_length=100)

    def __int__(self):
        return self.id

class Book(models.Model):
    isbn = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=75)
    publisher = models.CharField(max_length=75)
    price = models.IntegerField()
    genre = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    bookAuthor = models.ForeignKey(Author, on_delete=models.CASCADE, default='')
    yearPublished = models.IntegerField()
    copiesSold = models.IntegerField()

    def __int__(self):
        return self.isbn

class Rating(models.Model):
    isbn = models.IntegerField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default='')
    numberOfStars = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    review = models.CharField(max_length=250, default='')
    date = models.DateTimeField()

    def __int__(self):
        return self.isbn



#class Transaction(models.Model):
  #  id = models.IntegerField(primary_key=True)
   # date = models.DateField()
   # total = models.IntegerField()
    #creditCardNumber = models.IntegerField()
    #ccType = models.CharField(max_length=30)
    #ccExpire = models.DateField()
    #ccSecurityCode = models.IntegerField()






class ShoppingCart(models.Model):
    id = models.IntegerField(primary_key=True)
    books = models.ForeignKey(Book, on_delete=models.CASCADE)




class UserProfile(models.Model):
    username = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50, blank=True)
    emailAddress = models.CharField(max_length=50, blank=True)
    homeAddress = models.CharField(max_length=100, blank=True)
    shoppingCart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

class Wishlist(models.Model):
    name = models.CharField(max_length=100, blank=True, unique=True)
    book = models.ManyToManyField(Book)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default='Null')
