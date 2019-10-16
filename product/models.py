from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import (
   AbstractBaseUser, PermissionsMixin,
)
from django.db.models.signals import post_save

class Product(models.Model):

    # wp_wc_product_meta_lookup in actual database

    product_id = models.IntegerField()
    min_price = models.DecimalField(decimal_places=2,max_digits = 6,null=True)
    max_price = models.DecimalField(decimal_places=2,max_digits = 6,null=True)
    stock_status = models.TextField()
    total_sales = models.IntegerField()

def __str__(self):
    return self.product_id

class Payment(models.Model):
    product_id = models.IntegerField()
    transaction_id = models.IntegerField()
    prod_price = models.DecimalField(decimal_places=2,max_digits = 6)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.TextField()
    country = models.TextField()
    state = models.TextField()
    city = models.TextField()
    zip = models.IntegerField()

def __str__(self):
    return self.transaction_id

class Medicine(models.Model):
    medicine_name=models.TextField()
    synonms = models.TextField()

def __str__(self):
    return self.medicine_name

class CancelOrder(models.Model):

    order_id = models.IntegerField()
    user_id = models.IntegerField()
    is_approved = models.IntegerField(default=0)
    cancel_request_date = models.DateTimeField()
    cancel_date = models.DateTimeField()


class Post(models.Model):
    ID = models.AutoField(primary_key=True)
    post_date = models.DateTimeField(default="2019-08-31 18:23:22.000000")
    post_excerpt = models.TextField(default="Deliver as early as possible")
    post_type=models.CharField(max_length=20,default="shop_order",null=True)

class Order_item(models.Model):
    order_item_id_1 = models.ForeignKey(Post,on_delete = models.CASCADE,related_name='order_item_post_id')
    order_item_name = models.TextField()
    order_id = models.AutoField(primary_key=True)

class Order_item_meta(models.Model):
    meta_id = models.AutoField(primary_key=True)
    order_item_id_2= models.ForeignKey(Post,on_delete = models.CASCADE,related_name='order_item_meta_post_id')
    meta_key = models.CharField(max_length=100)
    meta_value = models.CharField(max_length=100)

class Petpal_User(models.Model):
    username = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=250,null=True)


# class UserProfile(models.Model):
#     user = models.OneToOneField(User,on_delete='cascade'),
#     user_id = models.AutoField(primary_key=True),
#     user_nicename = models.CharField(max_length=50,null=True)
#
#     def __str__(self):
#         return "%s's profile" % self.user
#
#
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         profile, created = UserProfile.objects.get_or_create(user=instance)
#
#
# post_save.connect(create_user_profile, sender=User)
#     # user_email = models.CharField(max_length=50)
#     user_registered = models.DateTimeField()
#     display_name = models.CharField(max_length=50)

#
# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_length=254, unique=True)
#     first_name = models.TextField(default='')
#     last_name = models.TextField(default='')
#     #any other fields you want
#     username = models.CharField(max_length=50)
#
#     USERNAME_FIELD = 'email'
# {
#    "order_item_id":"12",
#    "order_item_post_id":[
#       {
#          "order_item_id":"12",
#          "order_item_name":"hudbce"
#       }
#    ],
#    "order_item_meta_post_id":[
#       {
#          "order_item_id":"12",
#          "meta_key":"efef",
#          "meta_value":"2324"
#       }
#    ]
# }
# {
#    "order_item_post_id":[
#       {
#          "order_item_id_1":"1",
#          "order_iten_name":"abcdefghij"
#       }
#    ]
# }


