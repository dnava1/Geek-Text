from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.fields.related import ForeignKey
from django_filters.filters import NumberFilter


class Book(models.Model):
    isbn = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=75)
    publisher = models.CharField(max_length=75)
    price = models.IntegerField()
    genre = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    bookAuthor = models.CharField(max_length=50)
    yearPublished = models.IntegerField()
    copiesSold = models.IntegerField()


    def __int__(self):
        return str(self.name)

class Author(models.Model):
    id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    biography = models.CharField(max_length=250)
    publisher = models.CharField(max_length=100)
    books = models.ForeignKey(Book, on_delete=models.CASCADE, default='')


    def __int__(self):
        return self.id

RATING_CHOICES = {
    ("1", "1"),
    ("2", "2"),
    ("3", "3"), 
    ("4", "4"), 
    ("5", "5"),
}

class Rating(models.Model):

    isbn = models.IntegerField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default='')
    numberOfStars = models.IntegerField(choices= RATING_CHOICES, default= '')
    review = models.TextField(max_length=250, default='', help_text= 'Your review here...')
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(blank = True, null = True, upload_to='reviews')

    def __int__(self):
        return str(self.isbn)


class ShoppingCart(models.Model):
    id = models.IntegerField(primary_key=True)
    books = models.ForeignKey(Book, on_delete=models.CASCADE)


class UserProfile(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50, blank=True)
    emailAddress = models.CharField(max_length=50, blank=True)
    homeAddress = models.CharField(max_length=100, blank=True)
    shoppingCart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class Wishlist(models.Model):
    wishListName = models.CharField(max_length=100, primary_key=True, default='Null')
    books = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default='Null')


