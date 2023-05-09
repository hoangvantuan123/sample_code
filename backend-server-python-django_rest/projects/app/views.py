from django.shortcuts import render
from  rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
from django.views.generic import TemplateView
from rest_framework import generics
# Create your views here.

class HomeView(TemplateView):
    template_name ="home.html"

class ReactView(APIView):
    serializer_class = ReactSerializer
    def get(self, request):
        output = [{"employee": output.employee , "department": output.department}
                  for output in React.objects.all()]
        return Response(output)
    
    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
#
class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = Users.objects.all()

class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    serializers = UserSerializer
    queryset = Users.objects.all()


