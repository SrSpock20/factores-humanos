"""ProyectoIngenieria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from proyectoApp.views import loginPrincipal, areas, pregunta_Filtro, cuestionario, mensaje, reportes, salir
from proyectoApp.views import area_max_resp, user_area_max, users_last_login, user_filter,supervisor,ver_preguntas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginPrincipal, name='login'),
    path('supervisor/',supervisor, name='supervisor'),
    path('areas/', areas,name='areas'),
    path('preguntafiltro/', pregunta_Filtro, name='preguntafiltro'),
    path('cuestionario/<int:pk>',cuestionario,name='cuestionario'),
    path('mensaje/', mensaje, name= 'mensaje'),
    path('reportes/', reportes, name='reportes'),
    path('areas-respondidas/', area_max_resp, name = 'areamax'),
    path('user-cuestionario-max/', user_area_max, name='user-cuestionario'),
    path('regitro-controlador/', users_last_login, name='registro-controlador'),
    path('filter-user/', user_filter, name = 'user-filter'),
    path('ver-preguntas/<int:pk>',ver_preguntas,name='ver_preguntas'),
    path('salir/', salir, name = 'salir'),
]
