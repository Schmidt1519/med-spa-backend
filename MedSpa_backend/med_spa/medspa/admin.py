from django.contrib import admin
from .models import Client, Appointment, Service, Review, Membership, Cart, Payment


# Register your models here.
admin.site.register(Client)
admin.site.register(Appointment)
admin.site.register(Service)
admin.site.register(Review)
admin.site.register(Membership)
admin.site.register(Cart)
admin.site.register(Payment)
