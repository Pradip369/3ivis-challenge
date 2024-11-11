from django.db import models
from config.base_model import TimestampedModel


class GraphTitle(TimestampedModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class GraphData(TimestampedModel):
    title = models.ForeignKey(GraphTitle, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    value = models.FloatField()

    def __str__(self):
        return self.label
