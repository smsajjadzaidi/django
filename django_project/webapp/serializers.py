from rest_framework import serializers
from .models import Employees, Users
import re


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'

    def validate_first_name(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("length must be greater than 5")

        return value


def check_email(email):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if re.search(regex, email):
        pass
    else:
        raise serializers.ValidationError("Invalid Email!")


class UsersSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=10)
    last_name = serializers.CharField(max_length=10)
    email = serializers.EmailField(max_length=254, validators=[check_email])
    full_name = serializers.SerializerMethodField('fullname')

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return Users.objects.create(**validated_data)

    def validate(self, data):
        if data.get('first_name') == data.get('last_name'):
            raise serializers.ValidationError("First name and Last name cant be same!")
        return data

    def fullname(self, obj):
        return obj.first_name + " " + obj.last_name


