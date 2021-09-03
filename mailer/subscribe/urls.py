from django.urls import path
from .views import subscribe_for_newsletter,thank_you


urlpatterns = [
    path('', subscribe_for_newsletter,name='subscribe-for-newsletter'),
    path('thank-you/',thank_you,name='thank-you'),
]


app_name = 'subscribe'