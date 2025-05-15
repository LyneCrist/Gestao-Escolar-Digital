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
        # "data_de_transporte": "col-2",
        # "horario_de_atendimento": "col-2",
        # "motivo_de_transporte": "col-2",
        "descricao_motivo": "col-5",
        "nota": "col-2",
        "materia": "col-5",
        # "rua": "col-5",
        # "bairro": "col-5",
        # "numero": "col-2",
        # "cidade": "col-5",
        # "destino": "col-5",
        "observacao": "col-5",
    }

    return fields[field.name]


@register.filter(name="set_status")
def set_status(status_value, status_choices=None):
    # Mapeamento de status para classes CSS
    status_classes = {
        'Reprovado': 'status-reprovado',
        'Aprovado': 'status-aprovado',
        'Pendente': 'status-pendente',
        # Adicione outros status conforme necessário
        '': 'status-default'  # Fallback para status vazio
    }
    
    # Verifica se o status existe no mapeamento
    return status_classes.get(status_value, 'status-default')