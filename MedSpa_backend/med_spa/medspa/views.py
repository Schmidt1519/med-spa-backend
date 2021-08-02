from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import stripe
stripe.api_key = "sk_test_51JJVo1LbC0X6EBVPy6GyGTL3ZyajKbIrcNpd7w3nYoNdmhGp0v5DoIO1JSq8GWnmJurrQasOBhRcNsGwg5mveGTn00yQlC5EjN"

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restricted(request, *args, **kwargs):
    return Response(data="Only for Logged in User", status=status.HTTP_200_OK)

class UserList(APIView):

    def get(self, request):
        try:
            user = User.objects.all()
            serializer = UserSerializer(user, many=True)
            return Response(serializer.data)
        except User.DoesNotExist:
            raise Http404

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):

    def get_object(self, user):
        try:
            return User.objects.get(id=user)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, user):
        try:
            user = self.get_object(user)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            raise Http404

    def put(self, request, user):
        user = self.get_object(user)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user):
        user = self.get_object(user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AppointmentList(APIView):

    def get(self, request):
        try:
            appointment = Appointment.objects.all()
            serializer = AppointmentSerializer(appointment, many=True)
            return Response(serializer.data)
        except Appointment.DoesNotExist:
            raise Http404

    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppointmentDetail(APIView):

    def get_object(self, appointment):
        try:
            return Appointment.objects.get(id=appointment)
        except Appointment.DoesNotExist:
            raise Http404

    def get(self, request, appointment):
        try:
            appointment = self.get_object(appointment)
            serializer = AppointmentSerializer(appointment)
            return Response(serializer.data)
        except Appointment.DoesNotExist:
            raise Http404

    def put(self, request, appointment):
        appointment = self.get_object(appointment)
        serializer = AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, appointment):
        appointment = self.get_object(appointment)
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AppointmentByUser(APIView):

    def get_object(self, user):
        try:
            return Appointment.objects.filter(user=user)
        except Appointment.DoesNotExist:
            raise Http404

    def get(self, request, user):
        try:
            appointment = self.get_object(user)
            serializer = AppointmentSerializer(appointment, many=True)
            return Response(serializer.data)
        except Appointment.DoesNotExist:
            raise Http404

    def put(self, request, user):
        appointment = self.get_object(user)
        serializer = ServiceSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceList(APIView):

    def get(self, request):
        try:
            service = Service.objects.all()
            serializer = ServiceSerializer(service, many=True)
            return Response(serializer.data)
        except Service.DoesNotExist:
            raise Http404

    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceDetail(APIView):

    def get_object(self, service):
        try:
            return Service.objects.get(id=service)
        except Service.DoesNotExist:
            raise Http404

    def get(self, request, service):
        try:
            service = self.get_object(service)
            serializer = ServiceSerializer(service)
            return Response(serializer.data)
        except Service.DoesNotExist:
            raise Http404

    def put(self, request, service):
        service = self.get_object(service)
        serializer = ServiceSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, service):
        service = self.get_object(service)
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewList(APIView):

    def get(self, request):
        try:
            review = Review.objects.all()
            serializer = ReviewSerializer(review, many=True)
            return Response(serializer.data)
        except Review.DoesNotExist:
            raise Http404

    def post(self, request):
        serializer = AddReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetail(APIView):

    def get_object(self, review):
        try:
            return Review.objects.get(id=review)
        except Review.DoesNotExist:
            raise Http404

    def get(self, request, review):
        try:
            review = self.get_object(review)
            serializer = ReviewSerializer(review)
            return Response(serializer.data)
        except Review.DoesNotExist:
            raise Http404

    def put(self, request, review):
        review = self.get_object(review)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, review):
        review = self.get_object(review)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewUser(APIView):
    def get_object(self, user):
        try:
            return Review.objects.filter(user=user)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, user):
        try:
            review = self.get_object(user)
            serializer = ReviewSerializer(review, many=True)
            return Response(serializer.data)
        except User.DoesNotExist:
            raise Http404


class MembershipList(APIView):

    def get(self, request):
        try:
            membership = Membership.objects.all()
            serializer = MembershipSerializer(membership, many=True)
            return Response(serializer.data)
        except Membership.DoesNotExist:
            raise Http404

    def post(self, request):
        serializer = MembershipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MembershipDetail(APIView):

    def get_object(self, membership):
        try:
            return Membership.objects.get(id=membership)
        except Membership.DoesNotExist:
            raise Http404

    def get(self, request, membership):
        try:
            membership = self.get_object(membership)
            serializer = MembershipSerializer(membership)
            return Response(serializer.data)
        except Membership.DoesNotExist:
            raise Http404

    def put(self, request, membership):
        membership = self.get_object(membership)
        serializer = MembershipSerializer(membership, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, membership):
        membership = self.get_object(membership)
        membership.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MembershipByUser(APIView):

    def get_object(self, user):
        try:
            return Membership.objects.get(user=user)
        except Membership.DoesNotExist:
            raise Http404

    def get(self, request, user):
        try:
            membership = self.get_object(user)
            serializer = MembershipSerializer(membership)
            return Response(serializer.data)
        except Membership.DoesNotExist:
            raise Http404


class CartList(APIView):

    def get(self, request):
        try:
            cart = Cart.objects.all()
            serializer = CartSerializer(cart, many=True)
            return Response(serializer.data)
        except Cart.DoesNotExist:
            raise Http404

    def post(self, request):
        serializer = AddCartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartDetail(APIView):

    def get_object(self, user):
        try:
            return Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            raise Http404

    def get(self, request, user):
        try:
            cart = self.get_object(user)
            serializer = CartSerializer(cart)
            return Response(serializer.data)
        except Cart.DoesNotExist:
            raise Http404

    def put(self, request, user):
        cart = self.get_object(user)
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user):
        cart = self.get_object(user)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PaymentList(APIView):

    def get(self, request):
        try:
            payment = Payment.objects.all()
            serializer = PaymentSerializer(payment, many=True)
            return Response(serializer.data)
        except Payment.DoesNotExist:
            raise Http404

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentDetail(APIView):

    def get_object(self, payment):
        try:
            return Payment.objects.get(id=payment)
        except Payment.DoesNotExist:
            raise Http404

    def get(self, request, payment):
        try:
            payment = self.get_object(payment)
            serializer = PaymentSerializer(payment)
            return Response(serializer.data)
        except Payment.DoesNotExist:
            raise Http404

    def put(self, request, payment):
        payment = self.get_object(payment)
        serializer = PaymentSerializer(payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, payment):
        payment = self.get_object(payment)
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    class PaymentStripe(APIView):

        def post(self, request):
            stripe.Charge.create(
                amount=request.data['amount'],
                currency='usd',
                payment_method="card_1JJVxCLbC0X6EBVPh79MhCVX",
                receipt_email='schmidt1519@zohomail.com'
            )
