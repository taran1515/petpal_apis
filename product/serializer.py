
from product.models import *
from rest_framework import serializers
from allauth.account.adapter import get_adapter
from allauth.utils import (email_address_exists,
                               get_username_max_length)
from allauth.account import app_settings as allauth_settings
from django.utils.translation import ugettext_lazy as _
from allauth.account.utils import setup_user_email
from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('product_id','total_sales','min_price','max_price','stock_status')

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ('address','country','state','city','zip')


class MedicineListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medicine
        fields = ('medicine_name','synonms')

class MedicineSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medicine
        fields = ('medicine_name',)

class RegisterSerializer(serializers.Serializer):

    username = serializers.CharField(
        max_length=get_username_max_length(),
        min_length=allauth_settings.USERNAME_MIN_LENGTH,
        required=allauth_settings.USERNAME_REQUIRED
    )
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)


    def validate_username(self, username):
        username = get_adapter().clean_username(username)
        return username

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address."))
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                _("The two password fields didn't match."))
        return data

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }



    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        username =  (self.cleaned_data['username'])
        first_name =  (self.cleaned_data['first_name'])
        last_name =  (self.cleaned_data['last_name'])
        email =  (self.cleaned_data['email'])
        password =  (self.cleaned_data['password1'])
        p=Petpal_User(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
        p.save()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.profile.save()
        return user

class CancelOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = CancelOrder
        fields = ('order_id','user_id')


class CancelOrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = CancelOrder
        fields = ('order_id','user_id','is_approved','cancel_request_date','cancel_date')

class OrderItemSerailizer(serializers.ModelSerializer):

    class Meta:
        model = Order_item
        fields = ('order_item_id_1','order_item_name')


class OrderItemMetaSerializer(serializers.ModelSerializer):

    class Meta:
        model= Order_item_meta
        fields = ('meta_key','meta_value')


class PostSerializer(serializers.ModelSerializer):

    order_item_post_id = OrderItemSerailizer( many=True)
    order_item_meta_post_id = OrderItemMetaSerializer( many=True)
    class Meta:
        model = Post
        fields = ('ID','order_item_post_id','order_item_meta_post_id')

    def create(self, validated_data):
        a = validated_data.pop('order_item_post_id')
        b = validated_data.pop('order_item_meta_post_id')

        post = Post.objects.create(**validated_data)
        print (a[0]['order_item_name'])
        print(b[0])

        Order_item.objects.create(order_item_id_1 = post,order_item_name=a[0]['order_item_name'])
        # Order_item_meta.objects.create(order_item_id_2=post,meta_key=b[0]['meta_key'],meta_value=b[0]['meta_value'])
        # Order_item.objects.create(order_item_name = post)
        for order_item_meta_post_ids in b:
            Order_item_meta.objects.create(order_item_id_2 = post,**order_item_meta_post_ids)
        return post

#
# {
