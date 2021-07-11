from .models import Personas



def list_personas(limit=10):
    return Personas.objects.filter().order_by('-id')[:limit]


def find_persona(id):
    return Personas.objects.get(id=id)