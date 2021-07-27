from django.db import models


class Client(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)


class Appointment(models.Model):
    client = models.ForeignKey('Client', null=True, on_delete=models.CASCADE)
    service = models.ForeignKey('Service', null=True, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    is_available = models.BooleanField(null=True, default=True)


class Service(models.Model):
    service_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)


class Review(models.Model):
    service = models.ForeignKey('Service', null=True, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.CharField(max_length=300)


class Membership(models.Model):
    client = models.ForeignKey('Client', null=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    detail = models.CharField(max_length=50)
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)


class Cart(models.Model):
    client = models.ForeignKey('Client', null=True, on_delete=models.CASCADE)
    membership = models.ForeignKey('Membership', null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Payment(models.Model):
    cart = models.ForeignKey('Cart', null=True, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=50)
    total = models.DecimalField(default=0, max_digits=6, decimal_places=2)
