from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template

def tarento_home(request):
	#Products = Producto.objects.order_by('id').reverse()[:8]
	Categorias = Categoria.objects.order_by('?')[:1]
	seccion1 = Seccion1.objects.order_by('titulo')[:3]
	seccion2 = Seccion2.objects.order_by('?')[:1]
	seccion3 = Seccion3.objects.order_by('?')[:1]
	Slides = Diapositivas.objects.order_by('prioridad')[:6]
	Galerias = Galeria.objects.reverse()[:6]
	Active = 'home'
	return render(request, 'index.html')

def tarento_nosotros(request):
	Active = 'nosotros'
	About = Nosotros.objects.reverse()[:1]
	Galerias = Galeria.objects.reverse()[:6]
	return render(request, 'nosotros.html', {'Active': Active, 'Galerias': Galerias, 'About': About})

def tarento_contacto(request):
	return render(request, 'contacto.html', {'Categorias': Categorias, 'form': form_class, 'Active': Active, 'Galerias': Galerias, 'Message': Message})

def tarento_privacy(request):
	Galerias = Galeria.objects.reverse()[:6]
	Policy = Privacidad.objects.reverse()[:1]
	return render(request, 'privacy.html', {'Galerias': Galerias, 'Policy': Policy})



def consult_privacy(request):
	Galerias = Galeria.objects.reverse()[:6]
	Policy = Privacidad.objects.reverse()[:1]
	return render(request, 'privacy.html', {'Galerias': Galerias, 'Policy': Policy})

def consult_sitemap(request):
	Catalogos = Catalogo.objects.order_by('id').reverse()
	Policy = Privacidad.objects.reverse()[:1]
	Categorias = Categoria.objects.order_by('id')
	Products = Producto.objects.order_by('id')
	Line = Linea.objects.order_by('id')
	return render(request, 'sitemap.xml', {'Catalogos': Catalogos, 'Policy': Policy, 'Categorias': Categorias, 'Products': Products, 'Line': Line}, content_type='text/xml')