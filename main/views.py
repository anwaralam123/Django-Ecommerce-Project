import datetime
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .forms import signupform,RatingForm,ShippingAddressForm
from django.db.models import Q
from .models import Company, ProductCategory,Product,Image,ProductDetail,ProductDescription,AdditionalInformation,Rating,Cart,Cart_Total,ShippingAddress
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.conf import settings

import stripe
# print(">>>>>>>>>>",settings.STRIPE_SECRET_KEY)
# stripe.api_key ="sk_test_51P8RZ5P1a9M62WvFK6c7CEKg6brlXVPOakDuywWalGqsdZN2PxHrzFHg7LwJjgxagKp4M6WsC9mstO8olamOU4ar00SIc0S2E1"
stripe.api_key=settings.STRIPE_SECRET_KEY
print('my stripe key>>>>>>',stripe.api_key)

def charge(request):
    username=User.objects.filter(username=request.user).first()
    email=username.email
    amount=Cart_Total.objects.filter(user=request.user).first()
    total_amount=amount.total
    if request.method == "POST":
        
        customer = stripe.Customer.create(
            name=username.first_name,
            email=email,
            source="tok_visa"
        )
        print('Customer detail:',customer)
        # print(request.POST)
        
        # token = stripe.Token.create(
        #     card={
        #         "number": str(request.POST.get('cardnumber')),
        #         "exp_month": int(request.POST.get('mm')),
        #         "exp_year": int(request.POST.get('yy')),
        #         "cvc": str(request.POST.get('number'))
        #     },
        # )
        # print('My Token ID is>>>>>>',token.id)

        # Charge the customer
        charge = stripe.Charge.create(
            amount=int((total_amount)*100),
            currency="usd",
            customer=customer.id
        )
        # print(charge)
        
    return redirect('checkoutcomplete')







# Create your views here.

def index(request):
    mobile_name=request.GET.get('mobile')
    tablet_name=request.GET.get('tablet')
    if mobile_name:
        mobiles=Product.objects.filter(product_category__category_name__iexact='Mobile Phones', company__company_name=mobile_name)
    else:
        mobiles=Product.objects.filter(product_category__category_name__iexact='Mobile Phones')
    
    if tablet_name:
        tablets=Product.objects.filter(product_category__category_name__iexact='tablet',company__company_name=tablet_name)
    else:    
        tablets=Product.objects.filter(product_category__category_name__iexact='tablet')
    mobilecompany=Company.objects.filter(product_category__category_name='Mobile Phones')
    tabletcompany=Company.objects.filter(product_category__category_name='Tablet')
    trends=Product.objects.filter(trending_items=True)
    categories=ProductCategory.objects.all()
    if request.user.is_authenticated:
       carts =Cart.objects.filter(user=request.user)
    else:
        carts=None
    context={
        'mobiles':mobiles,
        'tablets':tablets,
        'mobs':mobilecompany,
        'tabs':tabletcompany,
        'trends':trends,
        'categories':categories,
        'carts':carts
    }
    return render(request,'main/index.html',context)




def about_us(request):
    return render(request,'main/about_us.html')


def contact_us(request):
    return render(request,'main/contact_us.html')


def faq(request):
    return render(request,'main/faq.html')


def myaccount(request):
    return render(request,'main/my_account.html')


def checkout_cart(request,id):
    detailId=ProductDetail.objects.get(product=id)
    prod=Product.objects.get(id=id)
    if prod:
        if(Cart.objects.filter(user=request.user,product=prod)):
            return redirect('showcart')
        else:        
            cart=Cart(user=request.user,product=prod,product_detail=detailId)
            cart.total_amount=cart.product_qty * cart.product.discount_price
            cart.save()
            return redirect('showcart')


def show_cart(request):
    if request.user.is_authenticated:
       carts =Cart.objects.filter(user=request.user)
    else:
        carts=None
    subtotal_list=[]    
    cart_subtotal=Cart.objects.filter(user=request.user)
    if cart_subtotal:
        for p in cart_subtotal:
            subtotal_list.append(p.total_amount)
            subtotal=sum(subtotal_list)
        shipping_price=100.0
        total_with_shipping=subtotal+shipping_price
    context={
        'carts':carts,
        'subtotal':subtotal,
        'total':total_with_shipping
    }
    return render(request,'main/checkout_cart.html',context)

