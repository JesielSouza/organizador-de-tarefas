from django.shortcuts import render
from .models import Tarefa
from django.contrib.auth.decorators import login_required
from .forms import TarefaForm
from django.shortcuts import redirect
# Create your views here.

@login_required
def lista_tarefas(request):
    tarefas = Tarefa.objects.filter(dono=request.user).order_by("prioridade", "prazo")
    return render(request, 'tarefas/lista.html', {'tarefas': tarefas})


@login_required
def nova_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.dono = request.user
            tarefa.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm()

    return render(request, 'tarefas/nova.html', {'form': form})
