from django.urls import path
from .views import CarListView, CarCreateView, CarUpdateView, CarDeleteView
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('add/', CarCreateView.as_view(), name='car_add'),
    path('car/<int:pk>/edit', CarUpdateView.as_view(), name='car_edit'),
    path('car/<int:pk>/delete', CarDeleteView.as_view(), name='car_delete'),
]
