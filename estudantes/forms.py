# from asyncio.windows_events import NULL
from django import forms

from .choices import GENERO_CHOICES
from .models import Estudante
from common.util import CommonsUtil

from datetime import datetime


class EstudanteForm(forms.ModelForm, CommonsUtil):

    nome = forms.CharField(
        max_length=60,
        required=False,
        widget=forms.TextInput(
            attrs={
                "name": "nome",
                "id": "nome",
                "autocomplete": "off",
            }
        ),
    )

    data_de_nascimento = forms.DateField(
        label="Data de Nascimento",
        required=False,
        input_formats=["%Y-%m-%d"],
        widget=forms.DateInput(
            format="%Y-%m-%d",
            attrs={
                "type": "date",
                "name": "dataNascimento",
                "id": "dataNascimento",
                "autocomplete": "off",
            },
        ),
    )

    genero = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect(),
        choices=GENERO_CHOICES,
    )

    ad = forms.CharField(
        label="AD",
        max_length=11,
        required=False,
        widget=forms.TextInput(
            attrs={
                "name": "ad",
                "id": "ad",
                "placeholder": "000000000000000",
                "autocomplete": "off",
            }
        ),
    )

    celular = forms.CharField(
        label="Celular",
        max_length=18,
        required=False,
        widget=forms.TextInput(
            attrs={
                "name": "celular",
                "id": "celular",
                "placeholder": "+55(00) 00000-0000",
                "autocomplete": "off",
            }
        ),
    )

    class Meta:

        model = Estudante

        fields = "__all__"

        exclude = ["status", "data_criacao"]

    def clean(self):

        super().clean()

        errors = {}

        estudante_id = self.instance.pk

        nome = self.cleaned_data.get("nome")

        data_de_nascimento = self.cleaned_data.get("data_de_nascimento")

        genero = self.cleaned_data.get("genero")

        ad = self.cleaned_data.get("ad")

        celular = self.cleaned_data.get("celular")

        if not nome:
            errors["nome"] = "Campo nome obrigatório"

        if nome:

            if len(nome) < 5 or len(nome) > 60:
                errors["nome"] = (
                    "Certifique-se de que o valor tenha entre 5 a 60 caracteres"
                )

            elif not self.is_alpha_pattern(nome):
                errors["nome"] = (
                    "Certifique-se de que o valor tenha apenas caracteres texto"
                )

        if not data_de_nascimento:
            errors["data_de_nascimento"] = "Campo data de nascimento obrigatório"

        if data_de_nascimento:

            ano = int(datetime.now().year - (data_de_nascimento.year))

            if ano == -1 or ano > 100:
                errors["data_de_nascimento"] = "Informe uma data de nascimento válida"

        if not genero:
            errors["genero"] = "Campo gênero obrigatório"

        if not ad:
            errors["cartao_sus"] = "Campo cartão SUS obrigatório"

        if ad:

            if len(ad) != 15:
                errors["cartao_sus"] = (
                    "Campo cartão SUS deve possuir um tamanho de 15 dígitos"
                )

            elif not self.is_numeric_pattern(ad):
                errors["cartao_sus"] = (
                    "Formato de campo inválido para cartão SUS, informe apenas números"
                )
            else:

                if estudante_id:

                    if (
                        Estudante.objects.filter(ad=ad)
                        .exclude(id=estudante_id)
                        .exists()
                    ):
                        errors["ad"] = "Já existe um mesmo AD cadastrado"
                elif Estudante.objects.filter(ad=ad).exists():
                    errors["ad"] = "Já existe um mesmo AD cadastrado"

        if not celular:
            errors["celular"] = "Campo celular obrigatório"

        if celular:

            celular = self.remove_characters(celular)

            if len(celular) != 13 or not self.is_phone_pattern(celular):
                errors["celular"] = (
                    "Certifique-se de que o número de celular esteja correto"
                )

            else:
                self.cleaned_data["celular"] = celular

        if errors:

            for key in errors.keys():
                self.fields[key].label_suffix = ": *"

            raise forms.ValidationError(errors)

        return self.cleaned_data
