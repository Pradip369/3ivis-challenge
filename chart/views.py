from django.shortcuts import render
from .models import GraphData
from .forms import ChartForm
from django.contrib.auth.decorators import login_required

@login_required
def custom_charts(request):
    form = ChartForm()
    graph_data = GraphData.objects.filter(title__id=1).values_list('label', 'value', named=True)
    chart_type = "pieChart"
    if request.method == "POST":
        form = ChartForm(request.POST)
        if form.is_valid():
            chart_title = form.cleaned_data['chart_title']
            chart_type = form.cleaned_data['chart_type']
            graph_data = GraphData.objects.filter(title=chart_title).values_list('label', 'value', named=True)
    xdata, ydata = [lbl.label for lbl in graph_data], [val.value for val in graph_data]
    chart_data = {'x': xdata, 'y': ydata}
    chart_container = 'piechart_container' if chart_type == 'pieChart' else 'discretebarchart_container'
    data = {
        'chart_type': chart_type,
        'chart_data': chart_data,
        'chart_container': chart_container,
        'form':form
    }
    return render(request, 'chart/custom_charts.html', data)
