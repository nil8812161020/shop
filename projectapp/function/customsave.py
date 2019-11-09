from django.http import HttpResponse
from django.contrib.auth import logout, authenticate, login
from projectapp.models import Users

#custom save data
def save_update(request,pk):
    message='fail'
    if pk:
        user = Users.objects.get(id=pk)
        user.first_lastname = request.POST['first_name']
        user.mobile = request.POST['mobile']
        user.email = request.POST['email']
        user.save()
    else:
        user = Users.objects.create_user(
            first_lastname=request.POST['first_name'],
            username=request.POST['username'],
            password=request.POST['password'],
            mobile=request.POST['mobile'],
            email=request.POST['email'],
        )
        login_user = authenticate(username=request.POST['username'], password=request.POST['password'])
        login(request, login_user)

    if user:
        message = 'successful'
    return HttpResponse(message)


