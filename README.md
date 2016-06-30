##########
Consulta ITS
##########
.. image:: http://consulta-its.com/static/logo.png
    :target: http://consulta-its.com

Sitio web corporativo para http://consulta-its.com Generado en Python con el framework de Django, las vistas son renderizadas a HTML con django-bakery,
Todas las herramientas utilizadas para la creación de este website son OpenSource.


.. ATENCIÓN::

    Toda nueva característica deseada se debe añadir al canal maestro de GIT.

    No existen Bugs identificados al momento de la publicación de este sitio web.


********
Características
********

* Páginas con jerarquía
* Soporte para fontawesome
* Soporte para clonarse a otros sitios
* Templates creados con el lenguaje Jinja2
* Los archivos estáticos no son incluídos en este documento pues son propiedad del cliente
* Página de contacto creada en php 
* Newsletter sincronizado con MailChimp, editar el archivo base.html para personalizar
* Tres niveles de Jerarquía soportados
* Archivo de sitemaps generado manualmente
* Preparado para SEO


Más información con <http://codelab.mx>`_.

************
Requisitos
************
Para poder generar páginas dinámicamente sin necesidad de una base de datos se requiere

Sistema operativo Windows, Linux o Unix

Python 2.7
*Pip (Recomendable para instalar los paquetes adicionales) = https://pip.pypa.io/en/stable/installing/
Django 1.9 > 'pip install django'
Django Bakery 'pip install django-bakery'

Servidor Nginx o Apache

*************
Documentación
*************

Információn adicional <info@codelab.mx>`_ para todos los detalles de como instalar, extender y utilizar este software


***********
Expansión rápida
***********
Puedes usar el instalador de django en un entorno virtual

<https://djangocms-installer.readthedocs.io>`_::

    $ pip install --upgrade virtualenv
    $ virtualenv env
    $ source env/bin/activate
    (env) $ pip install django
    (env) $ pip install django-bakery
    (env) $ mkdir consultaits && cd consultaits
    (env) $ python manage.py runserver


************
Soporte
************
Para ayuda sobre como clonar el proyecto y editarlo consulte con http://codelab.mxl.

******************
Soporte Adicional
******************

Este proyecto es creado por 'Codelab MX' Grupo Teklan S.R.L. de C.V. para el dominio http://consulta-its.com 
Si se requiere implementar o alojar este producto puede contactar al correo:
info@codelab.mx.
