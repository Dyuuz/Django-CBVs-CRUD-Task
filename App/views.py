from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Car
from .forms import CreateCarForm, CarUpdateForm

class CarListView(ListView):
    model = Car
    template_name = 'list.html'
    
    # This is the context variable used in template to access the list of cars
    context_object_name = 'cars'

class CarCreateView(CreateView):
    model = Car
    form_class = CreateCarForm
    template_name = 'create.html'
    
    def form_valid(self, form):
        self.object = form.save() # Save the form data to the database

        # Redirect to the success URL after saving the form
        return HttpResponse('Car created successfully')
    
    def form_invalid(self, form):
        # Pass form errors to the template
        return self.render_to_response(self.get_context_data(form=form, errors=form.errors))

class CarUpdateView(UpdateView):
    model = Car
    form_class = CarUpdateForm
    template_name = 'update.html'
    success_url = reverse_lazy('car_list')

    def form_valid(self, form):
        self.object = form.save() # Save the form data to the database
        
        # Redirect to the success URL after saving the form
        return HttpResponse('Car updated successfully')
    
    def form_invalid(self, form):
        # Pass form errors to the template
        return self.render_to_response(self.get_context_data(form=form, errors=form.errors))

class CarDeleteView(DeleteView):
    model = Car
    success_url = reverse_lazy('car_list')
    template_name = 'cars/partials/car_confirm_delete.html'

    # Override the post method to handle the deletion of the object
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponse(status=204)

    # Override the get method to return a 405 Method Not Allowed response when a Get Request is made to this View
    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])
