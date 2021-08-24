from django.shortcuts import render
from .models import Question, Login, Categories, Products
from django.http import HttpResponse


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
            return render(request, 'polls/product.html', context)    
        else:
            context['status'] = 0
    if context['status'] == 0:
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
    context = showAllProduct() 
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

def viewProductById(request, product_id):
    categories = Categories.objects.all()
    producr = Categories.objects.get(pk= product_id)
    pro = producr.products_set.all()
    cate_in = []
    for i in categories:
        cate_in.append(str(i.category_in).split(','))
        context = {'categoris': categories, 'cate_in': cate_in, "products": pro}
    return render(request, 'polls/product.html', context)

def product_detail(request, id_product):
    product = Products.objects.get(pk=id_product)
    
    content = {'product': product}
    return render(request, 'polls/product_detail.html',content)
    
def cart(request):
    return render(request, 'polls/cart.html')