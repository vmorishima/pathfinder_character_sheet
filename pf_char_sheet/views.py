from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Character

# Create your views here.
# def index(request):
#     char_list = Character.objects.order_by('name')
#     context = {'char_list': char_list}
#     return render(request, 'pf_char_sheet/index.html', context)

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'char_list'

    def get_queryset(self):
        return Character.objects.order_by('name')

# def new_page(request):
#     return render(request, 'pf_char_sheet/new.html')

class characterCreate(CreateView):
    template_name = 'new.html'
    model = Character
    fields = ['name', 'level', 'character_class', 'alignment', 'gender', 'race', 'size',
              'STR','DEX','CON','INT','WIS','CHA',
              'HP','FORT','WILL','REFLEX','BAB']

class characterUpdate(UpdateView):
    model = Character
    fields = ['name', 'level', 'character_class', 'alignment', 'gender', 'race', 'size',
              'STR','DEX','CON','INT','WIS','CHA',
              'HP','FORT','WILL','REFLEX','BAB']
    template_name = 'character_update.html'

class characterDelete(DeleteView):
    model = Character
    success_url = reverse_lazy('index')
    template_name = 'character_delete.html'

def char_page(request, character_id):
    char = get_object_or_404(Character, pk=character_id)
    return render(request, 'char_page.html', {'char': char})

def save(request):
    new_char = Character.objects.create()
    try:
        new_char.name = request.POST['name']
        new_char.level = request.POST['level']
        new_char.character_class = request.POST['class']
        new_char.alignment = request.POST['alignment']
        new_char.gender = request.POST['gender']
        new_char.race = request.POST['race']
    except (KeyError):
        return render(request, 'new.html', {'error_message': 'Error'})
    else:
        new_char.save()
        return HttpResponseRedirect(reverse('char', args=(new_char.id,)))

