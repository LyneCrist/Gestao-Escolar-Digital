from django import template
from django.forms.boundfield import BoundField

register = template.Library()


# @register.filter(name="is_fieldset")
# def is_fieldset(field: BoundField) -> bool:
#     return True if field in ["genero", "agendamento_fixo"] else False


# @register.filter(name="set_label")
# def set_label(field: BoundField) -> str:

#     fields = {"genero": "Gênero", "agendamento_fixo": "Agendamento Fixo"}

#     return f"{fields[field.name]} *" if field.errors else fields[field.name]


@register.filter(name="set_column_input")
def set_column_input(field: BoundField) -> str:

    fields = {
        "data_de_transporte": "col-2",
        "horario_de_atendimento": "col-2",
        "motivo_de_transporte": "col-2",
        "descricao_motivo": "col-5",
        "rua": "col-5",
        "bairro": "col-5",
        "numero": "col-2",
        "cidade": "col-5",
        "destino": "col-5",
        "observacao": "col-5",
    }

    return fields[field.name]


@register.filter(name="set_status")
def set_status(status: str) -> str:

    return {
        "CANCELADO": "status-cancelado",
        "AGENDADO": "status-agendado",
        "FINALIZADO": "status-finalizado",
    }[status.upper()]
