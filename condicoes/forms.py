from django import forms
from .utils import (
    CONDICAO_FISICA_CHOICES,
    ACOMPANHANTE_CHOICES,
    CUIDADO_ESPECIAL_CHOICES,
)
from .models import Condicao
from common.util import CommonsUtil


class CondicaoForm(forms.ModelForm, CommonsUtil):

    condicao_fisica = forms.ChoiceField(
        label="Condição Física",
        required=False,
        widget=forms.Select(
            attrs={
                "name": "condicao_fisica",
                "id": "condicao_fisica",
            }
        ),
        choices=CONDICAO_FISICA_CHOICES,
    )

    descricao_condicao = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "name": "condicao_fisica",
                "id": "condicao_fisica",
                "rows": "5",
            },
        ),
    )

    acompanhante = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect(),
        choices=ACOMPANHANTE_CHOICES,
    )

    cuidado_especial = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect(),
        choices=CUIDADO_ESPECIAL_CHOICES,
    )

    descricao_cuidado = forms.CharField(
        label="Descrição Cuidado",
        required=False,
        widget=forms.Textarea(
            attrs={
                "name": "descricao_cuidado",
                "id": "descricao_cuidado",
                "rows": "5",
            },
        ),
    )

    class Meta:

        model = Condicao

        fields = "__all__"

        exclude = ["data_criacao", "data_alteracao"]

    def clean(self):

        super().clean()

        errors = {}

        # paciente_id = self.instance.pk

        # nome = self.cleaned_data.get("nome")

        # data_de_nascimento = self.cleaned_data.get("data_de_nascimento")

        # genero = self.cleaned_data.get("genero")

        # cartao_sus = self.cleaned_data.get("cartao_sus")

        # agendamento_fixo = self.cleaned_data.get("agendamento_fixo")

        # telefone = self.cleaned_data.get("telefone")

        # rua = self.cleaned_data.get("rua")

        # numero = self.cleaned_data.get("numero")

        # complemento = self.cleaned_data.get("complemento")

        # ponto_referencia = self.cleaned_data.get("ponto_referencia")

        # if not nome:
        #     errors["nome"] = "Campo nome obrigatório"

        # if nome:

        #     if len(nome) < 5 or len(nome) > 60:
        #         errors["nome"] = (
        #             "Certifique-se de que o valor tenha entre 5 a 60 caracteres"
        #         )

        #     elif not self.is_alpha_pattern(nome):
        #         errors["nome"] = (
        #             "Certifique-se de que o valor tenha apenas caracteres texto"
        #         )

        # if not data_de_nascimento:
        #     errors["data_de_nascimento"] = "Campo data de nascimento obrigatório"

        # if data_de_nascimento:

        #     ano = int(datetime.now().year - (data_de_nascimento.year))

        #     if ano == -1 or ano > 100:
        #         errors["data_de_nascimento"] = "Informe uma data de nascimento válida"

        # if not genero:
        #     errors["genero"] = "Campo gênero obrigatório"

        # if not cartao_sus:
        #     errors["cartao_sus"] = "Campo cartão SUS obrigatório"

        # if cartao_sus:

        #     if len(cartao_sus) != 15:
        #         errors["cartao_sus"] = (
        #             "Campo cartão SUS deve possuir um tamanho de 15 dígitos"
        #         )

        #     elif not self.is_numeric_pattern(cartao_sus):
        #         errors["cartao_sus"] = (
        #             "Formato de campo inválido para cartão SUS, informe apenas números"
        #         )
        #     else:

        #         if paciente_id:

        #             if (
        #                 Condicao.objects.filter(cartao_sus=cartao_sus)
        #                 .exclude(id=paciente_id)
        #                 .exists()
        #             ):
        #                 errors["cartao_sus"] = (
        #                     "Já existe um mesmo Cartão SUS cadastrado"
        #                 )
        #         elif Condicao.objects.filter(cartao_sus=cartao_sus).exists():
        #             errors["cartao_sus"] = "Já existe um mesmo Cartão SUS cadastrado"

        # if not agendamento_fixo:
        #     errors["agendamento_fixo"] = "Selecione uma opção para agendamento fixo"

        # if not telefone:
        #     errors["telefone"] = "Campo telefone obrigatório"

        # if telefone:

        #     telefone = self.remove_characters(telefone)

        #     if len(telefone) != 13 or not self.is_phone_pattern(telefone):
        #         errors["telefone"] = (
        #             "Certifique-se de que o número de telefone esteja correto"
        #         )

        #     else:
        #         self.cleaned_data["telefone"] = telefone

        # if not rua:
        #     errors["rua"] = "Campo rua obrigatório"

        # if rua:

        #     if len(rua) < 5 or len(rua) > 60:
        #         errors["rua"] = (
        #             "Certifique-se de que o valor tenha entre 5 a 60 caracteres"
        #         )

        #     elif not self.is_alpha_numeric_character_pattern(rua):
        #         errors["rua"] = (
        #             "Certifique-se de que o valor tenha apenas caracteres texto"
        #         )

        # if not numero:
        #     errors["numero"] = "Campo número obrigatório"

        # if numero:

        #     if len(numero) > 7:
        #         errors["numero"] = (
        #             "Certifique-se de que o valor tenha no máximo 7 caracteres"
        #         )

        #     elif not self.find_numbers(numero):
        #         errors["numero"] = "Certifique-se de que valor informado tenha números"

        #     elif not self.is_alpha_numeric_character_pattern(numero):
        #         errors["numero"] = (
        #             "Certifique-se de que valor informado seja um número de endereço válido"
        #         )

        # if complemento:

        #     if len(complemento) < 5 or len(complemento) > 60:
        #         errors["complemento"] = (
        #             "Certifique-se de que o valor tenha entre 5 a 60 caracteres"
        #         )

        #     elif not self.is_alpha_numeric_character_pattern(complemento):
        #         errors["complemento"] = (
        #             "Certifique-se de que o valor tenha apenas caracteres texto"
        #         )

        # if ponto_referencia:

        #     if len(ponto_referencia) < 5 or len(ponto_referencia) > 60:
        #         errors["ponto_referencia"] = (
        #             "Certifique-se de que o valor tenha entre 5 a 60 caracteres"
        #         )

        #     elif not self.is_alpha_numeric_character_pattern(ponto_referencia):
        #         errors["ponto_referencia"] = (
        #             "Certifique-se de que o valor tenha apenas caracteres texto"
        #         )

        if errors:

            for key in errors.keys():
                self.fields[key].label_suffix = ": *"

            raise forms.ValidationError(errors)

        return self.cleaned_data