def plus_cart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        c=Cart.objects.filter(product=prod_id,user=request.user).first()
        c.product_qty+=1
        c.total_amount=c.product_qty * c.product.discount_price
        c.save()
        subtotal_list=[]    
        cart_subtotal=Cart.objects.filter(user=request.user)
        if cart_subtotal:
            for p in cart_subtotal:
                subtotal_list.append(p.total_amount)
            subtotal=sum(subtotal_list)
            # print(subtotal)
        shipping_price=100.0
        total_with_shipping=subtotal+shipping_price
        # print(total_with_shipping)
        data = {'quantity': c.product_qty,'amount':c.total_amount,'subtotal':subtotal,'total':total_with_shipping}
        return JsonResponse(data)
    

def minus_cart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        c=Cart.objects.filter(product=prod_id,user=request.user).first()
        # if c.product_qty>1:
        c.product_qty-=1
        c.total_amount=c.product_qty*c.product.discount_price
        c.save()
        subtotal_list=[]    
        cart_subtotal=Cart.objects.filter(user=request.user)
        if cart_subtotal:
            for p in cart_subtotal:
                subtotal_list.append(p.total_amount)
            subtotal=sum(subtotal_list)
        shipping_price=100.0
        total_with_shipping=subtotal+shipping_price
        data = {'quantity': c.product_qty,'amount':c.total_amount,'subtotal':subtotal,'total':total_with_shipping}
        return JsonResponse(data)

def remove_cart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        c=Cart.objects.filter(product=prod_id,user=request.user).first()
        c.delete()
        subtotal_list=[]    
        cart_subtotal=Cart.objects.filter(user=request.user)
        if cart_subtotal:
            for p in cart_subtotal:
                subtotal_list.append(p.total_amount)
            subtotal=sum(subtotal_list)
            # print(subtotal)
        shipping_price=100.0
        total_with_shipping=subtotal+shipping_price
        data = {'subtotal':subtotal,'total':total_with_shipping}
        return JsonResponse(data)


def checkout_info(request):
    # if request.method == 'POST':
    #     fm=ShippingAddressForm(request.POST)
    #     if fm.is_valid():
    #         shipping=fm.save(commit=False)
    #         shipping.user=request.user
    #         fm.save()
    #         fm=ShippingAddressForm()
    #         return redirect('checkoutpayment')
    # else:
    #     fm=ShippingAddressForm()
    #     print('Kuch ni bus esy e')

    if not Cart_Total.objects.filter(user=request.user).exists():
        subtotal_list=[]    
        cart_subtotal=Cart.objects.filter(user=request.user)
        if cart_subtotal:
            for p in cart_subtotal:
                subtotal_list.append(p.total_amount)
                subtotal=sum(subtotal_list)
                # print(subtotal)
            shipping_price=100.0
            total_with_shipping=subtotal+shipping_price
            # print(total_with_shipping)
            ct=Cart_Total(user=request.user,sub_total=subtotal,total=total_with_shipping)
            ct.save()
            return redirect('shipping')
    else:
        cart_subtotal = Cart.objects.filter(user=request.user)
        subtotal_list=[]
        if cart_subtotal:
            for p in cart_subtotal:
                subtotal_list.append(p.total_amount)
                subtotal=sum(subtotal_list)
                shipping_price = 100.00
                total_with_shipping = subtotal + shipping_price
            
            cart_total = Cart_Total.objects.filter(user=request.user).first()
            cart_total.sub_total = subtotal
            cart_total.total = total_with_shipping
            cart_total.save()
            return redirect('shipping')

    # if request.method=='POST':
    #     fm=ShippingAddressForm(request.POST)
    #     print(fm)
    #     if fm.is_valid():
    #         fm.save()
    #         fm=ShippingAddressForm()
    #         return redirect('checkoutpayment')
    # else:
    #     fm=ShippingAddressForm()
    #     print('Kuch ni bus esy e')
    return render(request,'main/checkout_info.html')


def shipping_address(request):
    
    if request.method == 'POST':
        
        fm=ShippingAddressForm(request.POST)
        if fm.is_valid():
            shipping=fm.save(commit=False)
            shipping.user=request.user
            fm.save()
            fm=ShippingAddressForm()
            return redirect('checkoutpayment')
    else:
        fm=ShippingAddressForm()
        print('Kuch ni bus esy e')
    return render(request,'main/checkout_info.html',{'form':fm})

