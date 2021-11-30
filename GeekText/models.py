from django.db import models



from django.core.validators import MinValueValidator, MaxValueValidator
import datetime


class Author(models.Model):
    id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    biography = models.CharField(max_length=250)
    publisher = models.CharField(max_length=100)

    def __int__(self):
        return str(self.id)


class Book(models.Model):

    GENRE_CHOICES = [

        ('FICTION', 'Fiction'),
        ('NONFICTION', 'Nonfiction'),
        ('DRAMA', 'Drama'),
        ('FOLKTALE', 'Folktale'),
        ('POETRY', 'Poetry')

    ]



    isbn = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=75)
    publisher = models.CharField(max_length=75)
    price = models.IntegerField()
    genre = models.CharField(max_length=30, choices=GENRE_CHOICES)
    description = models.CharField(max_length=250)
    bookAuthor = models.ForeignKey(Author, on_delete=models.CASCADE)
    yearPublished = models.IntegerField()
    copiesSold = models.IntegerField()



    def __int__(self):
       return str(self.isbn)





#class Rating(models.Model):
   # id = models.IntegerField(primary_key=True)
   # book = models.ForeignKey(Book, on_delete=models.CASCADE, default='',)
  #  numberOfStars = models.IntegerField(validators=[MinValueValidator(1),
      #                                 MaxValueValidator(5)])
   # review = models.CharField(max_length=250, default='')
   # date = models.DateField()

   # def __int__(self):
      #  return str(self.id)




#class ShoppingCart(models.Model):
   # id = models.IntegerField(primary_key=True)

   # books = models.ForeignKey(Book, on_delete=models.CASCADE)

   # def __str__(self):
      #  return str(self.id)





#class UserProfile(models.Model):

   # username = models.CharField(max_length=100, unique=True)
   # password = models.CharField(max_length=50)
  #  name = models.CharField(max_length=50, blank=True)
   # emailAddress = models.CharField(max_length=50, blank=True, unique=True)
    #homeAddress = models.CharField(max_length=100, blank=True)
   # shoppingCart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)

   # def __str__(self):
     #   return str(self.username)


#class Transaction(models.Model):
    #id = models.IntegerField(primary_key=True)
   # user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
   # creditCardNumber = models.IntegerField()
   # ccType = models.CharField(max_length=30)
   # ccExpire = models.DateField()
   # ccSecurityCode = models.IntegerField()

   # def __str__(self):
       # return str(self.id)


#class Wishlist(models.Model):
   # wishListName = models.CharField(max_length=100,  default='Null')
   # books = models.ForeignKey(Book, on_delete=models.CASCADE)
    #user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default='Null')

 #   def __str__(self):
      #  return str(self.wishListName)


