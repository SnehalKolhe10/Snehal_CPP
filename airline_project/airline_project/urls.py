# airline_project/urls.py
from django.contrib import admin
from django.urls import path, include
from airline import views  # Import your views to link the root URL

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('airline/', include('airline.urls')),  # Include the airline app's URLs
    path('', views.landing_page, name='landing_page'),  # Root URL, landing page
]
