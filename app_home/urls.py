from django.urls import path
from . import views
from . views import (
    XlexHomeView,
    JurisprudenciasListView,
    SobreNosView,
    HumanrightsView,
    DireitosHumanosView
    )

app_name = 'app_home'

urlpatterns = [
    path('', XlexHomeView.as_view(), name='home-view'),
    path('contato/', views.contact_view, name='contact-us'),
    path('sobrenos/', SobreNosView.as_view(), name='sobre-nos'),
    path('jurisprudencias/', JurisprudenciasListView.as_view(), name='jurisprudencias-page-list'),
    path('humanos/', DireitosHumanosView.as_view(), name='direitos-humanos'),
    path('humans/', HumanrightsView.as_view(), name='humans-right'),
]