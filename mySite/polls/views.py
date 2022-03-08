from django.shortcuts import render
from .models import Login, Categories, Products, Cart
from django.http import HttpResponse, response
import json


# Create your views here.

def login(request):
    return render(request, 'polls/login.html')

def eventLogin(request):
    logindata = Login.objects.all()
    username = request.POST['username']
    password = request.POST['password']
    
    #context = {'status': 0, 'username': ''}
    context = showAllProduct()
    for i in logindata: 
        if username == i.username and password == i.password:
            context['status'] = 1
            context['username'] = i.username
            response = render(request, 'polls/product.html', context)
            response.set_cookie('username', str(context['username']))  
            return response
        else:

            context['status'] = 0

    if context['status'] == 0:
        try:
            username  = request.COOKIES['username']
        except:
            username = ''
        context['product'] = showAllProduct() 
        context['username'] = username
        return render(request, 'polls/login.html', context)
        
    else:
        return render(request, 'polls/product.html', context)

def sign_up(request):
    username = request.POST['username']
    password = request.POST['password']
    pass_again = request.POST['password_again']

    content = showAllProduct()
    try:
        if password == pass_again:
            insert = Login.objects.create(username = username, password = password)
            content['status1'] = 1
            content['username'] = username
            return render(request, 'polls/product.html', content)
    except:
        content['status1'] = 0
        return render(request, 'polls/login.html', content)




def shop(request):
    cate_in = []
    categories = Categories.objects.all()
    
    context = {}
    for i in categories:
        cate_in.append(str(i.category_in).split(','))
        context = {'categoris': categories, 'cate_in': cate_in}
    try:
        username  = request.COOKIES['username']
    except:
        username = ''
    context['product'] = showAllProduct() 
    context['username'] = username
    return render(request, 'polls/product.html', context)

def showAllProduct():
    categories = Categories.objects.all()
    products = Products.objects.all()
    cate_in = []
    context ={} 
    for i in categories:
        cate_in.append(str(i.category_in).split(','))
        context = {'categoris': categories, 'cate_in': cate_in}
    context['products'] = products
    return context

def product_detail(request, id_product):
    product = Products.objects.get(pk=id_product)
     
    content = {'product': product}
    return render(request, 'polls/product_detail.html',content)
    
def cart(request):
    try:
        username  = request.COOKIES['username']
    except:
        username = ''
    context = {'username': username}
    return render(request, 'polls/cart.html', context)

def setcookie(request):  
    response = HttpResponse("Cookie Set")  
    response.set_cookie('java-tutorial', 'javatpoint.com')  
    return response  

def getcookie(request):  
    tutorial  = request.COOKIES['username']  
    return HttpResponse("java tutorials @: "+  tutorial)

def loginv4(request):  

    return render(request, 'polls/loginv4.html')

# API

def getAllProduct(request):
    products = Products.objects.all()
    product_item = []
    for i in products:
        product_item.append({"id": i.id, "product_name": i.product_name, "price": i.price, "discription": i.discription, "url_images": i.url_images, "title": i.title, "status": i.status})
    
    response_data = {'products': product_item}
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def getProductById(request, product_id):
    producr = Categories.objects.get(pk= product_id)
    pro = producr.products_set.all()
    product_item = []
    for i in pro:
        product_item.append({"id": i.id, "product_name": i.product_name, "price": i.price, "discription": i.discription, "url_images": i.url_images, "title": i.title, "status": i.status})
    response_data = { "products": product_item}
    return HttpResponse(json.dumps(response_data), content_type="application/json") 

def getCartItem(request):
    username  = request.COOKIES['username'] 
    cart = Cart.objects.filter(username_id = username)
    cart_item = []
    for i in cart:
        cart_item.append({"user": i.username_id,"id": i.id, "product_name": i.product.product_name, "price": i.product.price, "discription": i.product.discription, "url_images": i.product.url_images, "title": i.product.title, "status": i.product.status, "quantity": i.quantity})
    response_data = { "cart": cart_item}
    return HttpResponse(json.dumps(response_data), content_type="application/json") 

def delete_item(request, id):
    try:
        Cart.objects.get(id=id).delete()
    except Exception as e:
        return HttpResponse(json.dumps({"status": "Error"}), content_type="application/json")

    return HttpResponse(json.dumps({"status": "Success"}), content_type="application/json")

def add_to_cart(request, id):
    try:
        add_new = Cart.objects.create(username_id = request.COOKIES['username'], product_id = id, quantity = 1)
    except Exception as e:
        return HttpResponse(json.dumps({"status": "Error"}), content_type="application/json")
    return HttpResponse(json.dumps({"status": "Success"}), content_type="application/json")

def plus_quantity(request):
    try:
        cart = Cart.objects.get(id = request.POST['id'])
        cart.quantity = cart.quantity + 1
        cart.save()
    except Exception as e:
        return HttpResponse(json.dumps({"status": "Error"}), content_type="application/json")
    return HttpResponse(json.dumps({"status": "Success"}), content_type="application/json")