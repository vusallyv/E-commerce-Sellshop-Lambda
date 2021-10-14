import random
from django import forms
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from product.models import Product
from user.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
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
