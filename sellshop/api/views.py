# Create your views here.

from django.contrib.auth import get_user_model

from rest_framework import viewsets, permissions, status
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.serializers import CartSerializer, ProductSerializer, UserSerializer, ProductVersionSerializer, UserSerializer, CategorySerializer, BlogSerializer
from blog.models import Blog
from order.models import Cart
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
        product = Product.objects.filter(pk=product_id).first()
        if product:
            basket = Cart.objects.get_or_create(user=request.user)
            request.user.shoppingCardOfUser.product.add(product)
            message = {'success': True,
                       'message': 'Product added to your card.'}
            return Response(message, status=status.HTTP_201_CREATED)
        message = {'success': False, 'message': 'Product not found.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


# class TokenLoginView(TokenObtainPairView):

#     def post(self, request, *args, **kwargs):
#         print('------')
#         print(request.POST)
#         super().post(request, *args, **kwargs)