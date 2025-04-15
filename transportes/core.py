from . import errors
from datetime import datetime, time


class TransporteCore:

    def __init__(self) -> None:
        pass

    def validar_cancelamento(self, data_agendada: datetime) -> None:

        print(">>>>>  data_agendada:", data_agendada)

        data_atual = datetime.now()

        # data_atual = datetime(2024, 5, 25, 15, 30)

        duration = data_atual - data_agendada

        hora = data_atual.time().hour

        if duration.days < 1:

            raise errors.CancelarTransporteError(
                "Ação não permitida, período limite excedito para o cancelamento",
                "O LIMITE PARA CANCELAMENTO É PERMITIDO ATÉ COM 1 DIA DE ANTECEDÊNCIA",
            )

        elif duration.days == 1 and hora >= 18:

            raise errors.CancelarTransporteError(
                "Ação não permitida, limite de horário excedido",
                "O CANCELAMENTO PARA ATÉ 1 DIA DE ANTECENDÊNCIA É PERMITIDO ATÉ ÀS 18HRS",
            )
