
from django.shortcuts import render, redirect
from .models import UserDetails,UserProduct
from django.http import HttpResponse
from app.pac import get_pac_prediction

def index(request):
    return render(request, 'home.html')

def clogin(request):
    if request.method == 'POST':
        getusername = request.POST.get('username')
        getpassword = request.POST.get('password')
        try:
            UserDetails.objects.get(username=getusername, password=getpassword)
            return redirect('manage')
        except:
            return HttpResponse('You are a Kulla Nari')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        organization = request.POST['organization']
        phone = request.POST['phone']
        email = request.POST['email']
        order = request.POST['order']
        user_type = request.POST['type']
        customization = request.POST['customization']

        # Create a new UserDetails object and save it to the database
        UserDetails.objects.create(
            username=username,
            password=password,
            organization=organization,
            phone=phone,
            email=email,
            order=order,
            type=user_type,
            customization=customization,
        )

        UserProduct.objects.create(
            name=username,
            organize=organization,
            ph=phone,
            mail=email,
            orders=order,
            types=user_type,
            product_customization=customization,
        )

        # Redirect to the login page after a successful sign-up
        return redirect('clogin')

    return render(request, 'csignup.html')

def manage(request):
    details = UserDetails.objects.all()
    return render(request, 'requirements.html', {'details': details})

def RDteam(request):
    return render(request, 'R&Dteam.html')

def product(request):
    details = UserProduct.objects.all()

    # Initialize an empty list to store the results
    results = []

    # Iterate through UserProduct objects and apply PAC algorithm
    for user_product in details:
        order = user_product.orders
        suit_type = user_product.types
        customization = user_product.product_customization

        # Use the PAC algorithm to get the prediction
        pac_result = get_pac_prediction(order, suit_type, customization)

        # Update the product field in UserProduct model
        user_product.product = pac_result
        user_product.save()

        # Append the result to the list
        results.append({
            'name': user_product.name,
            'organize': user_product.organize,
            'ph': user_product.ph,
            'mail': user_product.mail,
            'orders': user_product.orders,
            'types': user_product.types,
            'product_customization': user_product.product_customization,
            'product': pac_result,
        })

    return render(request, 'product.html', {'details': results})


