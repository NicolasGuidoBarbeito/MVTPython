from django.shortcuts import render
from AppCoder.models import Familiar

# Create your views here.
def familiares(request):

    familiar1 = Familiar(nombre="Fabiana", edad=60, nacimiento="1962-08-20", parentesco="Mama")
    familiar2 = Familiar(nombre="Tomas", edad=25, nacimiento="1996-11-01", parentesco="Hermano") 
    familiar3 = Familiar(nombre="Roberto", edad=62, nacimiento="1960-10-05", parentesco="Papa") 

    familiar1.save()
    familiar2.save()
    familiar3.save()

    listaFamiliares = {'familiares': [familiar1, familiar2, familiar3]}

    return render(request, 'template1.html', listaFamiliares)