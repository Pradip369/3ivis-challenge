from django.contrib import admin
from .models import GraphData, GraphTitle


@admin.register(GraphTitle)
class GraphTitleAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "created_at", "updated_at"]
    search_fields = ["title"]
    list_display_links = list_display


@admin.register(GraphData)
class GraphDataAdmin(admin.ModelAdmin):
    list_display = ["id", "label", "value","created_at", "updated_at"]
    search_fields = ["lable"]
    list_display_links = list_display
