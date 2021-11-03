from django.http import JsonResponse
from rest_framework import viewsets, status

from .serializers import RatingSerializer
from .serializers import ShoppingCartSerializer
##from .serializers import TransactionSerializer
from .serializers import AuthorSerializer
from .serializers import UserProfileSerializer
from .serializers import BookSerializer
from .serializers import WishlistSerializer

from .models import Author
from .models import Rating
from .models import Book
from .models import UserProfile
##from .models import Transaction
from .models import ShoppingCart
from .models import Wishlist
from rest_framework.response import Response
from rest_framework.decorators import api_view


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

class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all().order_by('name')
    serializer_class = WishlistSerializer

@api_view(['POST'])
def wishlistUpdate(request, pk):
    list = Wishlist.objects.get(id=pk)
    serializer = WishlistSerializer(instance=list, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response (serializer.data)