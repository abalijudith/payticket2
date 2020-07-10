from rest_framework import serializers
from .models import Agence,Station,Trip

class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model=Agence
        fields='__all__'


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Station
        fields='__all__'



class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trip
        fields="__all__"