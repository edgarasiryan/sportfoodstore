from django.urls import path
from .views import cart_view, cart_add

app_name = 'cart'

urlpatterns = [
    path('', cart_view, name='cart-view'),
    path('add/', cart_add, name='add_to_cart'),
    # path('search/<slug:slug>', category_list, name='category-list'),
]