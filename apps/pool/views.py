from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormMixin
from .models import Actions, Certificate, Service
from .forms import LeadForms
from django.urls import reverse_lazy
from django.contrib import messages


class PoolView(FormMixin, ListView):
    model = Actions
    form_class = LeadForms
    ordering = '-created_at'
    template_name = 'pool/index.html'
    success_url = reverse_lazy('main_page')

    def get_queryset(self):
        return Actions.objects.filter(is_active=True).order_by('-created_at')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            self.object_list = self.get_queryset()
            return self.form_invalid(form)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance._request = self.request
        instance.save()
        messages.success(self.request, 'Заявка отправлена! Мы скоро свяжемся с вами.')
        return redirect(reverse_lazy('main_page') + '#form')
    
    def form_invalid(self, form):
        self.object_list = self.get_queryset()
        messages.error(self.request, 'Проверьте правильность заполнения формы.')
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["certificates"] = Certificate.objects.all()
        context["services"] = Service.objects.filter(is_active=True)
        return context


class PoliticView(TemplateView):
    template_name = "pool/privacy.html"
