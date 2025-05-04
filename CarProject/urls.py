"""
URL configuration for CarProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from App.views import CarListView, CarCreateView, CarUpdateView, CarDeleteView

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('', include('App.urls')),

    # i18n_patterns will automatically add the language prefix to the URLs
    # based on the user's selected language.
    *i18n_patterns(
        path('', CarListView.as_view(), name='home'),
        path('add/', CarCreateView.as_view(), name='car_add'),
        path('car/<int:pk>/edit', CarUpdateView.as_view(), name='car_edit'),
        path('car/<int:pk>/delete', CarDeleteView.as_view(), name='car_delete'),
    ),
]
