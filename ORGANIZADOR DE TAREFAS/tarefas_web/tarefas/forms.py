from django import forms
from .models import Tarefa

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome', 'prioridade', 'prazo', 'categoria']
        widgets = {
            'prazo': forms.DateInput(attrs={'type': 'date'}),
            'prioridade': forms.Select(),
        }
