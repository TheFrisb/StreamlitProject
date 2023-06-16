from django.shortcuts import render, redirect 
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from .sending_mails import elasticemail
from .models import *
import uuid
from decouple import config
import stripe
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from django.utils import timezone

# Set your secret key. Remember to switch to your live secret key in production!
stripe.api_key = config('STRIPE_SECRET_KEY')



def home(request): # this is the view that serves the home page
    #response = requests.get('/login/')
    #print(response)
    products = Product.objects.all() # this is a queryset, it returns all products
    context = {
        'products': products,
        'title': 'Home'
    }
    if request.user.is_authenticated: # check if the user is logged in
        user_profile = UserProfile.objects.get(user=request.user) # get the user profile of the logged in user
        print(user_profile.notification)
        if user_profile.notification is not None:
            context['notification'] = user_profile.notification
            user_profile.notification = None
            user_profile.save()
        context['user_profile'] = user_profile 
    return render(request, 'shop/home.html', context) # render the home.html template with the context dictionary


#create a view that serves a  streamlit dashboard
def streamlit_dashboard(request):
    if request.user.is_authenticated: # check if the user is logged in
        userProfile = UserProfile.objects.get(user=request.user) # get user_profile
        userProfile.streamlit_token = str(uuid.uuid4())
        userProfile.streamlit_token_created_at = timezone.now()
        userProfile.save()

        return redirect(config('STREAMLIT_URL') + '?user=' + str(userProfile.streamlit_token)) #change this to streamlit url in production or store it as .env file
    else:
        pass


def register_user(request): # this is the view that serves the register page

    if request.method == 'POST':
        email = request.POST.get('email') # get the email from the form
        password = request.POST.get('password') # get the password from the form
        # make username from email but make it unique
        username = email.split('@')[0] + '_' + str(uuid.uuid4())[:8] # this is the username and made unique by adding a random string to the end
      
        
        existing_user = User.objects.filter(email=email).first() # check for existing user

        if existing_user:
            print(existing_user)
            return JsonResponse({'status': 'Email existing!'}, status=404)


        registration_link = request.build_absolute_uri() + 'confirm/' + str(uuid.uuid4()) + '/' # this is the registration link that will be sent to the user's email
        new_user = User.objects.create_user(username=username, email=email, password=password, is_active=False) # create a new user object
        link_ob = RegistrationLink.objects.create(user=new_user, link=registration_link) # create a new RegistrationLink object

        print('User created!', new_user)
        try:
            elasticemail.send_user_confirmation_mail(new_user, link_ob) # send the user a confirmation email
            print('Email sent!')
        except:
            print('Mail failed')
            link_ob.delete()
            new_user.delete()
            return JsonResponse({'status': 'Mail limit reached!'}, status=401)
        
        return JsonResponse({'status': 'success'}, status=201)
    else:
        return JsonResponse({'status': 'Wrong request!'}, status=400)
    

def confirm_user(request, registration_link): # this is the view that confirms the user when he clicks on the registration link

    try:
        link_ob = RegistrationLink.objects.get(link=request.build_absolute_uri()) # get the RegistrationLink object
        confirmed_user = link_ob.user # get the user from the RegistrationLink object
        confirmed_user.is_active = True # set the user to active, that means he is able to login
        confirmed_user.save() # save the user
        link_ob.delete() # delete the RegistrationLink object
        return redirect('shop-home') # redirect to the home page
    
    except User.DoesNotExist: # if the user does not exist, for example a fake or a broken link..
        return redirect('shop-home') # redirect to the home page


def login_user(request): # this is the view that serves the login page
    
    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email) # get the user object
        except User.DoesNotExist:
            return JsonResponse({'status': 'User does not exist!'}, status=404) # if the user does not exist, return a 404 error
        
        if user.check_password(password): # check if the password is correct for that user
            if user.is_active == False: # check if the user is active
                return JsonResponse({'status': 'User is not active!', 'text': 'Unverified email'}, status=401) # if the user is not active, return a 401 error, which is handled in main.js
            
            else: # if the user is active, log him in
                user = authenticate(request, email=email, password=password) # authenticate the user (verify his credentials)
                login(request, user) # login the user
                return JsonResponse({'status': 'success'}, status=200) # return a 200 status code, which is handled in main.js
        else:
            return JsonResponse({'status': 'Wrong password!'}, status=403) # if the password is wrong, return a 403 error
    else:
        return JsonResponse({'status': 'Wrong request!'}, status=400) # if the request is not a POST request, return a 400 error
    

def logout_user(request): # this is the view that logs the user out
    if request.user.is_authenticated: # check if the user is logged in
            logout(request) # logout the user
            return redirect('shop-home') # redirect to the home page
    

def change_password(request): # this is the view that changes the password of the user
    if request.method == 'POST': 

        user = request.user # get the user object
        current_password = request.POST.get('current_password') # get the current password from the form
        password = request.POST.get('password') # get the new password from the form
        
        if not user.check_password(current_password): # check if the current password is correct
            return JsonResponse({'status': 'Wrong password!'}, status=403) # if the password is wrong, return a 403 error


        user.set_password(password) # set the new password
        user.save() # save the user
        update_session_auth_hash(request, user) # update the session auth hash

        return JsonResponse({'status': 'success'}, status=200) # return a 200 status code, which is handled in main.js
    else:
        return JsonResponse({'status': 'Wrong request!'}, status=400) # if the request is not a POST request, return a 400 error
    




