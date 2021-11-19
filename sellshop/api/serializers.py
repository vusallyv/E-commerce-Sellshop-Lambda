import random
from django.contrib.auth import get_user_model
from django.db.models import fields
from rest_framework import serializers
from product.models import Color, Image, Product, ProductVersion, Category, Review, Size
from user.models import Contact, User, Subscriber
from blog.models import Blog, Comment
from order.models import Cart, Cart_Item, City, Country, Coupon, Wishlist

User = get_user_model()


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    user = UserInfoSerializer()

    class Meta:
        model = Comment
        fields = ("id", "description", "user", "blog",
                  "is_main", "created_at", "replies")

    def get_replies(self, obj):
        return CommentSerializer(obj.replies.all(), many=True).data


class BlogSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ("id", "title", "description",
                  "creator", "product", "comments")

    def get_comments(self, obj):
        qs = obj.blogs_comment.filter(is_main=True)
        return CommentSerializer(qs, many=True).data


class ProductSerializer(serializers.ModelSerializer):
    main_version = serializers.SerializerMethodField()
    total_quantity = serializers.SerializerMethodField()
    versions = serializers.SerializerMethodField()
    # main_image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ("title", "subtitle", "ex_price", "price", "description",
                  "brand", "category", "total_quantity", "main_version", "versions")

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

    # def get_main_image(self, obj):
    #     if obj.main_version.image.image:
    #         return obj.main_version.image.image.url
    #     else:
    #         return None


class ProductOverViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = "__all__"


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = "__all__"


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer()

    class Meta:
        model = Review
        fields = "__all__"


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        exclude = ('country',)


class CountrySerializer(serializers.ModelSerializer):
    city = serializers.SerializerMethodField()

    class Meta:
        model = Country
        fields = ("country", "city")

    def get_city(self, obj):
        qs = obj.City_Country.all()
        return CitySerializer(qs, many=True).data


class ProductVersionSerializer(serializers.ModelSerializer):
    product = ProductOverViewSerializer()
    color = ColorSerializer()
    size = SizeSerializer()
    images = serializers.SerializerMethodField()
    review = serializers.SerializerMethodField()

    class Meta:
        model = ProductVersion
        fields = "__all__"

    def get_images(self, obj):
        qs = obj.version_images.get(is_main=True)
        return ImageSerializer(qs).data

    def get_review(self, obj):
        qs = obj.product_reviews.all()
        return ReviewSerializer(qs, many=True).data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email",
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
        # random_number = random.randint(0, 10000)
        # while User.objects.filter(username=f"Guest_{random_number}"):
        #     random_number = random.randint(0, 1000000)
        # validated_data['username'] = f"Guest_{random_number}"
        user = super().create(validated_data=validated_data)
        user.set_password(password)
        user.save()
        return user


class CartSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ("id", "user", "products")

    def get_products(self, obj):
        qs = obj.product.all()
        return ProductVersionSerializer(qs, many=True).data


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductVersionSerializer()
    is_ordered = serializers.SerializerMethodField()
    coupon_discount = serializers.SerializerMethodField()

    class Meta:
        model = Cart_Item
        fields = ("product", "quantity", "is_ordered", "coupon_discount")

    def get_is_ordered(self, obj):
        qs = obj.cart.is_ordered
        return qs
    
    def get_coupon_discount(self, obj):
        if obj.cart.coupon:
            qs = obj.cart.coupon.discount
            return qs
        return 0
            


class WishlistSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()

    class Meta:
        model = Wishlist
        fields = '__all__'

    def get_product(self, obj):
        qs = obj.product.all()
        return ProductVersionSerializer(qs, many=True).data
