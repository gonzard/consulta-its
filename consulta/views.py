from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from bakery.views import BuildableTemplateView

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


class BuildableIndexView (BuildableTemplateView):
	build_path = 'index.html'
	template_name = 'index.html'

class BuildableClientesView (BuildableTemplateView):
	build_path = 'clientes.html'
	template_name = 'clientes.html'

class BuildableFaqView (BuildableTemplateView):
	build_path = 'faq.html'
	template_name = 'faq.html'

class BuildableNosotrosView (BuildableTemplateView):
	build_path = 'nosotros.html'
	template_name = 'nosotros.html'

class BuildableContacto (BuildableTemplateView):
	build_path = 'contacto.html'
	template_name = 'contacto.html'

class BuildableServicio (BuildableTemplateView):
	build_path = 'servicios.html'
	template_name = 'servicios.html'

class BuildableSitemap (BuildableTemplateView):
	build_path = 'sitemap.xml'
	template_name = 'sitemap.xml'
