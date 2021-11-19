# Create your views here.

import re
from django.contrib.auth import get_user_model

from rest_framework import viewsets, permissions, status
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.serializers import CartItemSerializer, CartSerializer, ContactSerializer, CountrySerializer, CouponSerializer, ProductSerializer, SubscriberSerializer, UserSerializer, ProductVersionSerializer, UserSerializer, CategorySerializer, BlogSerializer, WishlistSerializer
from blog.models import Blog, Comment
from order.models import Cart, Cart_Item, City, Country, Coupon, ShippingAddress, Wishlist
from user.models import Contact, Subscriber, User
from product.models import Product, ProductVersion, Category, Review

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    queryset = get_user_model().objects.all()


class ListCategoryAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DetailCategoryAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CreateCategoryAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UpdateCategoryAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DeleteCategoryAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CreateBlogAPIView(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class UpdateBlogAPIView(UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class DeleteBlogAPIView(DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class ProductAPIView(APIView):
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            obj = Product.objects.get(pk=kwargs.get("pk"))
            serializer = self.serializer_class(obj)
        else:
            obj = Product.objects.all()
            serializer = self.serializer_class(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BlogAPIView(APIView):
    serializer_class = BlogSerializer

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            obj = Blog.objects.get(pk=kwargs.get("pk"))
            serializer = self.serializer_class(obj)
        else:
            obj = Blog.objects.all()
            serializer = self.serializer_class(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        blog_id = request.data.get('blogId')
        is_main = request.data.get('isMain')
        description = request.data.get('description')
        replyId = request.data.get('replyId')
        if blog_id:
            if replyId:
                Comment.objects.create(blog=Blog.objects.get(pk=kwargs.get(
                    "pk")), is_main=is_main, user=request.user, description=description, reply=Comment.objects.get(pk=replyId))
            else:
                Comment.objects.create(blog=Blog.objects.get(pk=kwargs.get(
                    "pk")), is_main=is_main, user=request.user, description=description)
            message = {'success': True,
                       'message': 'Comment added.'}
            return Response(message, status=status.HTTP_201_CREATED)
        message = {'success': False, 'message': 'Blog not found.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


class ProductVersionAPIVIew(APIView):
    serializer_class = ProductVersionSerializer

    def get(self, request, *args, **kwargs):
        if kwargs.get("product"):
            obj = ProductVersion.objects.filter(product=kwargs.get("product"))
            serializer = self.serializer_class(obj, many=True)
            stat = status.HTTP_200_OK
            if kwargs.get("pk"):
                obj = ProductVersion.objects.get(pk=kwargs.get("pk"))
                serializer = self.serializer_class(obj)
        else:
            serializer = {"detail": "Product not found"}
            stat = status.HTTP_404_NOT_FOUND
        return Response(serializer.data, status=stat)


class ProductVersionReviewAPIVIew(APIView):
    serializer_class = ProductVersionSerializer

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            obj = ProductVersion.objects.get(pk=kwargs.get("pk"))
            serializer = self.serializer_class(obj)
            stat = status.HTTP_200_OK
        else:
            serializer = {"detail": "ProductVersion not found"}
            stat = status.HTTP_404_NOT_FOUND
        return Response(serializer.data, status=stat)

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('productId')
        rating = request.data.get('rating')
        review = request.data.get('review')
        if product_id:
            Review.objects.create(product=ProductVersion.objects.get(pk=product_id),
                                  user=request.user, rating=rating, review=review)
            message = {'success': True,
                       'message': 'Comment added.'}
            return Response(message, status=status.HTTP_201_CREATED)
        message = {'success': False, 'message': 'Blog not found.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAdminUser,)


class ProductVersionCreateAPIView(CreateAPIView):
    queryset = ProductVersion.objects.all()
    serializer_class = ProductVersionSerializer
    permission_classes = (permissions.IsAdminUser,)


class ProductDestroyAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAdminUser,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductVersionDestroyAPIView(DestroyAPIView):
    queryset = ProductVersion.objects.all()
    serializer_class = ProductVersionSerializer
    permission_classes = (permissions.IsAdminUser,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAdminUser,)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class ProductVersionUpdateAPIView(UpdateAPIView):
    queryset = ProductVersion.objects.all()
    serializer_class = ProductVersionSerializer
    permission_classes = (permissions.IsAdminUser,)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CartView(APIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        obj = Cart.objects.get(user=request.user)
        serializer = self.serializer_class(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product')
        quantity = request.data.get('quantity')
        template = request.data.get('template')
        product = ProductVersion.objects.get(pk=product_id)
        Cart.objects.get_or_create(user=request.user, is_ordered=False)
        cart = Cart.objects.get(user=request.user, is_ordered=False)
        if product:
            if template == "cart.html":
                Cart_Item.objects.get_or_create(cart=cart, product=product)
                cart_item = Cart_Item.objects.get(cart=cart, product=product)
                cart_item.quantity = int(quantity)
                Cart_Item.objects.filter(cart=cart, product=product).update(
                    quantity=cart_item.quantity)
                Cart.objects.get(user=request.user,
                                 is_ordered=False).product.add(product)
            elif template == "product_list.html":
                Cart_Item.objects.get_or_create(cart=cart, product=product)
                cart_item = Cart_Item.objects.get(cart=cart, product=product)
                cart_item.quantity += int(quantity)
                Cart_Item.objects.filter(cart=cart, product=product).update(
                    quantity=cart_item.quantity)
                Cart.objects.get(user=request.user,
                                 is_ordered=False).product.add(product)
            elif template == "remove_from_cart":
                Cart_Item.objects.get_or_create(cart=cart, product=product)
                cart_item = Cart_Item.objects.get(cart=cart, product=product)
                Cart_Item.objects.filter(cart=cart, product=product).delete()
                Cart.objects.get(user=request.user,
                                 is_ordered=False).product.remove(product)
            message = {'success': True,
                       'message': 'Product added to your card.'}
            return Response(message, status=status.HTTP_201_CREATED)
        message = {'success': False, 'message': 'Product not found.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


class CartItemView(APIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        Cart.objects.get_or_create(user=request.user, is_ordered=False)
        obj = Cart_Item.objects.filter(
            cart=Cart.objects.get(user=request.user, is_ordered=False)).order_by('created_at')
        serializer = self.serializer_class(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CountryView(APIView):
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        country = request.data.get("country")
        obj = Country.objects.filter(country=country)
        serializer = self.serializer_class(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        country = request.data.get("country")
        obj = Country.objects.filter(country=country)
        serializer = self.serializer_class(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class WishlistAPIView(APIView):
    serializer_class = WishlistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        obj, created = Wishlist.objects.get_or_create(user=request.user)
        serializer = self.serializer_class(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product')
        product = ProductVersion.objects.get(pk=product_id)
        Wishlist.objects.get_or_create(user=request.user)
        wishlist = Wishlist.objects.get(user=request.user)
        if product and product not in wishlist.product.all():
            wishlist.product.add(product)
        else:
            wishlist.product.remove(product)
        message = {'success': True,
                   'message': 'Product added to your wishlist.'}
        return Response(message, status=status.HTTP_201_CREATED)


class CheckoutAPIView(APIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        company_name = request.data.get('company_name')
        address = request.data.get('address')
        country = request.data.get('country')
        city = request.data.get('city')
        shipping = ShippingAddress(
            user=request.user,
            company_name=company_name,
            country=Country.objects.get(country=country),
            city=City.objects.get(city=city),
            address=address,
        )
        shipping.save()
        message = {'success': True,
                   'message': 'Your order has been placed.'}
        return Response(message, status=status.HTTP_201_CREATED)


class SubscriberAPIVIew(APIView):
    serializer_class = SubscriberSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        if email and Subscriber.objects.filter(email=email).exists() == False:
            Subscriber.objects.create(email=email)
            message = {'success': True,
                       'message': 'Subscriber added.'}
            return Response(message, status=status.HTTP_201_CREATED)
        message = {'success': False, 'message': 'Subscriber already exists.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


class ContactAPIVIew(APIView):
    serializer_class = ContactSerializer

    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        email = request.data.get('email')
        message = request.data.get('message')
        if email and name and message:
            Contact.objects.create(name=name, email=email, message=message)
            message = {'success': True,
                       'message': 'Your message sent.'}
            return Response(message, status=status.HTTP_201_CREATED)
        message = {'success': False, 'message': 'Invalid message.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


class CouponAPIVIew(APIView):
    serializer_class = CouponSerializer

    def post(self, request, *args, **kwargs):
        code = request.data.get('code')
        if code:
            if Cart.objects.filter(user=request.user, is_ordered=False, coupon=None).exists():
                obj, created = Cart.objects.get_or_create(
                    user=request.user, is_ordered=False)
                obj.coupon = Coupon.objects.get(code=code)
                obj.save()
                message = {'success': True,
                           'message': 'Coupon applied.'}
                return Response(message, status=status.HTTP_201_CREATED)
            message = {'success': False, 'message': 'Coupon already applied to this cart.'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        message = {'success': False, 'message': 'Coupon not found.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
