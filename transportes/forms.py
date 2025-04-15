from django import forms
from common.util import CommonsUtil
from .choices import MOTIVO_CHOICES
from .models import Transporte
from datetime import datetime, time


class TransporteForm(forms.ModelForm, CommonsUtil):

    data_de_transporte = forms.DateField(
        label="Data de Transporte",
        required=False,
        input_formats=["%Y-%m-%d"],
        widget=forms.DateInput(
            format="%Y-%m-%d",
            attrs={
                "type": "date",
                "name": "dataTransporte",
                "id": "dataTransporte",
                "autocomplete": "off",
            },
        ),
    )

    horario_de_atendimento = forms.TimeField(
        label="Horário de Atendimento",
        required=False,
        widget=forms.TimeInput(
            attrs={
                "type": "time",
                "name": "horarioAtendimento",
                "id": "horarioAtendimento",
                "min": "09:00",
                "max": "16:00",
            },
        ),
    )

    motivo_de_transporte = forms.ChoiceField(
        label="Motivo de Transporte",
        required=False,
        widget=forms.Select,
        choices=MOTIVO_CHOICES,
    )

    descricao_motivo = forms.CharField(
        label="Descrição motivo",
        required=False,
        widget=forms.Textarea(
            attrs={
                "maxlength": "160",
            },
        ),
    )

    rua = forms.CharField(
        required=False,
    )

    bairro = forms.CharField(
        required=False,
    )

    numero = forms.CharField(
        label="Número",
        required=False,
        max_length=7,
    )

    cidade = forms.CharField(
        required=False,
    )

    destino = forms.CharField(
        required=False,
    )

    observacao = forms.CharField(
        label="Observação",
        required=False,
        widget=forms.Textarea(
            attrs={
                "maxlength": "160",
            },
        ),
    )

    class Meta:

        model = Transporte

        fields = "__all__"

        exclude = ["paciente", "status", "data_criacao", "data_alteracao"]

    def clean(self):

        super().clean()

        errors = {}

        # paciente_id = self.instance.pk

        data_de_transporte = self.cleaned_data.get("data_de_transporte")

        horario_de_atendimento = self.cleaned_data.get("horario_de_atendimento")

        motivo_de_transporte = self.cleaned_data.get("motivo_de_transporte")

        descricao_motivo = self.cleaned_data.get("descricao_motivo")

        rua = self.cleaned_data.get("rua")

        bairro = self.cleaned_data.get("bairro")

        numero = self.cleaned_data.get("numero")

        cidade = self.cleaned_data.get("cidade")

        destino = self.cleaned_data.get("destino")

        observacao = self.cleaned_data.get("observacao")

        if not data_de_transporte:
            errors["data_de_transporte"] = "Campo data de transporte obrigatório"

        if data_de_transporte:

            if data_de_transporte.year != datetime.now().year:
                errors["data_de_transporte"] = "Informe uma data de transporte válida"

        if not horario_de_atendimento:
            errors["horario_de_atendimento"] = "Campo data de atendimento obrigatório"

        if horario_de_atendimento:

            start_time = time(8, 0, 0)

            end_time = time(17, 0, 0)

            if horario_de_atendimento < start_time or horario_de_atendimento > end_time:
                errors["horario_de_atendimento"] = (
                    f"Erro: Hora de atendimento deve respeitar janela das {start_time.hour}hrs às {end_time.hour}hrs"
                )

        if motivo_de_transporte == "0":
            errors["motivo_de_transporte"] = "Selecione motivo para o transporte"

        if not descricao_motivo:
            errors["descricao_motivo"] = "Campo descricao motivo obrigatório"

        if descricao_motivo:

            if len(descricao_motivo) < 10 or len(descricao_motivo) > 160:
                errors["descricao_motivo"] = (
                    "Certifique-se de que o valor tenha entre 10 a 160 caracteres"
                )

        if not rua:
            errors["rua"] = "Campo rua obrigatório"

        if rua:

            if len(rua) < 5 or len(rua) > 60:
                errors["rua"] = (
                    "Certifique-se de que o valor tenha entre 5 a 60 caracteres"
                )

            elif not self.is_alpha_numeric_character_pattern(rua):
                errors["rua"] = (
                    "Certifique-se de que o valor tenha apenas caracteres texto"
                )

        if not bairro:
            errors["bairro"] = "Campo bairro obrigatório"

        if not numero:
            errors["numero"] = "Campo número obrigatório"

        if numero:

            if len(numero) > 7:
                errors["numero"] = "Campo número permite no máximo 7 caracteres"

            elif not self.find_numbers(numero):
                errors["numero"] = "Certifique-se de que valor informado tenha números"

            elif not self.is_alpha_numeric_character_pattern(numero):
                errors["numero"] = (
                    "Certifique-se de que valor informado seja um número de endereço válido"
                )

        if not cidade:
            errors["cidade"] = "Campo cidade obrigatório"

        if not destino:
            errors["destino"] = "Campo destino obrigatório"

        if not observacao:
            errors["observacao"] = "Campo observação obrigatório"

        if observacao:

            if len(observacao) < 10 or len(observacao) > 160:
                errors["observacao"] = (
                    "Certifique-se de que o valor tenha entre 10 a 160 caracteres"
                )

        if errors:

            for key in errors.keys():
                self.fields[key].label_suffix = ": *"

            raise forms.ValidationError(errors)

        return self.cleaned_data
