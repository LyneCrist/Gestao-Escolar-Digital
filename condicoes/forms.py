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
        
        if errors:

            for key in errors.keys():
                self.fields[key].label_suffix = ": *"

            raise forms.ValidationError(errors)

        return self.cleaned_data
