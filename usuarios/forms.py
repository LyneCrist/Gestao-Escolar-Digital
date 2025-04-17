from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    tipo_usuario = forms.ChoiceField(
        choices=[('pais', 'Pais'), ('professor', 'Professor')],
        widget=forms.RadioSelect(attrs={'class': 'radio-group'}),
        required=True
    )

    terms_accepted = forms.BooleanField(
        required=True,
        label="Aceito os termos e condições",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'tipo_usuario', 'terms_accepted')
  