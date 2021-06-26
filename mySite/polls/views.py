from django.shortcuts import render
from .models import Question, Login, Categories, Products
from django.http import HttpResponse


# Create your views here.

def index(request):
    myname = "Thắng"
    item = ["Điện thoại", "Xe máy"]
    context = {"name": myname, "item": item}
    return render(request, "polls/index.html", context)


def pages2(request):
    return render(request, 'polls/base.html')


def viewQuestion(request):
    listquestion = Question.objects.all()
    contect = {'listques': listquestion}
    return render(request, 'polls/fillData.html', contect)


def detailView(request, question_id):
    q = Question.objects.get(pk=question_id)
    context = {'qs': q}
    return render(request, 'polls/detailview.html', context)


def vote(request, question_id):
    q = Question.objects.get(pk=question_id)

    data = request.POST["choice"]
    c = q.choice_set.get(pk=data)

    c.vote = c.vote + 1
    c.save()
    return render(request, 'polls/result.html', {'q': q})


def login(request):
    return render(request, 'polls/login.html')


def eventLogin(request):
    logindata = Login.objects.all()
    username = request.POST['username']
    password = request.POST['pass']
    content = {'status': 0}
    for i in logindata:
        if username == i.username and password == i.password:
            content['status'] = 1
            return render(request, 'polls/index.html', content)
        else:
            content['status'] = 0
            return render(request, 'polls/login.html', content)


def shop(request):
    categories = Categories.objects.all()
    products = Products.objects.all()
    cate_in = []
    for i in categories:
        cate_in.append(str(i.category_in).split(','))
        context = {'categoris': categories, 'cate_in': cate_in}
    context['products'] = products
    return render(request, 'polls/product.html', context)

def viewProductById(request, product_id):
    categories = Categories.objects.all()
    producr = Categories.objects.get(pk= product_id)
    pro = producr.products_set.all()
    cate_in = []
    for i in categories:
        cate_in.append(str(i.category_in).split(','))
        context = {'categoris': categories, 'cate_in': cate_in, "products": pro}
    


    return render(request, 'polls/product.html', context)