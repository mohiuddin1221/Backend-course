from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import(
    Order
)
from .serializers import(
    OrderSerializer
)
# Create your views here.

class OrderView(APIView):
    def get(self, request):
        try:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders,many= True)
            return Response({
                'data' : serializer.data,
                'message' : "order data fetched successfully"
                
            }, status= status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                'data' : {},
                'message' : f"something went wrong : {str(e)}"
                
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    def post(self,request):
        try:
            data = request.data
            serializer = OrderSerializer(data=data)
            if not serializer.is_valid():
                return Response({
                    'data' : serializer.errors,
                    'message' : "something went wrong"
                }, status= status.HTTP_400_BAD_REQUEST)
            else:
                
                subject = 'New Order Placed'
                message = 'Dear customer' + " " + data['customer_name'] + 'Your order is placed'
                email = data['customer_email']
                recipient_list = [email] 
                send_mail(subject, message, EMAIL_HOST_USER, recipient_list)
                
                serializer.save()
                return Response({
                    'data': serializer.data,
                    'message': 'new order created'
                }, status= status.HTTP_201_CREATED)
                
                
        except:
            return Response({
                    'data' : {},
                    'message' : "something went wrong creation for order"
            },status=status.HTTP_400_BAD_REQUEST)
            
    def patch(self,request,pk):
        try:
            data = request.data
            orders = Order.objects.get(pk=pk)
            
            serializer = OrderSerializer(orders, data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'data' : serializer.data,
                    'message': 'order is update succesfully'
            }, status= status.HTTP_200_OK) 
            else:
                return Response({
                    'data': serializer.errors,
                    'message': 'Validation failed.'
                }, status=status.HTTP_400_BAD_REQUEST)        

        except Order.DoesNotExis:
            return Response({
                'data': {},
                'message' : 'something went wrong'
            })
        except Exception as e:
            return Response({
                'data': {},
                'message': f'Something went wrong: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    def delete(self,request,pk):
        try:
            data = request.data
            order = Order.objects.get(pk=pk)
            order.delete()
            return Response({
                'data': {},
                'message' : 'order is delete'
            }, status= status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response({
                'data' : {},
                'message' : 'order is not found'
            },status= status.HTTP_400_BAD_REQUEST)