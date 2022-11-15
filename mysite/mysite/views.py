from .models import Car
from rest_framework.response import Response
from .serializers import CarSerializer
from .serializers import Customer
from .serializers import Employee
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view
import random

@api_view(['GET'])
def get_cars(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def save_car(request):
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def update_car(request, id):
    try:
        theCar = Car.objects.get(pk=id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    
    serializer = CarSerializer(theCar, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_car(request, id):
    try:
        theCar = Car.objects.get(pk=id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    
    theCar.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def order_car(request, customerid, carid):
    try:
        the_car = Car.objects.get(pk=carid)
        the_customer = Customer.objects.get(pk=customerid)
        if the_car.status == 'Available' and the_customer.customer_status == None:
            the_car.status = 'Booked'
            the_customer.customer_status = the_car
            the_car.save()
            the_customer.save()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except the_car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def cancel_car_order(request, customerid, carid):
    try:
        the_car = Car.objects.get(pk=carid)
        the_customer = Customer.objects.get(pk=customerid)
        if the_car.status == 'Booked' and the_customer.customer_status == the_car:
            the_car.status = 'Available'
            the_customer.customer_status = None
            the_car.save()
            the_customer.save()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except the_car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def rent_car(request, customerid, carid):
    try:
        the_car = Car.objects.get(pk=carid)
        the_customer = Customer.objects.get(pk=customerid)
        if the_car.status == 'Booked' and the_customer.customer_status == the_car:
            the_car.status = 'Rented'
            the_car.save()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except the_car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def return_car(request, customerid, carid):
    car_status = ['Available', 'Damaged']
    try:
        the_car = Car.objects.get(pk=carid)
        the_customer = Customer.objects.get(pk=customerid)
        if the_car.status == 'Rented' and the_customer.customer_status == the_car:
            the_car.status = random.choice(car_status)
            the_customer.customer_status = None
            the_customer.save()
            the_car.save()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except the_car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_204_NO_CONTENT)

