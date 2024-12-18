from django.forms import ModelForm
from django import forms
from .models import Aluno,Curso,Cidade,Matricula

class AlunoForm(ModelForm):

    class Meta:
        model = Aluno
        fields = '__all__'
        widgets = {
            'nome_aluno' : forms.TextInput(attrs={'class': 'form-control' }),
            'endereco' : forms.TextInput(attrs={'class': 'form-control' }),
            'email' : forms.EmailInput(attrs={'class': 'form-control' }),
            'cidade': forms.Select(attrs={'class': 'form-control' }),
        }


class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ['aluno', 'curso', 'data_matricula', 'data_conclusao', 'nota_final']
        widgets = {
            'aluno': forms.Select(attrs={'class': 'form-control'}),
            'data_matricula': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'nota_final': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.01}),
        }