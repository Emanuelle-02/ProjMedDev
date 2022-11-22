from django.shortcuts import render, redirect
from .models import Farmacia, Entregador, Entregas
from .forms import *

# Create your views here.
def entregadorList(request):  
    entregadores = Entregador.objects.all()  
    return render(request,"entregador-list.html",{'entregadores':entregadores})  

def entregadorCreate(request):  
    if request.method == "POST":  
        form = EntregadorForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('entregador-list')  
            except:  
                pass  
    else:  
        form = EntregadorForm()  
    return render(request,'entregador-create.html',{'form':form})  

def entregadorUpdate(request, id):  
    entregador = Entregador.objects.get(id=id)
    form = EntregadorForm(initial={'nome': entregador.nome, 'email': entregador.email, 'cpf': entregador.cpf, 'telefone': entregador.telefone})
    if request.method == "POST":  
        form = EntregadorForm(request.POST, instance=entregador)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/entregador-list')  
            except Exception as e: 
                pass    
    return render(request,'entregador-update.html',{'form':form})  

def entregadorDelete(request, id):
    entregador = Entregador.objects.get(id=id)
    try:
        entregador.delete()
    except:
        pass
    return redirect('entregador-list')

def farmaciaList(request):  
    farmacias = Farmacia.objects.all()  
    return render(request,"farmacia-list.html",{'farmacias':farmacias}) 

def farmaciaCreate(request):  
    if request.method == "POST":  
        form = FarmaciaForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('farmacia-list')  
            except:  
                pass  
    else:  
        form = FarmaciaForm()  
    return render(request,'farmacia-create.html',{'form':form})  

def farmaciaUpdate(request, id):  
    farmacia = Farmacia.objects.get(id=id)
    form = FarmaciaForm(initial={'nome': farmacia.nome, 'email': farmacia.email, 'cnpj': farmacia.cnpj, 'telefone': farmacia.telefone, 'rua': farmacia.rua, 'numero': farmacia.numero, 'bairro': farmacia.bairro, 'cidade': farmacia.cidade})
    if request.method == "POST":  
        form = FarmaciaForm(request.POST, instance=farmacia)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/farmacia-list')  
            except Exception as e: 
                pass    
    return render(request,'farmacia-update.html',{'form':form})  

def farmaciaDelete(request, id):
    farmacia = Farmacia.objects.get(id=id)
    try:
        farmacia.delete()
    except:
        pass
    return redirect('farmacia-list')
    
def entregaList(request):  
    entregas = Entregas.objects.all()  
    return render(request,"entrega-list.html",{'entregas':entregas}) 

def entregaCreate(request):  
    if request.method == "POST":  
        form = EntregaForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('entrega-list')  
            except:  
                pass  
    else:  
        form = EntregaForm()  
    return render(request,'entrega-create.html',{'form':form})  

def entregaUpdate(request, id):  
    entrega = Entregas.objects.get(id=id)
    form = EntregaForm(initial={'medicamento': entrega.medicamento, 'Farmacia': entrega.Farmacia, 'entregador': entrega.entregador, 'destinatario': entrega.destinatario, 'rua': entrega.rua, 'numero': entrega.numero, 'bairro': entrega.bairro, 'cidade': entrega.cidade, 'status': entrega.status})
    if request.method == "POST":  
        form = EntregaForm(request.POST, instance=entrega)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/entrega-list')  
            except Exception as e: 
                pass    
    return render(request,'entrega-update.html',{'form':form})  

def entregaDelete(request, id):
    entrega = Entregas.objects.get(id=id)
    try:
        entrega.delete()
    except:
        pass
    return redirect('entrega-list')