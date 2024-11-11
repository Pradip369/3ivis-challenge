from django import forms
from .models import GraphTitle

CHART_TYPE_CHOICES = [
    ("", "Choose an option"),
    ('pieChart', 'Pie Chart'),
    ('discreteBarChart', 'Discrete BarChart'),
]


class ChartForm(forms.Form):
    chart_title = forms.ModelChoiceField(queryset=GraphTitle.objects.only('title'),
                                         widget=forms.Select(attrs={'class': 'form-control'}))
    chart_type = forms.ChoiceField(choices=CHART_TYPE_CHOICES,
                                   widget=forms.Select(attrs={'class': 'form-control'}))
