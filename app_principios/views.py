from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from typing import Any
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.aggregates import Count
from random import randint
from django.http import JsonResponse
from django.http import HttpRequest, HttpResponse
from django.utils import timezone
from app_manager .models import PageView

from django.views.generic import (
    ListView,
    DateDetailView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import (
    PrincipiosModel,
    RamoDireitoModel,
)

from .forms import (
    CreatePrincipioForm,
    UpdatePrincipioForm,
)

class PrincipiosListView(ListView):
    model = PrincipiosModel
    template_name = 'templates_principios/principios_list.html'
    ordering = ['-date_created']
    paginate_by = 12
    context_object_name = 'principios'
    
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['publicacoes_count'] = PrincipiosModel.objects.all().count()
        context["hide_sidebar"] = True
        context['canonical_url'] = self.request.build_absolute_uri(reverse('app_principios:principios-list'))
        return context
    
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        page, created = PageView.objects.get_or_create(
            page_name="Lista de Princípios",
            defaults={'last_accessed': timezone.now()}
        )
        if not created:
            page.view_count += 1
            page.last_accessed = timezone.now()
            page.save()

        return super().get(request, *args, **kwargs)

class PrincipiosSingleView(DetailView):
    model = PrincipiosModel
    template_name = 'templates_principios/principio_single.html'
    slug_field = 'slug'
    context_object_name = 'principios'
    reverse_lazy = reverse_lazy('app_principios:principios-list')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        principio_Direitoname = self.object.principio_name
        self.object.update_views() 
        
        page, created = PageView.objects.get_or_create(
            page_name=f"Principio post: {principio_Direitoname}",
            defaults={'last_accessed': timezone.now()}
        )
        if not created:
            page.view_count += 1
            page.last_accessed = timezone.now()
            page.save()
        
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['ramos'] = RamoDireitoModel.objects.all()
        principios = self.get_object()
        context['indexable'] = principios.is_indexable()
        context['current_app'] = 'app_principios'
        context['canonical_url'] = self.request.build_absolute_uri(
            reverse('app_principios:principio-single', kwargs={'slug': self.object.slug})
        )
        return context
        return context
    
class RamoDireitoListView(ListView):
    model = RamoDireitoModel
    template_name = 'templates_principios/principios_ramos_list.html'
    context_object_name = 'principios'
    
    def get_queryset(self):
        self.ramo = RamoDireitoModel.objects.get(slug=self.kwargs['ramo_slug'])
        return PrincipiosModel.objects.filter(ramo_direito=self.ramo)
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({
            'ramo': self.ramo,
            'ramos': RamoDireitoModel.objects.all(),
            'current_app': 'app_principios',
        })
        return context

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        page, created = PageView.objects.get_or_create(
            page_name=f"Principios: Ramos do Direito - {self.kwargs.get('ramo_slug', 'Unknown')}",
            defaults={'last_accessed': timezone.now()}
        )
        if not created:
            page.view_count += 1
            page.last_accessed = timezone.now()
            page.save()

        return super().get(request, *args, **kwargs)


# Class Create
class PrincipioCreateView(CreateView):
    model = PrincipiosModel
    template_name = 'templates_principios/principios_create.html'
    form_class = CreatePrincipioForm
    success_url = reverse_lazy('app_principios:principio-single')
    
    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.principio_name)
        response = super(PrincipioCreateView, self).form_valid(form)
        return response
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["hide_sidebar"] = True
        context['current_app']: 'app_principios'
        return context
    
    def get_success_url(self):
        return reverse('app_principios:principio-single', kwargs={'slug': self.object.slug})

class UpdatePrincipioView(UpdateView):
    model = PrincipiosModel
    form_class = UpdatePrincipioForm
    template_name = 'templates_principios/principio_update.html'
    success_url = reverse_lazy('app_principios:principios-list')
    
class DeletePrincipioView(DeleteView):
    model = PrincipiosModel
    template_name = 'templates_principios/principio_delete.html'
    success_url = reverse_lazy('app_principios:principios-list')