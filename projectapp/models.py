from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.

#users models
class Users(AbstractUser):
    first_lastname = models.CharField(max_length=60)
    mobile         = models.CharField(max_length=11)


#class Product(models.Model):
#    product_name     = models.CharField(max_length=300,unique=True)
#    product_price    = models.FloatField(max_length=10)
#    product_color    = models.CharField(max_length=20)
#    product_discount = models.CharField(max_length=4)
#    price_discount   = models.FloatField(max_length=20)
#    product_image    = models.FileField(upload_to = 'media/', blank=True)

#    def __str__(self):
#        return self.product_name + ": " + str(self.product_image)


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.CharField(max_length=4,default=0)
    price_discount = models.CharField(max_length=20,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.FileField(upload_to = 'media', blank=True,null=True)

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

#profile
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    product = models.ManyToManyField(Product,blank=True)


#order
class Order(models.Model):
   product    = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
   is_ordered = models.BooleanField(default=False)
   date_added = models.DateTimeField(auto_now=True)
   date_ordered = models.DateTimeField(null=True)

   def __str__(self):
       return self.product.name

#shoping cart
class Cart(models.Model):
    order = models.ManyToManyField(Order)
    owner = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
    is_ordered = models.DateTimeField(default=False)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.order.all()


