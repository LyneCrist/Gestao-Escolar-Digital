# from datetime import datetime, time

# # 1 validação
# # start_time = time(8, 0, 0)
# # end_time = time(17, 0, 0)

# # hora_consulta = time(17, 1, 0)

# # if hora_consulta < start_time or hora_consulta > end_time:

# #     print(
# #         "Erro: Hora informada deve respeitar janela de atendimento, das 08hrs às 17hrs"
# #     )


# # 2 validação
# # STATUS_CHOICES = ((1, "Agendado"), (2, "Cancelado"), (3, "Realizado"))

# # users = [("user-kb001", 2), ("user-kb045", 1), ("user-kb025", 3)]


# # def filter_status(data, status_choice):
# #     return (
# #         data[0],
# #         next(filter(lambda status: status[0] == data[1], status_choice)),
# #     )


# # result = list(map(lambda user: filter_status(user, STATUS_CHOICES), users))

# # print(result)

# # 3 validção


# class TransporteError(Exception):

#     def __init__(self, *args) -> None:
#         self.message = self.message = args[0]

#     # def __str__(self) -> str:
#     #     return f"NotifyError, {self.message}"


# def validar_cancelamento(data_agendada: datetime):

#     notification: dict[str, str] = {}

#     data_atual = datetime.now()

#     # data_atual = datetime(2024, 5, 25, 15, 30)

#     duration = data_atual - data_agendada

#     hora = data_atual.time().hour

#     if duration.days < 1:

#         raise TransporteError(
#             [
#                 "Ação não permitida por período limite excedito",
#                 "O LIMITE PARA CANCELAMENTO É PERMITIDO COM UM DIA DE ANTECEDÊNCIA",
#             ],
#         )

#     elif duration.days == 1 and hora >= 18:

#         raise TransporteError(
#             [
#                 "Ação não permitida por limite de horário",
#                 "O CANCELAMENTO É PERMITIDO ATÉ ÀS 18HRS",
#             ],
#         )

#     else:

#         return notification


# try:

#     data_agendada = datetime(2024, 5, 25, 18, 25)

#     validar_cancelamento(data_agendada)

# except TransporteError as exc:

#     print("exc>>>>>", exc.message)


def calculate_value(input_value):
    # Perform calculations on the input value
    result = input_value * 2
    return result


# Example usage
value = 10
calculated_value = calculate_value(value)

print(calculated_value)  # Output: 20
