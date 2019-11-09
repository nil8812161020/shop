from django.urls import path
from projectapp.views import index,user_account,edit_account, create_account,change_password\
    ,login_view,logout_view,create_product,shop,create_category,edit_product,show_products,delete_product,show_category\
    ,delete_category,search,display_product



urlpatterns = [
    path('search/', search, name='search'),
    path('index/', index , name='index'),
    path('users/login_account/', create_account, name='create_user'),
    path('users/account/<str:id>', user_account, name='account'),
    path('users/update/<str:pk>', edit_account, name='update_user'),
    path('users/changepass/', change_password , name='change_pass'),
    path('accounts/login/', login_view,name='login_account'),
    path('accounts/logout/', logout_view,name='user_logout'),
    path('product/create/', create_product, name='create_product'),
    path('product/edit/<str:pk>', edit_product, name='edit_product'),
    path('product/delete/<str:pk>', delete_product, name='delete_product'),
    path('product/show/', show_products, name='products'),
    path('product/show/<str:pk>', display_product, name='display_product'),
    path('product/shop/', shop, name='shop'),
    path('product/category/create', create_category, name='create_category'),
    path('product/category/edit/<str:pk>', create_category, name='edit_category'),
    path('product/show/category', show_category, name='categories'),
    path('product/delete/category/<str:pk>', delete_category, name='delete_category'),
]


