from django.db import models


class Role(models.Model):
    role_type = models.CharField(max_length=50)


class User(models.Model):
    role = models.ForeignKey('Role', blank=True, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=50)


class Service(models.Model):
    service_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)


class Review(models.Model):
    user = models.ForeignKey('User', blank=True, null=True, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, blank=True, null=True, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.CharField(max_length=300)


class Appointment(models.Model):
    user = models.ForeignKey('User', blank=True, null=True, on_delete=models.CASCADE)
    service = models.ForeignKey('Service', blank=True, null=True, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    is_available = models.BooleanField(blank=True, null=True)


class Payment(models.Model):
    appointment = models.ForeignKey('Appointment', blank=True, null=True, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=50)
    total = models.DecimalField(default=0, max_digits=6, decimal_places=2)
