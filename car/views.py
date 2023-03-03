from django.shortcuts import render
from django.db.models import Q

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Car, Reservation
from .serializers import CarSerializer, ReservationSerializer
from .permissions import IsStaffOrReadOnly

# Create your views here.

class CarView(ModelViewSet):

    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsStaffOrReadOnly]

    def get_queryset(self):
        
        #! Users who are admin will be able to view all Car 
        if self.request.user.is_staff:
            queryset = super().get_queryset()
        
        #! Non-admin users will only be able to view cars with availability = True
        else:
            queryset = super().get_queryset().filter(availability = True)
        
        
        #! We do a detailed filtering with query_params:
        start = self.request.query_params.get('start')
        print(start)
        end = self.request.query_params.get('end')
        print(end)


        #! Method to list cars that have no reservations between the dates entered by the user
        con1 = Q(start_date__lt = end)
        con2 = Q(end_date__gt = start)
        not_avilable = Reservation.objects.filter(con1 & con2).values_list('car_id', flat = True)

        queryset = queryset.exclude(id__in = not_avilable)
        return queryset


class ReservationView(ListCreateAPIView):

    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]  # If the user is registered, they can only make reservations.

    #! If the user is an admin, let him view every reservation, if the user is a customer, let him see only his own reservations

    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
        return super().get_queryset().filter(customer = self.request.user)


class ReservationDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    
    #! The user may want to extend the reservation date, but if there is another reservation for the same vehicle on the desired dates, she should receive a warning:

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()  # Gets which object it is from here
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)  # raise_exception = True if serializer passes validation false if false

        end = serializer.validated_data.get('end_date')  # With Valided_data, we reach the data that has passed the validation. Since we wanted to extend the end date after we reached the field we will use, we took the end_date from there.
        car = serializer.validated_data.get('car')
        start = instance.start_date  # I was able to access the start_date field like end and car fields, but since they can use both put and patch on the front end, we accessed the object from the variable I assigned above. In Put operation we have to resend all the data, in Patch we can only send the data we want to change.
        if Reservation.objects.filter(car = car).exists():  # I check the reservation table for any information about the vehicle I want to extend the expiry date. Returns True if present, False otherwise.
            for res in Reservation.objects.filter(car = car):
                if start < res.start_date < end:
                    return Response({'message':'Car is not available'})
        return super().update(request, *args, **kwargs)        
        


