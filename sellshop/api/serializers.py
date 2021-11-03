import random
from django.contrib.auth import get_user_model
from django.db.models import fields
from rest_framework import serializers
from product.models import Color, Product, ProductVersion, Category, Size
from user.models import User
from blog.models import Blog
from order.models import Cart, Cart_Item

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    blogs_comment = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ("id", "title", "description",
                  "creator", "like", "product")


class ProductSerializer(serializers.ModelSerializer):
    main_version = serializers.SerializerMethodField()
    total_quantity = serializers.SerializerMethodField()
    versions = serializers.SerializerMethodField()
    main_image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ("title", "subtitle", "ex_price", "price", "description",
                  "brand", "category", "total_quantity", "main_version", "versions", "main_image")

    def get_total_quantity(self, obj):
        return obj.total_quantity

    def get_main_version(self, obj):
        if obj.main_version:
            return ProductVersionSerializer(obj.main_version).data
        return None

    def get_versions(self, obj):
        if obj.main_version:
            qs = obj.versions.exclude(id=obj.main_version.id)
        else:
            qs = obj.versions.all()
        return ProductVersionSerializer(qs, many=True).data

    def get_main_image(self, obj):
        if obj.main_version.image.image:
            return obj.main_version.image.image.url
        else:
            return None


class ProductOverViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = "__all__"


class ProductVersionSerializer(serializers.ModelSerializer):
    product = ProductOverViewSerializer()
    color = ColorSerializer()
    size = SizeSerializer()

    class Meta:
        model = ProductVersion
        fields = "__all__"

    # # def get_main_image(self, obj):
    # #     if obj.main_version.image.image:
    # #         return obj.main_version.image.image.url
    # #     else:
    # #         return None


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


class CartSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    # images = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ("id", "user", "products")

    def get_products(self, obj):
        qs = obj.product.all()
        return ProductVersionSerializer(qs, many=True).data

    # def get_images(self, obj):
    #     qs = obj.product.first().version_images.all()
    #     return ProductVersionSerializer(qs, many=True).data


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductVersionSerializer( )
    class Meta:
        model = Cart_Item
        fields = ("product", "quantity")