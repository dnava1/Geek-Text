from django.contrib import admin


from .models import Author
#from .models import Rating
from .models import Book
#from .models import Wishlist
#from .models import UserProfile

#from .models import ShoppingCart
#from .models import Transaction


admin.site.register(Author)
#admin.site.register(Rating)
admin.site.register(Book)
#admin.site.register(Wishlist)
#admin.site.register(UserProfile)
#admin.site.register(Transaction)
#admin.site.register(ShoppingCart)