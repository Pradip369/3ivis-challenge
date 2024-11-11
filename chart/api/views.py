from rest_framework import generics
from chart.models import GraphData
from .serializers import ChartDataSerializer


class ChartDataView(generics.ListAPIView):
    queryset = GraphData.objects.all()
    serializer_class = ChartDataSerializer

class ChartDataDetailView(generics.RetrieveAPIView):
    queryset = GraphData.objects.all()
    serializer_class = ChartDataSerializer
