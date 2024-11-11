from rest_framework import serializers
from chart.models import GraphData


class ChartDataSerializer(serializers.ModelSerializer):
    title = serializers.CharField()

    class Meta:
        model = GraphData
        fields = ['title','label','value']
