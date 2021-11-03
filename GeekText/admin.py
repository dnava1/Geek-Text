from django.contrib import admin


from .models import Author
from .models import Rating
from .models import Book
from .models import UserProfile

from .models import ShoppingCart
from .models import Wishlist



admin.site.register(Author)
admin.site.register(Rating)
admin.site.register(Book)
admin.site.register(UserProfile)

admin.site.register(ShoppingCart)
admin.site.register(Wishlist)