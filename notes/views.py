
from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, Tag
from .forms import NoteForm
# Create your views here.
def note_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})

def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            # Парсинг строки тегов и добавление их в note
            tag_names = form.cleaned_data['tags'].split(',')
            for name in tag_names:
                tag, created = Tag.objects.get_or_create(name=name.strip())
                note.tags.add(tag)
            return redirect('notes:note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})

def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            updated_note = form.save(commit=False)
            updated_note.save()
            updated_note.tags.clear()

            tag_names = form.cleaned_data['tags'].split(',')
            for name in tag_names:
                
                name = name.strip()
                if name:
                    tag, created = Tag.objects.get_or_create(name=name)
                    updated_note.tags.add(tag)
    
            return redirect('notes:note_list')
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/note_form.html', {'form': form, 'note': note})


def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('notes:note_list')
    return render(request, 'notes/note_confirm_delete.html', {'object': note})