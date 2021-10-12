from django.shortcuts import render

# Create your views here.

from rest_framework import permissions, serializers, status
from rest_framework.views import APIView
from api.serializers import ProductSerializer
from rest_framework.response import Response

from product.models import Product


class ProductAPIView(APIView):
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny)

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            obj = Product.objects.get(pk=kwargs.get("pk"))
            serializer = self.serializer_class(obj)
        else:
            qs = Product.objects.all()
            serializer = self.serializer_class(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        pass
