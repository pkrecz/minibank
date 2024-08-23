# -*- coding: utf-8 -*-

from django.views.generic import ListView
from .models import CustomerModel

class SelectCustomerListView(ListView):
    
    def get_queryset_customer(self, criteria):
        criterias = self.request.GET.get(criteria)
        Pesel_results = CustomerModel.objects.filter(Pesel__startswith=criterias).order_by('-pk')
        Identification_results = CustomerModel.objects.filter(Identification__istartswith=criterias).order_by('-pk')
        if Pesel_results.exists():
            return Pesel_results
        elif Identification_results.exists():
            return Identification_results
        else:
            return CustomerModel.objects.none()
