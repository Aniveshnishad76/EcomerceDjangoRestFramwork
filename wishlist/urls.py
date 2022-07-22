from django.urls import path

from wishlist.views import WishListView, WishListViewCreate

urlpatterns = [
    path('my-wishlist/', WishListView.as_view(), name="my-wishlist"),
    path('<slug>', WishListViewCreate.as_view(), name="add-to-wishlist"),

]