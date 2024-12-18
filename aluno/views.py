from django.shortcuts import render,get_object_or_404,redirect
from .forms import AlunoForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.core.paginator import Paginator

def aluno_editar(request,id):
    aluno = get_object_or_404(Aluno,id=id)
   
    if request.method == 'POST':
        form = AlunoForm(request.POST,instance=aluno)

        if form.is_valid():
            form.save()
            return redirect('aluno_listar')
    else:
        form = AlunoForm(instance=aluno)

    return render(request,'aluno/form.html',{'form':form})


def aluno_remover(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    aluno.delete()
    return redirect('aluno_listar') # procure um url com o nome 'lista_aluno'


def aluno_criar(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            form = AlunoForm()
    else:
        form = AlunoForm()

    return render(request, "aluno/form.html", {'form': form})
# views.py


def aluno_listar(request):
    alunos = Aluno.objects.all()

    # Configura a paginação usando get_page()
    paginator = Paginator(alunos, 10)  # Mostra 10 alunos por página
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)  # Evita exceções ao lidar com páginas inválidas

    context = {
        'page_obj': page_obj,  # Passa 'page_obj' para o template
    }

    return render(request, "aluno/alunos.html", context)




def index(request):
    total_alunos = Aluno.objects.count()
    context = {
        'total_alunos' : total_alunos,
    }
    return render(request, "aluno/index.html",context)



def matricula_editar(request,id):
    matricula = get_object_or_404(Matricula,id=id)
   
    if request.method == 'POST':
        form = MatriculaForm(request.POST,instance=matricula)

        if form.is_valid():
            form.save()
            return redirect('matricula_listar')
    else:
        form = MatriculaForm(instance=matricula)

    return render(request,'aluno/form_matricula.html',{'form':form})


def matricula_remover(request, id):
    matricula = get_object_or_404(Matricula, id=id)
    matricula.delete()
    return redirect('matricula_listar') # procure um url com o nome 'lista_aluno'


def matricula_criar(request):
    if request.method == 'POST':
        form = MatriculaForm(request.POST)
        if form.is_valid():
            form.save()
            form = MatriculaForm()
    else:
        form = MatriculaForm()

    return render(request, "aluno/form_matricula.html", {'form': form})
# views.py


def matricula_listar(request):
    matriculas = Matricula.objects.all()

    # Configura a paginação usando get_page()
    paginator = Paginator(matriculas, 5)  # Mostra 10 alunos por página
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)  # Evita exceções ao lidar com páginas inválidas

    context = {
        'page_obj': page_obj,  # Passa 'page_obj' para o template
    }

    return render(request, "aluno/matricula.html", context)