import random
import re
from user.models import User
from product.models import Product, ProductVersion, Category
from rest_framework import serializers
from django.contrib.auth import get_user_model
from blog.models import Blog, Comment
from order.models import Cart


User = get_user_model()


class UserOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    blogs_comment = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ("id", "title", "description",
                  "creator", "like", "product", "blogs_comment")

    def get_blogs_comment(self, obj):
        return CommentSerializer(obj.blogs_comment, many=True).data


class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ("id", "user", "description",
                  "blog", "replies")

    def get_replies(self, obj):
        return CommentSerializer(obj.replies, many=True).data


class ProductSerializer(serializers.ModelSerializer):
    main_version = serializers.SerializerMethodField()
    total_quantity = serializers.SerializerMethodField()
    versions = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ("title", "subtitle", "ex_price", "price", "description",
                  "brand", "category", "total_quantity", "main_version", "versions")

    def get_total_quantity(self, obj):
        return obj.total_quantity

    def get_main_version(self, obj):
        return ProductVersionSerializer(obj.main_version).data

    def get_versions(self, obj):
        qs = obj.versions.exclude(id=obj.main_version.id)
        return ProductVersionSerializer(qs, many=True).data


class ProductVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVersion
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    productversion = serializers.SerializerMethodField()
    product = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ("id", "user", "productversion", "product")

    def get_productversion(self, obj):
        product_list = []
        for product in Cart.objects.all():
            product_list.append(product.product.values())
        return product_list

    def get_product(self, obj):
        return ProductVersion.objects.get(id=1).Product_Cart.values()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "email",
                  "phone_number", "password", 'password_confirmation')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    password_confirmation = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    def validate(self, attrs):
        password = attrs['password']
        password_confirmation = attrs.pop('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError(
                {'password': 'Password does not match.'})
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop('password')
        random_number = random.randint(0, 10000)
        while User.objects.filter(username=f"Guest_{random_number}"):
            random_number = random.randint(0, 1000000)
        validated_data['username'] = f"Guest_{random_number}"
        user = super().create(validated_data=validated_data)
        user.set_password(password)
        user.save()
        return user
