from django.shortcuts import render
from .models import Locations
from rest_framework import generics
from .serializers import LocationsSerializer
# from django.contrib.auth.decorators import login_required


# @login_required
class LocationCreate(generics.CreateAPIView):
	queryset = Locations.objects.all(),
	serializer_class = LocationsSerializer

# @login_required
class LocationList(generics.ListAPIView):
    queryset = Locations.objects.all()
    serializer_class = LocationsSerializer

# @login_required
class LocationDetail(generics.RetrieveAPIView):
    queryset = Locations.objects.all()
    serializer_class = LocationsSerializer

# @login_required
class LocationUpdate(generics.RetrieveUpdateAPIView):
    queryset = Locations.objects.all()
    serializer_class = LocationsSerializer

# @login_required
class LocationDelete(generics.RetrieveDestroyAPIView):
    queryset = Locations.objects.all()
    serializer_class = LocationsSerializer