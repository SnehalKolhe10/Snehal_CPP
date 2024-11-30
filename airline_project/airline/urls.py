from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin page
    path('', views.landing_page, name='landing_page'),  # Landing page
    path('accounts/login/', LoginView.as_view(template_name='airline/login.html'), name='login'),  # Login page
    path('accounts/logout/', LogoutView.as_view(next_page='landing_page'), name='logout'),  # Logout page
    path('register/', views.register, name='register'),  # Registration page
    path('home/', views.home, name='home'),  # Home page (requires login)
    path('add-to-cart/<int:flight_id>/', views.add_to_cart, name='add_to_cart'),  # Add flight to cart
    path('cart/', views.cart, name='cart'),  # View cart page
    path('cart/<int:cart_id>/remove/', views.remove_from_cart, name='remove_from_cart'),  # Remove flight from cart
    path('cart/<int:cart_id>/update/', views.update_cart, name='update_cart'),  # Update flight in cart
     path('checkout/', views.checkout, name='checkout'),
]
