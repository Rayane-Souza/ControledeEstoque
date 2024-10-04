from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from produtos.models import Produto

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['name', 'pages']

def produto_list(request, template_name='produtos/produto_list.html'):
    produto = Produto.objects.all()
    data = {}
    data['object_list'] = produto
    return render(request, template_name, data)

def produto_view(request, pk, template_name='produtos/produto_detail.html'):
    produto= get_object_or_404(Produto, pk=pk)    
    return render(request, template_name, {'object':produto})

def produto_create(request, template_name='produtos/produto_form.html'):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('produto_list')
    return render(request, template_name, {'form':form})

def produto_update(request, pk, template_name='produtos/produto_form.html'):
    produto= get_object_or_404(Produto, pk=pk)
    form = ProdutoForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('produto_list')
    return render(request, template_name, {'form':form})

def produto_delete(request, pk, template_name='produtos/produto_confirm_delete.html'):
    produto= get_object_or_404(Produto, pk=pk)    
    if request.method=='POST':
        produt.delete()
        return redirect('produto_list')
    return render(request, template_name, {'object':produto})
