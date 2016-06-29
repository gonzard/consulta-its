from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template

def consult_home(request):
	return render(request, 'index.html')

def consult_nosotros(request):
	return render(request, 'nosotros.html')

def consult_servicios(request):
	return render(request, 'servicios.html')

def consult_soluciones(request):
	return render(request, 'soluciones.html')

def consult_clientes(request):
	return render(request, 'clientes.html')

def consult_contacto(request):
	return render(request, 'contacto.html')

def consult_faq(request):
	return render(request, 'faq.html')

def consult_sitemap(request):
	return render(request, 'sitemap.xml', content_type = 'text/xml')