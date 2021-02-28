from django.http import HttpResponse
from django.template.loader import get_template


class HomeView():

    def home(self):
        plantilla = get_template('index.html')
        return HttpResponse(plantilla.render())

    def formularioAlumno(self):
        plantilla= get_template('formularioAlumno.html')
        return HttpResponse(plantilla.render())

    def menu(self):
        return HttpResponse('Ruta hacia el menú principal')

    def ruta2(self, parametro1):
        return HttpResponse('Ruta con parametro:  ' + str(parametro1))

    def ruta3(self, parametro1, parametro2):
        return HttpResponse('Ruta con 2 parametros, parametro1= ' + str(parametro1)+ ' parametro2 ='+str(parametro2))
