from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Specie, Pet, MedEspeciality, Veterinarian
from .form import PetForm, VeterinarianForm
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializers import SpecieSerializer, MedEspecialitySerializer,PetSerializer,VeterinarianSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes

# Create your views here.
#custom API
@api_view(["GET"]) 
def specie_count(request):
    #CANTIDAD DE ESPECIES#
    try:
        cantidad=Specie.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"message":str(e)},status=400)


def index(request):
    
    return render(request, 'index.html')

def contact(request, name):
    return HttpResponse(f"Hello, {name}. You're at the medhistory contact.")

def species(request):
    post_name = request.POST.get('name')

    if post_name:
        specie = Specie(name=post_name)
        specie.save()


    species = Specie.objects.all() 
    return render(request, 'form_species.html', {'species': species})

def petFormView(request):
    form = PetForm()
    pet = None
    id_pet = request.GET.get("id")
    if id_pet:
        pet = Pet.objects.get(id=id_pet)
        pet = get_object_or_404(Pet, id=id_pet)
        form = PetForm(instance=pet)

    if request.method == "POST":
        if pet:
            form = PetForm(request.POST, instance=pet)
        else:
            form = PetForm(request.POST)

    if form.is_valid():
        form.save()
    return render(request, 'form_pets.html', {'form': form})

def medespecialitys(request):
    post_name = request.POST.get('name')

    if post_name:
        medespeciality = MedEspeciality(name=post_name)
        medespeciality.save()


    medespecialitys = MedEspeciality.objects.all() 
    return render(request, 'form_medespecialitys.html', {'medespecialitys': medespecialitys})

def veterinarianFormView(request):
    form = VeterinarianForm()
    veterinarian = None
    id_veterinarian = request.GET.get("id")
    if id_veterinarian:
        veterinarian = Veterinarian.objects.get(id=id_veterinarian)
        veterinarian = get_object_or_404(Veterinarian, id=id_veterinarian)
        form = VeterinarianForm(instance=veterinarian)

    if request.method == "POST":
        if veterinarian:
            form = VeterinarianForm(request.POST, instance=veterinarian)
        else:
            form = VeterinarianForm(request.POST)

    if form.is_valid():
        form.save()
    return render(request, 'form_veterinarians.html', {'form': form})

class SpeciesViewSet(viewsets.ModelViewSet):
    queryset=Specie.objects.all()
    serializer_class=SpecieSerializer
    
class MedespecialitysViewSet(viewsets.ModelViewSet):
    queryset=MedEspeciality.objects.all()
    serializer_class=MedEspecialitySerializer
    
class PetsViewSet(viewsets.ModelViewSet):
    queryset=Pet.objects.all()
    serializer_class=PetSerializer
    
class VeterinariansViewSet(viewsets.ModelViewSet):
    queryset=Veterinarian.objects.all()
    serializer_class=VeterinarianSerializer
####    
class SpecieCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset=Specie.objects.all()
    serializer_class=SpecieSerializer