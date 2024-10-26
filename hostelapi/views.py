from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework import parsers 
from rest_framework.filters import SearchFilter
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from .models import *
from .serializers import *


class StudentViewSet(ModelViewSet):
    queryset =  Student.objects.all()
    serializer_class =  StudentSerializer

class RoomViewSet(ModelViewSet):
    queryset =  Room.objects.all()
    serializer_class =  RoomSerializer

class BookingViewSet(ModelViewSet):
    queryset =  Booking.objects.all()
    serializer_class =  BookingSerializer

class PaymentViewSet(ModelViewSet):
    queryset =  Payment.objects.all()
    serializer_class =  PaymentSerializer
    


# # class TypeViewSet(ModelViewSet):
# #     queryset =  Type.objects.all()
# #     serializer_class =  TypeSerializer
# #     permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
