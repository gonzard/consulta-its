from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.consult_home),
	url(r'^nosotros\.html/$', views.consult_nosotros),
    url(r'^servicios\.html/', views.consult_servicios),
    url(r'^soluciones\.html/', views.consult_soluciones),
    url(r'^clientes\.html/$', views.consult_clientes),
    url(r'^contacto\.html/$', views.consult_contacto),
    url(r'^faq\.html/$', views.consult_faq),
    url(r'^sitemap\.xml/$', views.consult_sitemap),
]
