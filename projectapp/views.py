from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from projectapp.models import Users,Product,Category,Cart,Profile,Order
from projectapp.function import customsave,customproduct,customcategory
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
import json

#search product
def search(request):
    search = request.GET.get('input')
    queryset = Product.objects.filter(name__startswith=search).values('id','name')
    data = json.dumps(list(queryset))
    print(data)
    return HttpResponse(data,content_type='application/json')


# Create your views here.

def index(request):

    message="welcome"
    obj=Product.objects.all()
    return render(request,'index.html',{'message':message,'obj':obj})

#shopping
def shop(request):

    obj=Product.objects.all()
    return render(request,'shopping.html',{'obj':obj})


#create users
def create_account(request,pk=None):
   try:
        message = ''
        if request.method == 'GET':
            return render(request, 'user_pure_html.html')
        elif request.method == 'POST':
            if Users.objects.filter(username=request.POST['username']).exists():
                message='بری از قبل ثبت شدهنام کار'
            else:
                message = customsave.save_update(request,pk)
        obj_user = Users.objects.latest('id')
        return redirect(reverse('account' , kwargs={'id':obj_user.id} ))
   except Exception as e:
      return render(request, 'error.html',{'message':e})

#user account
def user_account(request,id):
    obj=Users.objects.get(id=int(id))
    return render(request,'user_account.html',{'object':obj})

#edit user account
def edit_account(request, pk):
    try:
        obj_user = Users.objects.get(id=pk)
        if request.method == 'GET':
            return render(request, 'users_edit.html', {'object': obj_user})
        elif request.method == 'POST':
            customsave.save_update(request, pk)
            obj_user = Users.objects.latest('id')
            return redirect(reverse('account', kwargs={'id': obj_user.id}))
    except Exception as e:
            return render(request,'error.html',{'message':e})

#change password users
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            message = 'رمز عبور با موفقیت تغییر یافت'
            return redirect(reverse('account', kwargs={'id': user.id}))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    args = {'form': form}
    return render(request, 'change_password.html', args)

#login account
def login_view(request):
    message = ''
    if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          user = auth.authenticate(username=username, password=password)
          if user is not None:
              if user.is_active:
                  auth.login(request,user)
                  # Redirect to index page.
                  return redirect(reverse('account', kwargs={'id': user.id}))
              else:
                  # Return a 'disabled account' error message
                  return HttpResponse("اکانت شما غیر فعال شده است.")
          else:
              # Return an 'invalid login' error message.
              message = "نام کاربری  " "" + username +"" " و رمز عبور " + password + " معتبر نمی باشند "
              return render(request,'user_pure_html.html',{'message':message})
    else:
        # the login is a  GET request, so just show the user the login form.
       return render(request,'user_pure_html.html')

#log out
@login_required
def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return redirect(reverse('index'))

#add product
def create_product(request,pk=None):
    message=''
    category = Category.objects.all()
    if request.method == 'GET':
        return render(request,'product_form.html',{'category':category})
    elif request.method=='POST':
        if Product.objects.filter(name=request.POST['product_name']).exists():
            message='محصولی با این نام قبلا ثبت شده است'
        else:
            customproduct.save_update(request, pk)
            message='محصول با موفقیت ثبت شد'
    return render(request,'product_form.html',{'message':message})
#edit product
def edit_product(request, pk):
    try:
        obj_product = Product.objects.get(id=pk)
        category = Category.objects.all()
        if request.method == 'GET':
            return render(request, 'product_edit.html', {'object': obj_product,'category':category})
        elif request.method == 'POST':
            customproduct.save_update(request, pk)
            product_obj = Product.objects.all()
            return render(request,'products.html',{'products':product_obj})
    except Exception as e:
            return render(request,'error.html',{'message':e})

#delete product
def delete_product(request,pk):
    try:
        obj_product = Product.objects.filter(id=pk)
        obj_product.delete()
        messages.info(request,'محصول با موفقیت حذف شد!!')
        return redirect('products')
    except Exception as e:
        return render(request, 'error.html', {'message': e} )

#display product page
def display_product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request,'display-product.html',{'product':product})

#product list
def show_products(request):
    product_obj = Product.objects.all()
    return render(request,'products.html',{'products':product_obj})

#add and update category
def create_category(request,pk=None):
    if pk:
        try:
            obj_category = Category.objects.get(id=pk)
            if request.method == 'GET':
                return render(request, 'category_edit.html', {'object': obj_category})
            elif request.method == 'POST':
                if Category.objects.filter(name=request.POST['category_name']).exists():
                    message = 'سته بندی با این نام از قبل ایجاد شده است.'
                else:
                    customcategory.save_update(request, pk)
                    message = 'ویرایش با موفقیت انجام شد'
                obj_category = Category.objects.all()
                return render(request, 'categories.html', {'category': obj_category})
        except Exception as e:
            return render(request, 'error.html', {'message': e})
    else:
        message = ''
        if request.method == 'GET':
            return render(request, 'category.html')
        elif request.method == 'POST':
            if Category.objects.filter(name=request.POST['category_name']).exists():
                message = 'سته بندی با این نام از قبل ایجاد شده است.'
            else:
                customcategory.save_update(request, pk)
                message = "دسته بندی با موفقیت ایجاد شد"
            return render(request, 'category.html', {'message': message})

#category list
def show_category(request):
    category_obj = Category.objects.all()
    return render(request,'categories.html',{'category':category_obj})

#delete product
def delete_category(request,pk):
    try:
        obj_category = Category.objects.filter(id=pk)
        obj_category.delete()
        messages.info(request,'حصول با موفقیت حذف شد!!')
        return redirect('categories')
    except Exception as e:
        return render(request, 'error.html', {'message': e} )

#shopping cart
def add_cart(request,pk=None):
    product = Product.objects.get(id=pk)
    Order.objects.create(product=product,is_ordered=True)
    items=Order.objects.filter(product=product)
    for item in items:
        Cart.objects.create(order=item)
    return render(request,'cart.html',{'product':product})
