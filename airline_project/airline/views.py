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
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Account created successfully! Please log in.')
#             return redirect('login')  # Redirect to login page after successful registration
#     else:
#         form = UserCreationForm()

#     return render(request, 'airline/register.html', {'form': form})

# import boto3
# import json
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .forms import CustomUserCreationForm

# # AWS Configuration
# AWS_REGION = "us-east-1"  # e.g., "us-east-1"
# TOPIC_NAME = "new-user-registration-topic"  # Name of your SNS topic

# # AWS SNS: Create or Retrieve Topic ARN
# def get_or_create_sns_topic(topic_name):
#     sns_client = boto3.client('sns', region_name=AWS_REGION)
#     response = sns_client.create_topic(Name=topic_name)
#     return response['TopicArn']

# # AWS SNS: Publish message
# def publish_to_sns(topic_arn, message, subject=None):
#     sns_client = boto3.client('sns', region_name=AWS_REGION)
#     response = sns_client.publish(
#         TopicArn=topic_arn,
#         Message=message,
#         Subject=subject if subject else "New User Registration"
#     )
#     return response

# # Registration page
# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()

#             # Save additional fields
#             user.first_name = form.cleaned_data['first_name']
#             user.last_name = form.cleaned_data['last_name']
#             user.email = form.cleaned_data['email']
#             user.save()

    #         # Prepare SNS notification
    #         try:
    #             topic_arn = get_or_create_sns_topic(TOPIC_NAME)
    #             sns_message = json.dumps({
    #                 "event": "User Created",
    #                 "username": user.username,
    #                 "first_name": user.first_name,
    #                 "last_name": user.last_name,
    #                 "email": user.email,
    #                 "phone_number": form.cleaned_data['phone_number'],
    #             })

    #             # Publish to SNS
    #             publish_to_sns(topic_arn, sns_message, subject="New User Registered")
    #             messages.success(request, "Account created successfully! Notification sent.")
    #         except Exception as e:
    #             messages.error(request, f"Account created, but failed to send notification: {str(e)}")

    #         return redirect('login')
    # else:
    #     form = CustomUserCreationForm()

    # return render(request, 'airline/register.html', {'form': form})
    
import boto3
import uuid
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
  # Assuming you have a Custom User Creation form

# AWS SNS and SQS Configuration
TOPIC_NAME = "UserRegistrationNotifications"  # Replace with your desired topic name
ADMIN_EMAIL = "snehalpkolhe@gmail.com"      # Replace with your admin email
SQS_QUEUE_URL = "https://sqs.us-east-1.amazonaws.com/513189235636/PendingMails.fifo"  # Replace with your SQS URL

# Create SNS topic
def create_sns_topic(topic_name):
    sns_client = boto3.client('sns')
    response = sns_client.create_topic(Name=topic_name)
    return response['TopicArn']

# Subscribe email to SNS topic
def subscribe_email_to_topic(topic_arn, email_address):
    sns_client = boto3.client('sns')
    sns_client.subscribe(
        TopicArn=topic_arn,
        Protocol='email',
        Endpoint=email_address
    )
    print(f"Subscription request sent to {email_address}")

# Send notification to SNS
def send_user_creation_notification(topic_arn, username):
    sns_client = boto3.client('sns')
    message = f"A new user has registered with the email: {username}."
    sns_client.publish(
        TopicArn=topic_arn,
        Message=message,
        Subject="New User Registration"
    )

# Send message to SQS
def send_message_to_sqs(username):
    sqs_client = boto3.client('sqs')
    # queue_url = 'https://sqs.us-east-1.amazonaws.com/513189235636/PendingMails.fifo'
    message_body = f"New user registered with email: {username}"

    response = sqs_client.send_message(
        QueueUrl=SQS_QUEUE_URL,
        MessageBody=message_body,
        MessageGroupId='user-registration',
        MessageDeduplicationId=str(uuid.uuid4())
    )
    print(f"Message sent to SQS: {response['MessageId']}")

# Registration view for user creation
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            

            # Authenticate and log in the user
            user = authenticate(username=user.username, password=form.cleaned_data['password1'])
            if user is not None:
                login(request, user)
                messages.success(request, "Account created successfully! You are now logged in.")

                # SNS and SQS logic
                try:
                    topic_arn = create_sns_topic(TOPIC_NAME)
                    subscribe_email_to_topic(topic_arn, ADMIN_EMAIL)
                    send_user_creation_notification(topic_arn, user.email)
                    send_message_to_sqs(user.username)
                except Exception as e:
                    messages.error(request, f"Error sending notifications: {e}")

                return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'airline/register.html', {'form': form})



# Sorting function for flights by price
def sort_prices_low_to_high(flights):
    """Sort flights by price in ascending order."""
    return sorted(flights, key=lambda flight: flight.price)

# Home page with flight search
@login_required
def home(request):
    flights = None
    default_flights = Flight.objects.all()[:5]  # Default flights when no search is performed

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

    # If there are flights, sort them by price
    if flights:
        flights = sort_prices_low_to_high(flights)
    else:
        # If no flights match, show default flights
        flights = default_flights

    return render(request, 'airline/home.html', {'flights': flights, 'default_flights': default_flights})

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

# Sorting function for cart items by price
def sort_cart_by_price(cart_items):
    """Sort cart items by total price in ascending order."""
    return sorted(cart_items, key=lambda item: item.total_price)

# View to display the cart
@login_required
def cart(request):
    user_cart = Cart.objects.filter(user=request.user)
    total_price = sum(item.flight.price * item.passengers for item in user_cart)

    # Add the total price for each cart item to display in the template
    for item in user_cart:
        item.total_price = item.flight.price * item.passengers

    # Sort the cart items by total price
    user_cart = sort_cart_by_price(user_cart)

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
