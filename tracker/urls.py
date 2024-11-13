from django.urls import path

from . import views

urlpatterns = [
    # path("hi", views.fetch_historical_data, name="index"),
    # path('chart/', views.chart_view, name='chart_view'),
    path("", views.render_chart, name='render_chart'),
]