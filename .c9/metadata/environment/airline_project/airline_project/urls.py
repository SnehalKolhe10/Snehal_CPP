{"filter":false,"title":"urls.py","tooltip":"/airline_project/airline_project/urls.py","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":10,"column":0},"end":{"row":10,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"266a2b4e6948ab1582746aee011364d39e58871f","undoManager":{"mark":4,"position":4,"stack":[[{"start":{"row":15,"column":10},"end":{"row":15,"column":11},"action":"insert","lines":["a"],"id":2},{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"insert","lines":["i"]},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"insert","lines":["r"]},{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"insert","lines":["l"]}],[{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"insert","lines":["i"],"id":3},{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"insert","lines":["n"]},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"insert","lines":["e"]}],[{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"insert","lines":["/"],"id":4}],[{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"remove","lines":["/"],"id":5},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"remove","lines":["e"]},{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"remove","lines":["n"]},{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"remove","lines":["i"]},{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"remove","lines":["l"]},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"remove","lines":["r"]},{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"remove","lines":["i"]},{"start":{"row":15,"column":10},"end":{"row":15,"column":11},"action":"remove","lines":["a"]}],[{"start":{"row":0,"column":0},"end":{"row":17,"column":0},"action":"remove","lines":["from django.contrib import admin","from django.urls import path, include","from django.contrib.auth import views as auth_views","from django.conf import settings"," ","","urlpatterns = [","    path('admin/', admin.site.urls),","    ","    # Login and Logout URLs","#   path('login/', auth_views.LoginView.as_view(success_url='/flights/'), name='login'),","#   path('logout/', auth_views.LogoutView.as_view(), name='logout'),","    ","#     # Include the flight-related views from the airline app","#     path('flights/', include('airline.urls')),","    path('', include('airline.urls')),","]",""],"id":6},{"start":{"row":0,"column":0},"end":{"row":10,"column":0},"action":"insert","lines":["# airline_project/urls.py","from django.contrib import admin","from django.urls import path, include","from airline import views  # Import your views to link the root URL","","urlpatterns = [","    path('admin/', admin.site.urls),  # Admin URL","    path('airline/', include('airline.urls')),  # Include the airline app's URLs","    path('', views.landing_page, name='landing_page'),  # Root URL, landing page","]",""]}]]},"timestamp":1732153590405}