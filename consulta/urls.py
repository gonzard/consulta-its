from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^www/$', views.consult_home),
	url(r'^www/nosotros\.html/$', views.consult_nosotros),
    url(r'^www/servicios\.html/', views.consult_servicios),
    url(r'^www/soluciones\.html/', views.consult_soluciones),
    url(r'^www/clientes\.html/$', views.consult_clientes),
    url(r'^www/contacto\.html/$', views.consult_contacto),
    url(r'^www/faq\.html/$', views.consult_faq),
    url(r'^www/sitemap\.xml/$', views.consult_sitemap),
]