# def create_checkout_session(request):
#     prod_total=Cart_Total.objects.filter(user=request.user).first()
#     print(prod_total.total)
#     if request.method == 'POST':
#         checkout_sessoion=stripe.checkout.Session.create(
#             line_items=[
#                 {
#                     'price_data':{
#                         'currency':'usd',
#                         'unit_amount':int(prod_total.total*100),
#                         'product_data':{
#                             'name':'Nomi'
#                         },
#                     },
#                     'quantity':1
#                 },
#             ],
#             mode='payment',
#             success_url="http://127.0.0.1:8000/checkout-complete/"
#         )
#         return redirect(checkout_sessoion.url,code=303)

def checkout_payment(request):
    return render(request,'main/checkout_payment.html')


def checkout_complete(request):
    items=Cart_Total.objects.filter(user=request.user).first()
    cart_items=Cart.objects.filter(user=request.user)
    print("***********>>>>>>>>",cart_items)
    # total_amount=items.total
    date=datetime.datetime.now()
    delivery_date_delta=datetime.timedelta(days=2)
    delivery_date=date+delivery_date_delta
    context={
        'items':items,
        'cart_items':cart_items,
        'date':date,
        'delivery_date':delivery_date
    }
    return render(request,'main/checkout_complete.html',context)


def product_detail(request,id):
    print(request.POST)
    if request.method=='POST':
        form=RatingForm(request.POST)
        if form.is_valid():
            rating=form.save(commit=False)
            rating.user=request.user
            rating.product_id=id
            rating.rate=request.POST.get('rating')
            rating.save()
            return redirect('productinfo',id=id)
    else:    
        form=RatingForm()
        
    product=Product.objects.filter(id=id).first()
    product_images=Image.objects.filter(product=id)
    products=ProductDetail.objects.get(product=id)
    related_products=Product.objects.filter(product_category=product.product_category).exclude(id=id)[:6]
    product_descriptions=ProductDescription.objects.filter(product=id)
    additionalinfo=AdditionalInformation.objects.filter(product=id)
    additional=additionalinfo.values_list('additional_info__product__product_name',flat=True)
    # ratings=Rating.objects.filter(product=id)
    ratings=Rating.objects.filter(product=id).order_by("-rate")
    # print(additional,"===========")
    categories=ProductCategory.objects.all()
    info_lists = [info.feature_description.split("\n") for info in additionalinfo]
    # print(additionalinfo)
    
    # context for showing stars on review and rating form
    star_range=range(1,6)
    context={
        'product':product,
        'productimages':product_images,
        'details':products,
        'inputs_list': products.description.split("\n"),
        'related':related_products,
        'descriptions':product_descriptions,
        'informations':additionalinfo,
        'info_lists':info_lists,
        'categories':categories,
        'additional':additional[0],
        'ratings':ratings,
        'form':form,
        'stars':star_range
    }
    return render(request,'main/product_detail.html',context)


def product(request,product_category):
    # print(product_category)
    items=Product.objects.filter(product_category__category_name=product_category)
    # print(items)
    categories=ProductCategory.objects.all()
    print(categories)
    context={
        'items':items,
        'categories':categories,
        'prod':product_category
    }
    return render(request,'main/product.html',context)


def search_results(request):
    return render(request,'main/search_results.html')


def signup(request):
    if request.method=='POST':
        fm=signupform(request.POST)
        if fm.is_valid():
            fm.save()
            fm=signupform()
            return HttpResponseRedirect('/login/')
    else:
        fm=signupform()
    return render(request,'main/signup.html',{'form':fm})


def user_login(request):
    # if not request.user.is_authenticated:
        if request.method=='POST':
            fm=AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    return redirect('/')
                else:
                    return redirect('login')
        else:
            fm=AuthenticationForm()
        return render(request,'main/login.html',{'form':fm})
    # else:
    #     return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return redirect('/')





















# views.py
# def plus_cart(request):
#     if request.method == 'GET':
#         prod_id = request.GET.get('prod_id')
#         if prod_id:
#             try:
#                 c = Cart.objects.get(product_id=prod_id, user=request.user)
#                 c.product_qty += 1
#                 c.save()
#                 data = {'quantity': c.product_qty}
#                 return JsonResponse(data)
#             except Cart.DoesNotExist:
#                 return JsonResponse({'error': 'Product not found in cart'}, status=404)
#         else:
#             return JsonResponse({'error': 'No product ID provided'}, status=400)
#     else:
#         return JsonResponse({'error': 'Invalid request method'}, status=405)
