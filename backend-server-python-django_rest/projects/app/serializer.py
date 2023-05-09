from rest_framework import serializers
from . models import *
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Users
        fields = ['id', 'username', 'email', 'password', 'created_at', 'updated_at']
        # Khong hien th nen api chi dung dc post va put
        #extra_kwargs = {'name_ma_hoa_khac':{'write_only':True}}
    
    def create(self, validated_data):
        user = Users.objects.create(
            username= validated_data['username'],
            email= validated_data['email'],
            # mã hoá passowrd
            password= make_password(validated_data['password'])
        )
       
        return user

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields =['employee', 'department']