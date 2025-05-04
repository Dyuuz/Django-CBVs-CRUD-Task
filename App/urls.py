from django.urls import path
from .views import CarListView, CarCreateView, CarUpdateView, CarDeleteView

urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('add/', CarCreateView.as_view(), name='car_add'),
    path('car/<int:pk>/edit', CarUpdateView.as_view(), name='car_edit'),
    path('car/<int:pk>/delete', CarDeleteView.as_view(), name='car_delete'),
]
