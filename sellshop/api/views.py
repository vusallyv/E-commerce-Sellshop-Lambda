from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView,DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response


from api.serializers import UserSerializer, UserOverviewSerializer, CategorySerializer, BlogSerializer
from product.models import Category
from blog.models import Blog

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
def CategoriesDetail(request,pk):
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
    serializer = CategorySerializer(instance=get_elemt ,data=request.data)
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
    
class ListBlogAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    

class DetailListBlogAPIView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class CreateBlogAPIView(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    

class UpdateBlogAPIView(UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
    
class DeleteBlogAPIView(DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    