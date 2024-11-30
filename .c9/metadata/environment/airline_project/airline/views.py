{"filter":false,"title":"views.py","tooltip":"/airline_project/airline/views.py","undoManager":{"mark":10,"position":10,"stack":[[{"start":{"row":100,"column":0},"end":{"row":117,"column":0},"action":"remove","lines":["def update_cart(request, cart_id):","    cart_item = get_object_or_404(Cart, id=cart_id)","    ","    # Ensure that the cart item belongs to the current user","    if cart_item.user == request.user:","        if request.method == 'POST':","            form = CartUpdateForm(request.POST, instance=cart_item)","            if form.is_valid():","                form.save()  # Save the updated number of passengers","                messages.success(request, 'Cart updated successfully!')","                return redirect('cart')  # Redirect back to cart after update","        else:","            form = CartUpdateForm(instance=cart_item)","    else:","        messages.error(request, 'You cannot update an item from another user\\'s cart.')","","    return render(request, 'airline/update_cart.html', {'form': form, 'cart_item': cart_item})",""],"id":2},{"start":{"row":100,"column":0},"end":{"row":109,"column":94},"action":"insert","lines":["def update_cart(request, cart_id):","    cart_item = get_object_or_404(CartItem, id=cart_id)","    if request.method == 'POST':","        form = CartUpdateForm(request.POST, instance=cart_item)","        if form.is_valid():","            form.save()","            return redirect('cart')","    else:","        form = CartUpdateForm(instance=cart_item)","    return render(request, 'airline/update_cart.html', {'cart_item': cart_item, 'form': form})"]}],[{"start":{"row":110,"column":0},"end":{"row":111,"column":0},"action":"insert","lines":["",""],"id":3}],[{"start":{"row":0,"column":0},"end":{"row":119,"column":0},"action":"remove","lines":["from django.shortcuts import render, redirect, get_object_or_404","from django.contrib.auth.forms import UserCreationForm","from django.contrib.auth.decorators import login_required","from django.contrib import messages","from .models import Flight, Cart","from .forms import CartUpdateForm","","# Landing page: Redirects logged-in users to 'home' and shows options to non-logged-in users","def landing_page(request):","    if request.user.is_authenticated:","        return redirect('home')  # Redirect to home if the user is already logged in","    return render(request, 'airline/landing.html')  # Show login/register options for new users","","# Registration page","def register(request):","    if request.method == 'POST':","        form = UserCreationForm(request.POST)","        if form.is_valid():","            form.save()","            messages.success(request, f'Account created for {form.cleaned_data[\"username\"]}!')","            return redirect('login')  # Redirect to login page after successful registration","    else:","        form = UserCreationForm()","","    return render(request, 'airline/register.html', {'form': form})","","# Home page with flight search","@login_required","def home(request):","    flights = None","    if request.method == 'POST':","        source = request.POST.get('source')","        destination = request.POST.get('destination')","        date = request.POST.get('date')","        passengers = request.POST.get('passengers', 1)","","        # Filter flights based on user input","        flights = Flight.objects.filter(","            departure_city=source,","            arrival_city=destination,","            departure_time__date=date","        )","","        # Add flight duration and price calculation","        for flight in flights:","            duration = flight.arrival_time - flight.departure_time","            flight.duration = str(duration)  # Store as string to display","","    return render(request, 'airline/home.html', {'flights': flights})","","# Add flight to cart","@login_required","def add_to_cart(request, flight_id):","    flight = get_object_or_404(Flight, id=flight_id)","","    # Get passengers count from the form (or default to 1 if not provided)","    passengers = int(request.POST.get('passengers', 1))","","    # Check if the flight is already in the user's cart","    cart_item, created = Cart.objects.get_or_create(user=request.user, flight=flight)","","    if created:","        cart_item.passengers = passengers","        cart_item.save()","        messages.success(request, f'{flight.flight_number} has been added to your cart.')","    else:","        cart_item.passengers += passengers  # If already in the cart, increase the count","        cart_item.save()","        messages.info(request, f'{passengers} more passengers added to your cart for {flight.flight_number}.')","","    return redirect('cart')","","# View to display the cart","@login_required","def cart(request):","    user_cart = Cart.objects.filter(user=request.user)","    total_price = sum(item.flight.price * item.passengers for item in user_cart)","","    # Add the total price for each cart item (individual total) to display in the template","    for item in user_cart:","        item.total_price = item.flight.price * item.passengers  # Calculate the total price for this flight","","    return render(request, 'airline/cart.html', {'cart': user_cart, 'total_price': total_price})","","# Remove flight from the cart","@login_required","def remove_from_cart(request, cart_id):","    cart_item = get_object_or_404(Cart, id=cart_id)","","    # Ensure that the cart item belongs to the current user","    if cart_item.user == request.user:","        cart_item.delete()  # Remove the item from the cart","        messages.success(request, 'Flight removed from cart.')","    else:","        messages.error(request, 'You cannot remove an item from another user\\'s cart.')","","    return redirect('cart')","","# Update flight in the cart (number of passengers)","@login_required","def update_cart(request, cart_id):","    cart_item = get_object_or_404(CartItem, id=cart_id)","    if request.method == 'POST':","        form = CartUpdateForm(request.POST, instance=cart_item)","        if form.is_valid():","            form.save()","            return redirect('cart')","    else:","        form = CartUpdateForm(instance=cart_item)","    return render(request, 'airline/update_cart.html', {'cart_item': cart_item, 'form': form})","","# Checkout page - New checkout functionality","@login_required","def checkout(request):","    user_cart = Cart.objects.filter(user=request.user)","    total_price = sum(item.flight.price * item.passengers for item in user_cart)","    ","    # Placeholder for any additional checkout logic (payment, etc.)","    return render(request, 'airline/checkout.html', {'cart': user_cart, 'total_price': total_price})",""],"id":4},{"start":{"row":0,"column":0},"end":{"row":115,"column":0},"action":"insert","lines":["from django.shortcuts import render, redirect, get_object_or_404","from django.contrib.auth.forms import UserCreationForm","from django.contrib.auth.decorators import login_required","from django.contrib import messages","from .models import Flight, CartItem  # Corrected to use CartItem","from .forms import CartUpdateForm","","# Landing page: Redirects logged-in users to 'home' and shows options to non-logged-in users","def landing_page(request):","    if request.user.is_authenticated:","        return redirect('home')  # Redirect to home if the user is already logged in","    return render(request, 'airline/landing.html')  # Show login/register options for new users","","# Registration page","def register(request):","    if request.method == 'POST':","        form = UserCreationForm(request.POST)","        if form.is_valid():","            form.save()","            messages.success(request, f'Account created successfully! Please log in.')","            return redirect('login')  # Redirect to login page after successful registration","    else:","        form = UserCreationForm()","","    return render(request, 'airline/register.html', {'form': form})","","# Home page with flight search","@login_required","def home(request):","    flights = None","    if request.method == 'POST':","        source = request.POST.get('source')","        destination = request.POST.get('destination')","        date = request.POST.get('date')","","        if source and destination and date:","            # Filter flights based on user input","            flights = Flight.objects.filter(","                departure_city__iexact=source,","                arrival_city__iexact=destination,","                departure_time__date=date","            )","","    return render(request, 'airline/home.html', {'flights': flights})","","# Add flight to cart","@login_required","def add_to_cart(request, flight_id):","    flight = get_object_or_404(Flight, id=flight_id)","","    # Get passengers count from the form (or default to 1 if not provided)","    passengers = int(request.POST.get('passengers', 1))","","    # Check if the flight is already in the user's cart","    cart_item, created = CartItem.objects.get_or_create(user=request.user, flight=flight)","","    if created:","        cart_item.passengers = passengers","        cart_item.save()","        messages.success(request, f'{flight.flight_number} has been added to your cart.')","    else:","        cart_item.passengers += passengers  # If already in the cart, increase the count","        cart_item.save()","        messages.info(request, f'{passengers} more passengers added to your cart for {flight.flight_number}.')","","    return redirect('cart')","","# View to display the cart","@login_required","def cart(request):","    user_cart = CartItem.objects.filter(user=request.user)","    total_price = sum(item.flight.price * item.passengers for item in user_cart)","","    # Add the total price for each cart item to display in the template","    for item in user_cart:","        item.total_price = item.flight.price * item.passengers","","    return render(request, 'airline/cart.html', {'cart': user_cart, 'total_price': total_price})","","# Remove flight from the cart","@login_required","def remove_from_cart(request, cart_id):","    cart_item = get_object_or_404(CartItem, id=cart_id)","","    # Ensure that the cart item belongs to the current user","    if cart_item.user == request.user:","        cart_item.delete()","        messages.success(request, 'Flight removed from cart.')","    else:","        messages.error(request, 'You cannot remove an item from another user\\'s cart.')","","    return redirect('cart')","","# Update flight in the cart (number of passengers)","@login_required","def update_cart(request, cart_id):","    cart_item = get_object_or_404(CartItem, id=cart_id)","    if request.method == 'POST':","        form = CartUpdateForm(request.POST, instance=cart_item)","        if form.is_valid():","            form.save()","            messages.success(request, 'Cart updated successfully.')","            return redirect('cart')","    else:","        form = CartUpdateForm(instance=cart_item)","    return render(request, 'airline/update_cart.html', {'cart_item': cart_item, 'form': form})","","# Checkout page","@login_required","def checkout(request):","    user_cart = CartItem.objects.filter(user=request.user)","    total_price = sum(item.flight.price * item.passengers for item in user_cart)","","    # Placeholder for any additional checkout logic (e.g., payment integration)","    return render(request, 'airline/checkout.html', {'cart': user_cart, 'total_price': total_price})",""]}],[{"start":{"row":0,"column":0},"end":{"row":115,"column":0},"action":"remove","lines":["from django.shortcuts import render, redirect, get_object_or_404","from django.contrib.auth.forms import UserCreationForm","from django.contrib.auth.decorators import login_required","from django.contrib import messages","from .models import Flight, CartItem  # Corrected to use CartItem","from .forms import CartUpdateForm","","# Landing page: Redirects logged-in users to 'home' and shows options to non-logged-in users","def landing_page(request):","    if request.user.is_authenticated:","        return redirect('home')  # Redirect to home if the user is already logged in","    return render(request, 'airline/landing.html')  # Show login/register options for new users","","# Registration page","def register(request):","    if request.method == 'POST':","        form = UserCreationForm(request.POST)","        if form.is_valid():","            form.save()","            messages.success(request, f'Account created successfully! Please log in.')","            return redirect('login')  # Redirect to login page after successful registration","    else:","        form = UserCreationForm()","","    return render(request, 'airline/register.html', {'form': form})","","# Home page with flight search","@login_required","def home(request):","    flights = None","    if request.method == 'POST':","        source = request.POST.get('source')","        destination = request.POST.get('destination')","        date = request.POST.get('date')","","        if source and destination and date:","            # Filter flights based on user input","            flights = Flight.objects.filter(","                departure_city__iexact=source,","                arrival_city__iexact=destination,","                departure_time__date=date","            )","","    return render(request, 'airline/home.html', {'flights': flights})","","# Add flight to cart","@login_required","def add_to_cart(request, flight_id):","    flight = get_object_or_404(Flight, id=flight_id)","","    # Get passengers count from the form (or default to 1 if not provided)","    passengers = int(request.POST.get('passengers', 1))","","    # Check if the flight is already in the user's cart","    cart_item, created = CartItem.objects.get_or_create(user=request.user, flight=flight)","","    if created:","        cart_item.passengers = passengers","        cart_item.save()","        messages.success(request, f'{flight.flight_number} has been added to your cart.')","    else:","        cart_item.passengers += passengers  # If already in the cart, increase the count","        cart_item.save()","        messages.info(request, f'{passengers} more passengers added to your cart for {flight.flight_number}.')","","    return redirect('cart')","","# View to display the cart","@login_required","def cart(request):","    user_cart = CartItem.objects.filter(user=request.user)","    total_price = sum(item.flight.price * item.passengers for item in user_cart)","","    # Add the total price for each cart item to display in the template","    for item in user_cart:","        item.total_price = item.flight.price * item.passengers","","    return render(request, 'airline/cart.html', {'cart': user_cart, 'total_price': total_price})","","# Remove flight from the cart","@login_required","def remove_from_cart(request, cart_id):","    cart_item = get_object_or_404(CartItem, id=cart_id)","","    # Ensure that the cart item belongs to the current user","    if cart_item.user == request.user:","        cart_item.delete()","        messages.success(request, 'Flight removed from cart.')","    else:","        messages.error(request, 'You cannot remove an item from another user\\'s cart.')","","    return redirect('cart')","","# Update flight in the cart (number of passengers)","@login_required","def update_cart(request, cart_id):","    cart_item = get_object_or_404(CartItem, id=cart_id)","    if request.method == 'POST':","        form = CartUpdateForm(request.POST, instance=cart_item)","        if form.is_valid():","            form.save()","            messages.success(request, 'Cart updated successfully.')","            return redirect('cart')","    else:","        form = CartUpdateForm(instance=cart_item)","    return render(request, 'airline/update_cart.html', {'cart_item': cart_item, 'form': form})","","# Checkout page","@login_required","def checkout(request):","    user_cart = CartItem.objects.filter(user=request.user)","    total_price = sum(item.flight.price * item.passengers for item in user_cart)","","    # Placeholder for any additional checkout logic (e.g., payment integration)","    return render(request, 'airline/checkout.html', {'cart': user_cart, 'total_price': total_price})",""],"id":5},{"start":{"row":0,"column":0},"end":{"row":115,"column":0},"action":"insert","lines":["from django.shortcuts import render, redirect, get_object_or_404","from django.contrib.auth.forms import UserCreationForm","from django.contrib.auth.decorators import login_required","from django.contrib import messages","from .models import Flight, Cart  # Updated import to use Cart","from .forms import CartUpdateForm","","# Landing page: Redirects logged-in users to 'home' and shows options to non-logged-in users","def landing_page(request):","    if request.user.is_authenticated:","        return redirect('home')  # Redirect to home if the user is already logged in","    return render(request, 'airline/landing.html')  # Show login/register options for new users","","# Registration page","def register(request):","    if request.method == 'POST':","        form = UserCreationForm(request.POST)","        if form.is_valid():","            form.save()","            messages.success(request, f'Account created successfully! Please log in.')","            return redirect('login')  # Redirect to login page after successful registration","    else:","        form = UserCreationForm()","","    return render(request, 'airline/register.html', {'form': form})","","# Home page with flight search","@login_required","def home(request):","    flights = None","    if request.method == 'POST':","        source = request.POST.get('source')","        destination = request.POST.get('destination')","        date = request.POST.get('date')","","        if source and destination and date:","            # Filter flights based on user input","            flights = Flight.objects.filter(","                departure_city__iexact=source,","                arrival_city__iexact=destination,","                departure_time__date=date","            )","","    return render(request, 'airline/home.html', {'flights': flights})","","# Add flight to cart","@login_required","def add_to_cart(request, flight_id):","    flight = get_object_or_404(Flight, id=flight_id)","","    # Get passengers count from the form (or default to 1 if not provided)","    passengers = int(request.POST.get('passengers', 1))","","    # Check if the flight is already in the user's cart","    cart_item, created = Cart.objects.get_or_create(user=request.user, flight=flight)","","    if created:","        cart_item.passengers = passengers","        cart_item.save()","        messages.success(request, f'{flight.flight_number} has been added to your cart.')","    else:","        cart_item.passengers += passengers  # If already in the cart, increase the count","        cart_item.save()","        messages.info(request, f'{passengers} more passengers added to your cart for {flight.flight_number}.')","","    return redirect('cart')","","# View to display the cart","@login_required","def cart(request):","    user_cart = Cart.objects.filter(user=request.user)","    total_price = sum(item.flight.price * item.passengers for item in user_cart)","","    # Add the total price for each cart item to display in the template","    for item in user_cart:","        item.total_price = item.flight.price * item.passengers","","    return render(request, 'airline/cart.html', {'cart': user_cart, 'total_price': total_price})","","# Remove flight from the cart","@login_required","def remove_from_cart(request, cart_id):","    cart_item = get_object_or_404(Cart, id=cart_id)","","    # Ensure that the cart item belongs to the current user","    if cart_item.user == request.user:","        cart_item.delete()","        messages.success(request, 'Flight removed from cart.')","    else:","        messages.error(request, 'You cannot remove an item from another user\\'s cart.')","","    return redirect('cart')","","# Update flight in the cart (number of passengers)","@login_required","def update_cart(request, cart_id):","    cart_item = get_object_or_404(Cart, id=cart_id)","    if request.method == 'POST':","        form = CartUpdateForm(request.POST, instance=cart_item)","        if form.is_valid():","            form.save()","            messages.success(request, 'Cart updated successfully.')","            return redirect('cart')","    else:","        form = CartUpdateForm(instance=cart_item)","    return render(request, 'airline/update_cart.html', {'cart_item': cart_item, 'form': form})","","# Checkout page","@login_required","def checkout(request):","    user_cart = Cart.objects.filter(user=request.user)","    total_price = sum(item.flight.price * item.passengers for item in user_cart)","","    # Placeholder for any additional checkout logic (e.g., payment integration)","    return render(request, 'airline/checkout.html', {'cart': user_cart, 'total_price': total_price})",""]}],[{"start":{"row":105,"column":65},"end":{"row":105,"column":66},"action":"remove","lines":["m"],"id":6},{"start":{"row":105,"column":64},"end":{"row":105,"column":65},"action":"remove","lines":["e"]},{"start":{"row":105,"column":63},"end":{"row":105,"column":64},"action":"remove","lines":["t"]},{"start":{"row":105,"column":62},"end":{"row":105,"column":63},"action":"remove","lines":["i"]},{"start":{"row":105,"column":61},"end":{"row":105,"column":62},"action":"remove","lines":["_"]}],[{"start":{"row":105,"column":72},"end":{"row":105,"column":73},"action":"remove","lines":["m"],"id":7},{"start":{"row":105,"column":71},"end":{"row":105,"column":72},"action":"remove","lines":["e"]},{"start":{"row":105,"column":70},"end":{"row":105,"column":71},"action":"remove","lines":["t"]},{"start":{"row":105,"column":69},"end":{"row":105,"column":70},"action":"remove","lines":["i"]},{"start":{"row":105,"column":68},"end":{"row":105,"column":69},"action":"remove","lines":["_"]}],[{"start":{"row":81,"column":0},"end":{"row":91,"column":27},"action":"remove","lines":["def remove_from_cart(request, cart_id):","    cart_item = get_object_or_404(Cart, id=cart_id)","","    # Ensure that the cart item belongs to the current user","    if cart_item.user == request.user:","        cart_item.delete()","        messages.success(request, 'Flight removed from cart.')","    else:","        messages.error(request, 'You cannot remove an item from another user\\'s cart.')","","    return redirect('cart')"],"id":9},{"start":{"row":81,"column":0},"end":{"row":93,"column":27},"action":"insert","lines":["def remove_from_cart(request, cart_id):","    # Ensure the cart item belongs to the current user","    cart_item = Cart.objects.filter(id=cart_id, user=request.user).first()","    ","    if not cart_item:","        # Handle the case where the cart item doesn't exist or doesn't belong to the user","        messages.error(request, 'Cart item not found or does not belong to you.')","        return redirect('cart')","","    # If cart item exists, delete it","    cart_item.delete()","    messages.success(request, 'Flight removed from cart.')","    return redirect('cart')"]}],[{"start":{"row":27,"column":0},"end":{"row":27,"column":2},"action":"insert","lines":["# "],"id":10},{"start":{"row":28,"column":0},"end":{"row":28,"column":2},"action":"insert","lines":["# "]},{"start":{"row":29,"column":0},"end":{"row":29,"column":2},"action":"insert","lines":["# "]},{"start":{"row":30,"column":0},"end":{"row":30,"column":2},"action":"insert","lines":["# "]},{"start":{"row":31,"column":0},"end":{"row":31,"column":2},"action":"insert","lines":["# "]},{"start":{"row":32,"column":0},"end":{"row":32,"column":2},"action":"insert","lines":["# "]},{"start":{"row":33,"column":0},"end":{"row":33,"column":2},"action":"insert","lines":["# "]},{"start":{"row":35,"column":0},"end":{"row":35,"column":2},"action":"insert","lines":["# "]},{"start":{"row":36,"column":0},"end":{"row":36,"column":2},"action":"insert","lines":["# "]},{"start":{"row":37,"column":0},"end":{"row":37,"column":2},"action":"insert","lines":["# "]},{"start":{"row":38,"column":0},"end":{"row":38,"column":2},"action":"insert","lines":["# "]},{"start":{"row":39,"column":0},"end":{"row":39,"column":2},"action":"insert","lines":["# "]},{"start":{"row":40,"column":0},"end":{"row":40,"column":2},"action":"insert","lines":["# "]},{"start":{"row":41,"column":0},"end":{"row":41,"column":2},"action":"insert","lines":["# "]},{"start":{"row":43,"column":0},"end":{"row":43,"column":2},"action":"insert","lines":["# "]}],[{"start":{"row":43,"column":71},"end":{"row":44,"column":0},"action":"remove","lines":["",""],"id":11}],[{"start":{"row":43,"column":71},"end":{"row":44,"column":0},"action":"insert","lines":["",""],"id":12},{"start":{"row":44,"column":0},"end":{"row":45,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":45,"column":0},"end":{"row":72,"column":0},"action":"insert","lines":["from django.shortcuts import render","from django.contrib.auth.decorators import login_required","from .models import Flight","","@login_required","def home(request):","    # Default flights (first 5 flights) when no search is performed","    flights = Flight.objects.all()[:5]","    ","    if request.method == 'POST':","        source = request.POST.get('source')","        destination = request.POST.get('destination')","        date = request.POST.get('date')","","        if source and destination and date:","            # Filter flights based on user input","            flights = Flight.objects.filter(","                departure_city__iexact=source,","                arrival_city__iexact=destination,","                departure_time__date=date","            )","","        if not flights:","            # If no flights are found, show a message","            flights = None  # This will display the \"no flights found\" message in the template","    ","    return render(request, 'airline/home.html', {'flights': flights})",""],"id":13}]]},"ace":{"folds":[],"scrolltop":682.4999936676023,"scrollleft":0,"selection":{"start":{"row":72,"column":0},"end":{"row":72,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":6,"state":"start","mode":"ace/mode/python"}},"timestamp":1732996871034,"hash":"ffb50bd2f8d053efc2d1de8183eaefd60ebbe672"}