from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import *


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone']


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ['id', 'user', 'service', 'date', 'start_time', 'end_time', 'is_available']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'image', 'name', 'description']


class ReviewSerializer(serializers.ModelSerializer):
#    user = UserCreateSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'rating', 'review']


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ['id', 'user', 'type', 'detail', 'price', 'is_active']


class CartSerializer(serializers.ModelSerializer):
    membership = MembershipSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'membership', 'quantity']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'cart', 'payment_type', 'total']
