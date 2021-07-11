from .models import Personas

def find_persona(id):
    return Personas.objects.get(id=id)