def create_checkout_session(request): #
    if request.method == 'POST':
        try:
            
            product_id = request.POST.get('product_id') # get the product id from the form
            product = Product.objects.get(id=product_id) # get the product object
            django_user_id = request.user.id
            if request.user.email == '': # check if the user has an email for auto filling the email and connecting the payment method in stripe
                email = None # if the user has no email, set the email to None
            else:
                email = request.user.email # if the user has an email, set the email to the user's email
            price = float(product.price)
            user_profile = UserProfile.objects.get(user=request.user)
            if user_profile.active_coupon is not None:
                price = price - price * user_profile.active_coupon.get_discount
                print(price)

            checkout_session = stripe.checkout.Session.create( # create a checkout session
                line_items=[
                {
                    'price_data': {
                        'currency': 'eur',
                        'product_data': {
                            'name': product.name,
                            'description': 'Enables you ' + str(product.use_count) + ' uses of the app',
                        },
                        'unit_amount': int(price*100),  # Stripe expects the amount in cents
                    },
                    'quantity': 1,
                },
            ],
                mode='payment',
                success_url='http://127.0.0.1:8000/', # change this to home
                cancel_url='http://127.0.0.1:8000/', #change this to home
                customer_email=email,
                payment_intent_data={
                                        'metadata': {
                                            'django_user_id': str(request.user.id),
                                            'product_id': str(product.id),
                                        }
                }
                

            )
            '''
                line_items is a list of dictionaries, each dictionary represents a product in the checkout session, this is the stripe api
                price_data is a dictionary that contains product data, currency and price
                product_data is a dictionary that contains the name and description of the product
                unit_amount is the price of the product in cents (stripe expects the amount in cents)
                quantity is the quantity of the product ordered
                mode is the mode of the checkout session, in this case it is payment
                success_url is the url that the user is redirected to after a successful payment
                cancel_url is the url that the user is redirected to after a canceled payment
                customer_email is the email of the customer, if the customer has no email, it is set to None
            '''
        except Exception as e: # if there is an error, return it
            return str(e) # this is for debugging purposes

        return redirect(checkout_session.url, code=303) # redirect the user to the checkout session url
    else:
        return JsonResponse({'status': 'Wrong request!'}, status=400) # if the request is not a POST request, return a 400 error
    



# This is your Stripe CLI webhook secret for testing your endpoint locally.

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
        
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)

    # Handle the event based on its type
    if event.type == 'payment_intent.succeeded':
        payment_intent = event.data.object
        metadata = payment_intent['metadata']

        django_user_id = int(metadata.get('django_user_id'))
        product_id = int(metadata.get('product_id'))

        user_profile = UserProfile.objects.get(user__id=django_user_id)
        product = Product.objects.get(id=product_id)
        user_profile.credits_balance += product.use_count
        print(user_profile.notification)
        user_profile.notification = f'You have successfully purchased {product.use_count} credits!'
        if user_profile.active_coupon is not None:
            user_profile.active_coupon = None
        user_profile.save()

        OrderItem.objects.create(user=user_profile.user, product=product, price=product.price, use_count=product.use_count)
        print('Payment successful!')
    elif event.type == "payment_intent.payment_failed":
        intent = event['data']['object']
        metadata = intent['metadata']
        django_user_id = int(metadata.get('django_user_id'))
        product_id = int(metadata.get('product_id'))
        error_message = intent['last_payment_error']['message'] if intent.get('last_payment_error') else None

        user_profile = UserProfile.objects.get(user__id=django_user_id)
        product = Product.objects.get(id=product_id)
        user_profile.notification = f'Purchase failed! Possible reason: {error_message}'
        user_profile.save()
        print("Failed: ", intent['id']), error_message

    return HttpResponse(status=200)


def send_contact_message(request):  # this is the view that sends the contact message
    if request.method == 'POST':
        from_mail = request.POST.get('from_mail') # get the email from the form
        message = request.POST.get('message') # get the message from the form
        try:
            elasticemail.send_contact_message(from_mail, message) # send the email
            print('Email sent!')
        except:
            print('Email could not be sent!')
            pass
        return JsonResponse({'status': 'success'}, status=201) # return a 201 status code, which is handled in main.js
    else:
        return JsonResponse({'status': 'Wrong request!'}, status=400) # if the request is not a POST request, return a 400 error
    

def add_coupon(request):
    if request.method == 'POST':
        coupon_name = request.POST.get('coupon_name')
        try:
            coupon = Coupon.objects.get(name=coupon_name)
            if not coupon.is_active:
                return JsonResponse({'status': 'error'}, status = 400)
        except:
            return JsonResponse({'status': 'error'}, status = 400)
        
        user_profile = UserProfile.objects.get(user=request.user)
        user_profile.active_coupon = coupon
        user_profile.save()
        return JsonResponse({'status': 'success', 'discount': coupon.get_discount}, status=201)
    else:
        return JsonResponse({'status': 'Wrong request!'}, status=400) # if the request is not a POST request, return a 400 error

@csrf_exempt
def reduce_credits(request): # handle streamlit user
    if request.method == 'POST':
        user_token = request.POST.get('user_token') # get token
        try:
            user_profile = UserProfile.objects.get(streamlit_token=user_token) # get user or return error
        except UserProfile.DoesNotExist:
            return HttpResponse("User not found", status=404)
        print(user_profile)
        if user_profile.credits_balance > 0: # check if he has credits
            user_profile.credits_balance -= 1 # Remove a credit
            user_profile.save() # Save userprofile
            print(user_profile.credits_balance)
            try:
                elasticemail.notify_user_for_credit_spent(user_profile) # send mail for reduced credit
            except:
                pass

            return HttpResponse("Credits reduced successfully", status=200)
        else:
            print(user_profile.credits_balance)
            return HttpResponse("Not enough credits", status=403) # send error for not enough credits

    else:
        return HttpResponse("Invalid request method", status=405)