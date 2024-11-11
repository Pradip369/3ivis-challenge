from django.urls import path
from .views import custom_charts

app_name = "charts"

urlpatterns = [
    path('custom_charts/', custom_charts, name='custom_charts'),
]

