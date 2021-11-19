from rest_framework import viewsets
from rest_framework import generics

#import django_filters.rest_framework


from .serializers import RatingSerializer
from .serializers import ShoppingCartSerializer
from .serializers import TransactionSerializer
from .serializers import AuthorSerializer
from .serializers import UserProfileSerializer
from .serializers import WishlistSerializer
from .serializers import BookSerializer
# from .serializers import OrderBookSerializer

from .models import Author
from .models import Rating
from .models import Book
from .models import Wishlist
from .models import UserProfile
from .models import Transaction
from .models import ShoppingCart
# from .models import OrderBook




class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('isbn')
    serializer_class = BookSerializer
    filter_fields= (
        'bookAuthor',
    )



class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('id')
    serializer_class = AuthorSerializer

#class BookListView(generics.ListAPIView):
   # queryset = Book.objects.all()
    #serializer_class = BookSerializer
   # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

# 





class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all().order_by('id')
    serializer_class = RatingSerializer

class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all().order_by('user')
    serializer_class = ShoppingCartSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all().order_by('username')
    serializer_class = UserProfileSerializer




class WishListViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all().order_by('wishListName')
    serializer_class = WishlistSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by('id')
    serializer_class = TransactionSerializer





