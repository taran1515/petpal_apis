from rest_framework import status,filters,generics
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from product.models import Product,Payment,Medicine,CancelOrder
from product.serializer import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


# @csrf_exempt
# @api_view(['GET', 'POST'])
# def product_list(request):
#     """
#     List  products, or create a new product.
#     """
#     if request.method == 'GET':
#         data = []
#         nextPage = 1
#         previousPage = 1
#         products = Product.objects.all()
#         page = request.GET.get('page', 1)
#         paginator = Paginator(products, 10)
#         try:
#             data = paginator.page(page)
#         except PageNotAnInteger:
#             data = paginator.page(1)
#         except EmptyPage:
#             data = paginator.page(paginator.num_pages)
#
#         serializer = ProductSerializer(data,context={'request': request} ,many=True)
#         if data.has_next():
#             nextPage = data.next_page_number()
#         if data.has_previous():
#             previousPage = data.previous_page_number()
#
#         return Response({'data': serializer.data})
#
#     elif request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_products(request):
    """
    List  products, or create a new product.
    """
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
def post_product(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

class ProductDetail(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Product.objects.filter(id=id)


@csrf_exempt
@api_view(['GET'])
def get_addresses(request):
    """
    List  products, or create a new product.
    """
    if request.method == 'GET':
        payment = Payment.objects.all()
        serializer = PaymentSerializer(payment,many=True)
        return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
def post_address(request):
    if request.method == 'POST':
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

class AddressDetail(generics.ListAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Payment.objects.filter(transaction_id=id)

@csrf_exempt
@api_view(['GET'])
def medicine_list(request):
    """
    List  products, or create a new product.
    """
    if request.method == 'GET':
        medicine = Medicine.objects.all()
        serializer = MedicineListSerializer(medicine,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MedicineListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

@csrf_exempt
@api_view(['POST'])
def medicine_search(request):


    if request.method=="POST":
        serializer = MedicineSearchSerializer(data=request.data)
        if serializer.is_valid():
            med =  (serializer.data['medicine_name'])
            x = Medicine.objects.filter(medicine_name=med)
            serializer2 = MedicineSearchSerializer(x,many=True)
            return Response(serializer2.data, status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(['GET'])
def get_cancel_orders(request):
    """
    List  products, or create a new product.
    """
    if request.method == 'GET':
        cancel_order= CancelOrder.objects.all()
        serializer = CancelOrderSerializer(cancel_order,many=True)
        return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
def post_cancel_order(request):

    if request.method == 'POST':
        serializer = CancelOrderDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

class CancelOrderDetail(generics.ListAPIView):
    serializer_class = CancelOrderDetailSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return CancelOrder.objects.filter(order_id=id)

@csrf_exempt
@api_view(['GET', 'POST'])
def order(request):
    """
    List  products, or create a new product.
    """
    if request.method == 'GET':
        order= Order.objects.all()
        serializer = OrderSerializer(order,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


class PostDetail(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Post.objects.filter(ID=id)

class PostDetailCreate(APIView):
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            print(PostSerializer.data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )



