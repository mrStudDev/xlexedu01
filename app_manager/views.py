from django.shortcuts import render
from django.utils import timezone
from .models import PageView, DailyPageView
from typing import Any
from django.db.models import Sum

from django.views.generic import (
    ListView,
    DateDetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


class ManagerView(ListView):
    model = PageView
    template_name = 'templates_manager/manager_admin.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Buscando todos os PageViews
        context['page'] = PageView.objects.all()

        # Ordenando os PageViews pela contagem de visualizações (decrescente)
        context['pages'] = PageView.objects.all().order_by('-view_count')

        # Formatando a data e hora em cada PageView
        for page in context['pages']:
            page.last_accessed = page.last_accessed.strftime("%d de %b de %Y às %H:%M")

        # Calculando o total de visualizações de todas as páginas
        context['total_views'] = PageView.objects.aggregate(total=Sum('view_count'))['total'] or 0

        # Configurações adicionais para o template (provavelmente relacionadas ao layout)
        context["hide_sidebar"] = True
        context['current_app'] = 'app_manager'

        # Obtendo as visualizações diárias de cada página
        daily_views = DailyPageView.objects.values('date').annotate(total=Sum('view_count')).order_by('-date')
        context['daily_views'] = daily_views

        return context
    
def update_page_view(page_name):
    page_view, _ = PageView.objects.get_or_create(page_name=page_name)
    page_view.view_count += 1
    page_view.last_accessed = timezone.now()
    page_view.save()

    today = timezone.now().date()
    daily_view, created = DailyPageView.objects.get_or_create(page=page_view, date=today)
    if not created:
        daily_view.view_count += 1
        daily_view.save()