from django.urls import path
from .views import ChartDataView, ChartDataDetailView

urlpatterns = [
    path('chart_data/',ChartDataView.as_view(),name='chart_data'),
    path('chart_data/<int:pk>', ChartDataDetailView.as_view(), name='chart_data_detail'),
]
