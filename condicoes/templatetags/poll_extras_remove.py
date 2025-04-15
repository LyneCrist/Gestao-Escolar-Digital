from django import template
from django.forms.boundfield import BoundField

register = template.Library()


@register.filter(name="is_fieldset")
def is_fieldset(field: BoundField) -> bool:
    return True if field in ["genero", "agendamento_fixo"] else False


@register.filter(name="set_label")
def set_label(field: BoundField) -> str:

    fields = {"genero": "Gênero", "agendamento_fixo": "Agendamento Fixo"}

    return f"{fields[field.name]} *" if field.errors else fields[field.name]


@register.filter(name="set_column_input")
def set_column_input(field: BoundField) -> str:

    fields = {
        "nome": "col-5",
        "data_de_nascimento": "col-1",
        "genero": "col-5",
        "cartao_sus": "col-2",
        "agendamento_fixo": "col-5",
        "telefone": "col-2",
        "rua": "col-5",
        "numero": "col-2",
        "complemento": "col-4",
        "ponto_referencia": "col-4",
    }

    return fields[field.name]
