class TransporteError(Exception):

    def __init__(self, mensagem: str):
        self.message = mensagem


class CancelarTransporteError(Exception):

    def __init__(self, mensagem: str, descritiva: str):
        self.message = mensagem
        self.description = descritiva
