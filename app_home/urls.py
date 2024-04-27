from django.urls import path
from . import views
from . views import XlexHomeView, JurisprudenciasListView, SobreNosView

app_name = 'app_home'

urlpatterns = [
    path('', XlexHomeView.as_view(), name='home-view'),
    path('contato/', views.contact_view, name='contact-us'),
    path('sobre-nos/', SobreNosView.as_view(), name='sobre-nos'),
    path('jurisprudencias/', JurisprudenciasListView.as_view(), name='jurisprudencias-page-list'),
]