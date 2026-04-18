from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Actions
from .forms import LeadForms


class PoolView(ListView):
    model = Actions
    ordering = '-created_at'
    template_name = 'pool/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = getattr(self, 'form', LeadForms())
        return context

    def post(self, request, *args, **kwargs):
        form = LeadForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page')

        self.form = form
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        return render(request, self.template_name, context)
