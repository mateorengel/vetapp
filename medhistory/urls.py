from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from views import specie_count

router= DefaultRouter()
router.register(r'species',views.SpeciesViewSet)
router.register(r'medespecialitys',views.MedespecialitysViewSet)
router.register(r'pets',views.PetsViewSet)
router.register(r'veterinarians',views.VeterinariansViewSet)

urlpatterns = [
    #path('', views.index),
    # path('contact/<str:name>', views.contact, name='contact'),
    # path('species/', views.species, name='species'),
    # path('pets/', views.petFormView, name='pets'),
    # path('medespecialitys/', views.medespecialitys, name='medespecialitys'),
    # path('veterinarians/', views.veterinarianFormView, name='veterinarians'),
    path('species/cantidad',views.specie_count),
    path('',include(router.urls))
]
