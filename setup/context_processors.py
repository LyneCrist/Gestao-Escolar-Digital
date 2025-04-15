from django.conf import settings


def global_variables(request):
    return {"FIELDSET_LEGENDS": ["genero", "agendamento_fixo"]}
