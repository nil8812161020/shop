from django.http import HttpResponse
from projectapp.models import Product


#custom save data
def save_update(request,pk):
    message='fail'
    if pk:
        product = Product.objects.get(id=pk)
        product.name = request.POST['product_name']
        product.price = request.POST['product_price']
        product.description = request.POST['product_description']
        product.discount = request.POST['product_discount']
        product.price_discount = request.POST['price_discount']
        product.category_id = request.POST.get('id')
        if request.FILES.get('product_image'):
           product.image = request.FILES.get('product_image')
        else:
           product.image = product.image
        product.save()
    else:
        product = Product.objects.create(
            name = request.POST['product_name'],
            price = request.POST['product_price'],
            description = request.POST['product_description'],
            discount = request.POST['product_discount'],
            price_discount = request.POST['price_discount'],
            category_id = request.POST.get('id'),
            image = request.FILES['product_image'],

        )
    if product:
        message = 'successful'
    return HttpResponse(message)


