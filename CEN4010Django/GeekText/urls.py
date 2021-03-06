from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)
#router.register(r'ratings', views.RatingViewSet)
#router.register(r'wishlist', views.WishListViewSet)
router.register(r'users', views.UserProfileViewSet)
router.register(r'shopping cart', views.ShoppingCartViewSet)
#router.register(r'transaction', views.TransactionViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
