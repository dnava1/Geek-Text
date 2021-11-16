from rest_framework import viewsets

from .serializers import RatingSerializer
from .serializers import ShoppingCartSerializer
##from .serializers import TransactionSerializer
from .serializers import AuthorSerializer
from .serializers import UserProfileSerializer
from .serializers import WishlistSerializer
from .serializers import BookSerializer

from .models import Author
from .models import Rating
from .models import Book
from .models import Wishlist
from .models import UserProfile
##from .models import Transaction
from .models import ShoppingCart


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('isbn')
    serializer_class = BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('id')
    serializer_class = AuthorSerializer



class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all().order_by('isbn')
    serializer_class = RatingSerializer

class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all().order_by('id')
    serializer_class = ShoppingCartSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all().order_by('username')
    serializer_class = UserProfileSerializer



class WishListViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all().order_by('wishListName')
    serializer_class = WishlistSerializer





