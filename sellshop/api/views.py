# Create your views here.

from django.contrib.auth import get_user_model

from rest_framework import viewsets, permissions, status
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.serializers import CartItemSerializer, CartSerializer, ProductSerializer, UserSerializer, ProductVersionSerializer, UserSerializer, CategorySerializer, BlogSerializer
from blog.models import Blog
from order.models import Cart, Cart_Item
from user.models import User
from product.models import Product, ProductVersion, Category

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

# Blog api


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
        product = ProductVersion.objects.get(pk=product_id)
        Cart.objects.get_or_create(user=request.user)
        cart = Cart.objects.get(user=request.user)
        if product:
            print(quantity)
            product.quantity -= int(quantity)
            product.save()
            Cart_Item.objects.get_or_create(cart=cart, product=product)
            cart_item = Cart_Item.objects.get(cart=cart, product=product)
            cart_item.quantity += int(quantity)
            Cart_Item.objects.filter(cart=cart, product=product).update(quantity=cart_item.quantity)
            Cart.objects.get(user=request.user).product.add(product)
            message = {'success': True,
                       'message': 'Product added to your card.'}
            return Response(message, status=status.HTTP_201_CREATED)
        # elif product and product in Cart.objects.get(user=request.user).product.all():
        #     product.quantity += 1
        #     product.save()
        #     Cart_Item.objects.get_or_create(cart=cart, product=product)
        #     cart_item = Cart_Item.objects.get(cart=cart, product=product)
        #     cart_item.quantity += 1
        #     Cart_Item.objects.filter(cart=cart, product=product).update(quantity=cart_item.quantity)
        #     Cart.objects.get(user=request.user).product.remove(product)
        #     message = {'success': True,
        #                'message': 'Product removed from your card.'}
        #     return Response(message, status=status.HTTP_201_CREATED)
        message = {'success': False, 'message': 'Product not found.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


class CartItemView(APIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        obj = Cart_Item.objects.filter(cart=Cart.objects.get(user=request.user))
        serializer = self.serializer_class(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)