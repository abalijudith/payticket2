from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from .serializers import AgencySerializer,TripSerializer,StationSerializer
from .models import Agence,Trip,Station


class AgencyList(viewsets.ModelViewSet):
    serializer_class = AgencySerializer
    queryset = Agence.objects.all()

class TripList(viewsets.ModelViewSet):
    serializer_class = TripSerializer
    queryset = Trip.objects.all()


class StationList(viewsets.ModelViewSet):
    serializer_class = StationSerializer
    queryset = Station.objects.all()