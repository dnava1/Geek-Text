from typing import ValuesView
from django.db.models.query import QuerySet
from django.views import generic
from rest_framework import viewsets
from rest_framework.serializers import Serializer
from django.shortcuts import render
from django.http import JsonResponse

from .serializers import RatingSerializer, RatingSortedSerializer
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
    queryset = Rating.objects.all().order_by('-numberOfStars')
    serializer_class = RatingSerializer

def rating_list(request):
    if request.method == 'GET':
        reviews = Rating.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            reviews = reviews.filter(title__icontains=title)
        
        reviews_serializer = reviewserializer(reviews, many=True)
        return JsonResponse(reviews_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = reviewserializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Rating.objects.all().delete()
        return JsonResponse({'message': '{} reviews were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

class RatingSortedView(viewsets.ViewSet):
    querySet = Rating.objects.all().order_by('-isbn')
    serializer_class = RatingSortedSerializer



class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all().order_by('id')
    serializer_class = ShoppingCartSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all().order_by('username')
    serializer_class = UserProfileSerializer



class WishListViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all().order_by('wishListName')
    serializer_class = WishlistSerializer





