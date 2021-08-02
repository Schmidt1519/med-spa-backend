from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=100, unique=True)
    phone = models.CharField(null=True, max_length=50)

    # add fields you would like to update in database
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email


class Appointment(models.Model):
    user = models.ForeignKey('User', null=True, on_delete=models.CASCADE)
    service = models.ForeignKey('Service', null=True, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    is_available = models.BooleanField(null=True, default=True)


class Service(models.Model):
    image = models.CharField(max_length=300)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=800)


class Review(models.Model):
    user = models.ForeignKey('User', null=True, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.CharField(max_length=300)


class Membership(models.Model):
    user = models.ForeignKey('User', null=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    detail = models.CharField(max_length=50)
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    is_active = models.BooleanField(null=True, default=True)


class Cart(models.Model):
    user = models.ForeignKey('User', null=True, on_delete=models.CASCADE)
    membership = models.ForeignKey('Membership', null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)


class Payment(models.Model):
    cart = models.ForeignKey('Cart', null=True, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=50)
    total = models.DecimalField(default=0, max_digits=6, decimal_places=2)
