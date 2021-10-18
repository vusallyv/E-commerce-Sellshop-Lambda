import random
from user.models import User
from product.models import Product, ProductVersion, Category
from rest_framework import serializers
from django.contrib.auth import get_user_model
from blog.models import Blog


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
    class Meta:
        model = Blog
        fields = '__all__'


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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "email",
                  "phone_number", "password")

    def create(self, validated_data):
        random_number = random.randint(0, 10000)
        while User.objects.filter(username=f"Guest_{random_number}"):
            random_number = random.randint(0, 1000000)
        user = User.objects.create(
            username=f"Guest_{random_number}",
            email=validated_data.get("email"),
            first_name=validated_data.get("first_name"),
            phone_number=validated_data.get("phone_number"),
        )
        user.set_password(validated_data.get("password"))
        user.save()

        return user
