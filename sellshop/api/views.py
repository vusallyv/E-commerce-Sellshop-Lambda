# Create your views here.

from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import viewsets, permissions, serializers, status
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from blog.models import Blog, Comment
from order.models import Cart
from user.models import User
from product.models import Product, ProductVersion, Category
from api.serializers import CartSerializer, CommentSerializer, ProductSerializer, UserSerializer, ProductVersionSerializer, UserSerializer, UserOverviewSerializer, CategorySerializer, BlogSerializer


from rest_framework.decorators import api_view
User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    overview_serializer_class = UserOverviewSerializer

    def get_serializer_class(self):
        serializer = self.overview_serializer_class
        if self.request.method == 'GET':
            serializer = self.serializer_class
        return serializer


# decorators api method
@api_view(['GET'])
def CategoriesList(request):
    all_listt = Category.objects.all()
    serializer = CategorySerializer(all_listt, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def CategoriesDetail(request, pk):
    get_elemt = Category.objects.get(id=pk)
    serializer = CategorySerializer(get_elemt, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CategoriesCreate(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def CategoriesUpdate(request, pk):
    get_elemt = Category.objects.get(id=pk)
    serializer = CategorySerializer(instance=get_elemt, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def CategoriesDelete(request, pk):
    del_elemt = Category.objects.get(id=pk)
    del_elemt.delete()
    return Response('Successfully delete Category ID')

# class api method


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


class CommentAPIView(APIView):
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            obj = Comment.objects.get(pk=kwargs.get("pk"))
            serializer = self.serializer_class(obj)
        else:
            obj = Comment.objects.all()
            serializer = self.serializer_class(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CartAPIView(APIView):
    serializer_class = CartSerializer

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            obj = Cart.objects.get(pk=kwargs.get("pk"))
            serializer = self.serializer_class(obj)
        else:
            obj = Cart.objects.all()
            serializer = self.serializer_class(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


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
    permission_classes = (permissions.IsAdminUser,)
