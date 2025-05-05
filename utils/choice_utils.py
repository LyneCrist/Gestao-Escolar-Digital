motivos = {1: "Consulta agendada", 2: "Consulta cancelada", 3: "Consulta realizada"}


def filter_status_choices(transporte, status_choice):

    return {
        "id": transporte["pk"],
        "nome": transporte["nome"],
        "data": transporte["data_criacao"],
        "data_alteracao": transporte["data_alteracao"],
        "status": next(
            filter(lambda status: status[0] == transporte["status"], status_choice)
        )[1],
        "motivo": motivos[transporte["status"]],
    }
