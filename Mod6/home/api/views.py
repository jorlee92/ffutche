from rest_framework import generics
from home.models import User, School, Scholarship
from home.api.serializers import *

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class SchoolListView(generics.ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class SchoolDetailView(generics.RetrieveAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class ScholarshipListView(generics.ListAPIView):
    queryset = Scholarship.objects.all()
    serializer_class = SchoolSerializer

class ScholarshipDetailView(generics.RetrieveAPIView):
    queryset = Scholarship.objects.all()
    serializer_class = SchoolSerializer

class TuitionFeesListView(generics.ListAPIView):
    queryset = Scholarship.objects.all()
    serializer_class = SchoolSerializer

class TuitionFeesDetailView(generics.RetrieveAPIView):
    queryset = Scholarship.objects.all()
    serializer_class = SchoolSerializer