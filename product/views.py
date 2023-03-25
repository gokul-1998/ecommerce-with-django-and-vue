from django.http    import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


# products[0:4] means that we are getting the first 4 products
# apiview is a class based view that allows us to create our own API endpoints 
class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            # we are using the category_slug to get the category and then we are using the product_slug to get the product
            # product.objects.filter(category__slug=category_slug) means that we are filtering the products by category
            # products.objct is used to get the product by slug 
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)