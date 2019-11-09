from django.http import HttpResponse
from projectapp.models import Category

#custom save and update category
def save_update(request,pk):
    message='fail'
    if pk:
        category = Category.objects.get(id=pk)
        category.name = request.POST['category_name']
        category.slug = request.POST['category_slug']
        category.save()
    else:
        category = Category.objects.create(
            name=request.POST['category_name'],
            slug=request.POST['category_slug'],
        )
    if category:
        message = 'successful'
    return HttpResponse(message)


