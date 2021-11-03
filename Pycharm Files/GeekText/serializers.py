from rest_framework import serializers

from .models import Author
from .models import Rating
from .models import Book
from .models import Wishlist

from .models import UserProfile

##from .models import Transaction
from .models import ShoppingCart


from django.contrib.auth.models import User, Group
from rest_framework import serializers


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('__all__')

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('__all__')

class RatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rating
        fields = ('__all__')

class RatingSortedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rating
        fields = ('__all__')

class WishlistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wishlist
        fields = ('__all__')

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('__all__')

class ShoppingCartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = ('__all__')

#class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    #class Meta:
        #model = Transaction
        #fields = ('__all__')
