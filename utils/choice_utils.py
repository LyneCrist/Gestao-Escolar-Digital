motivos = {1: "Consulta agendada", 2: "Consulta cancelada", 3: "Consulta realizada"}


def filter_status_choices(transporte, status_choice):

    return {
        "id": transporte["pk"],
        "nome": transporte["nome"],
        "data": transporte["data"],
        "horario": transporte["horario"],
        "status": next(
            filter(lambda status: status[0] == transporte["status"], status_choice)
        )[1],
        "motivo": motivos[transporte["status"]],
    }
