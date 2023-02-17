from django.contrib import admin
from django.urls import path
from .views import (
    CreateCheckoutSessionView,
    SuccessView,
    CancelView,
    ProductLandingPageView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('buy/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('', ProductLandingPageView.as_view(), name='landing'),
]
