from django.urls import path, include
from . import views

urlpatterns = [
    path('user/', views.UserList.as_view()),
    path('user/<int:user>/', views.UserDetail.as_view()),
    path('appointments/', views.AppointmentList.as_view()),
    path('appointments/<int:appointment>/', views.AppointmentDetail.as_view()),
    path('services/', views.ServiceList.as_view()),
    path('services/<int:service>/', views.ServiceDetail.as_view()),
    path('reviews/', views.ReviewList.as_view()),
    path('reviews/<int:review>/', views.ReviewDetail.as_view()),
    path('memberships/', views.MembershipList.as_view()),
    path('memberships/<int:membership>/', views.MembershipDetail.as_view()),
    path('carts/', views.CartList.as_view()),
    path('carts/<int:cart>/', views.CartDetail.as_view()),
    path('payments/', views.PaymentList.as_view()),
    path('payments/<int:payment>/', views.PaymentDetail.as_view()),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('restricted/', views.restricted),
]
