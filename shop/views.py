from django.shortcuts import render,get_object_or_404,redirect, HttpResponseRedirect
from django.http import HttpResponse
import json
from shop.PayTm import Checksum
from django.db.models import Q
from shop.models import Product,Contact,Order,OrderUpdate
from django.core.paginator import Paginator,InvalidPage,EmptyPage
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import Group,User

from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate, logout

# Create your views here.
from django.http import HttpResponse
MERCHANT_KEY = 'HCPfTQa0QkJsx#AU'

def index(request):
    products = Product.objects.all()

    # PAGINATOR----------------------------------------------
    paginator = Paginator(products, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
    # ---------------------------------------------------------------
    return render(request, 'shop/index.html',{'products':products})

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    thank = False
    if request.method=="POST":
        name=request.POST.get('name','')
        email = request.POST.get('email', '')
        query = request.POST.get('query', '')
        phone = request.POST.get('phone', '')
        contact=Contact(name=name,email=email,query=query,phone=phone)
        contact.save()
        thank = True
    return render(request, 'shop/contact.html',{'thank':thank})

def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates,order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')

def search(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=Product.objects.all().filter(Q(product_name__contains=query)|Q(category__contains=query))
    return render(request,'shop/search.html',{'products':products,'query':query})


def productView(request, myid):
    #fetch the product by id
    product=Product.objects.filter(id=myid)
    print(Product)
    return render(request, 'shop/productView.html', {'product':product[0]})

def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        amount = request.POST.get('amount', '')
        name = request.POST.get('name', '')
        instructions=request.POST.get('instructions', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Order(items_json=items_json,amount=amount ,name=name, instructions=instructions,email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        #return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})
        # Request paytm to transfer the amount to your account after payment by user
        param_dict = {

            'MID': 'eSudyN23298197861191',
            'ORDER_ID': str(order.order_id),
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/shop/handlerequest/',

        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'shop/paytm.html', {'param_dict': param_dict})
    return render(request, 'shop/checkout.html')

def Blog(request):
    return render(request, 'shop/blog.html')

@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'shop/paymentstatus.html', {'response': response_dict})




def signupView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return redirect('shop:ShopHome')
            else:
                return redirect('signup')
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            customer_group = Group.objects.get(name='Customer')
            customer_group.user_set.add(signup_user)  # this is how to add a user to a group

    else:
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form': form})



def signinView(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('shop:ShopHome')
            else:
                return redirect('signup')
    else:
        form=AuthenticationForm()
    return render(request, 'accounts/signin.html', {'form':form})





def signoutView(request):
    logout(request)
    return redirect('shop:signin')


