from rest_framework import serializers
from .models import Role
from .models import User
from .models import Service
from .models import Review
from .models import Appointment
from .models import Payment


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'role_type']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'role', 'username', 'first_name' 'last_name', 'email_address', 'phone_number']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'service_name', 'description', 'price']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'service', 'rating', 'review']


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'user', 'service', 'date', 'start_time', 'end_time', 'is_available']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'appointment', 'payment_type', 'total']
