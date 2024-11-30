from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Flight, Cart  # Updated import to use Cart
from .forms import CartUpdateForm

# Landing page: Redirects logged-in users to 'home' and shows options to non-logged-in users
def landing_page(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to home if the user is already logged in
    return render(request, 'airline/landing.html')  # Show login/register options for new users

# Registration page
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account created successfully! Please log in.')
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()

    return render(request, 'airline/register.html', {'form': form})

# Home page with flight search
# @login_required
# def home(request):
#     flights = None
#     if request.method == 'POST':
#         source = request.POST.get('source')
#         destination = request.POST.get('destination')
#         date = request.POST.get('date')

#         if source and destination and date:
#             # Filter flights based on user input
#             flights = Flight.objects.filter(
#                 departure_city__iexact=source,
#                 arrival_city__iexact=destination,
#                 departure_time__date=date
#             )

#     return render(request, 'airline/home.html', {'flights': flights})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Flight

@login_required
def home(request):
    # Default flights (first 5 flights) when no search is performed
    flights = Flight.objects.all()[:5]
    
    if request.method == 'POST':
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        date = request.POST.get('date')

        if source and destination and date:
            # Filter flights based on user input
            flights = Flight.objects.filter(
                departure_city__iexact=source,
                arrival_city__iexact=destination,
                departure_time__date=date
            )

        if not flights:
            # If no flights are found, show a message
            flights = None  # This will display the "no flights found" message in the template
    
    return render(request, 'airline/home.html', {'flights': flights})

# Add flight to cart
@login_required
def add_to_cart(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)

    # Get passengers count from the form (or default to 1 if not provided)
    passengers = int(request.POST.get('passengers', 1))

    # Check if the flight is already in the user's cart
    cart_item, created = Cart.objects.get_or_create(user=request.user, flight=flight)

    if created:
        cart_item.passengers = passengers
        cart_item.save()
        messages.success(request, f'{flight.flight_number} has been added to your cart.')
    else:
        cart_item.passengers += passengers  # If already in the cart, increase the count
        cart_item.save()
        messages.info(request, f'{passengers} more passengers added to your cart for {flight.flight_number}.')

    return redirect('cart')

# View to display the cart
@login_required
def cart(request):
    user_cart = Cart.objects.filter(user=request.user)
    total_price = sum(item.flight.price * item.passengers for item in user_cart)

    # Add the total price for each cart item to display in the template
    for item in user_cart:
        item.total_price = item.flight.price * item.passengers

    return render(request, 'airline/cart.html', {'cart': user_cart, 'total_price': total_price})

# Remove flight from the cart
@login_required
def remove_from_cart(request, cart_id):
    # Ensure the cart item belongs to the current user
    cart_item = Cart.objects.filter(id=cart_id, user=request.user).first()
    
    if not cart_item:
        # Handle the case where the cart item doesn't exist or doesn't belong to the user
        messages.error(request, 'Cart item not found or does not belong to you.')
        return redirect('cart')

    # If cart item exists, delete it
    cart_item.delete()
    messages.success(request, 'Flight removed from cart.')
    return redirect('cart')

# Update flight in the cart (number of passengers)
@login_required
def update_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)
    if request.method == 'POST':
        form = CartUpdateForm(request.POST, instance=cart_item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cart updated successfully.')
            return redirect('cart')
    else:
        form = CartUpdateForm(instance=cart_item)
    return render(request, 'airline/update_cart.html', {'cart': cart, 'form': form})

# Checkout page
@login_required
def checkout(request):
    user_cart = Cart.objects.filter(user=request.user)
    total_price = sum(item.flight.price * item.passengers for item in user_cart)

    # Placeholder for any additional checkout logic (e.g., payment integration)
    return render(request, 'airline/checkout.html', {'cart': user_cart, 'total_price': total_price})
