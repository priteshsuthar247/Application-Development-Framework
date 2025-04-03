from django.shortcuts import render, redirect, get_object_or_404
from .models import Note

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'myapp/note_list.html', {'notes': notes})

def add_note(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        Note.objects.create(title=title, content=content)
        return redirect('note_list')
    return render(request, 'myapp/add_note.html')

def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == "POST":
        note.title = request.POST['title']
        note.content = request.POST['content']
        note.save()
        return redirect('note_list')
    return render(request, 'myapp/edit_note.html', {'note': note})

def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect('note_list')
