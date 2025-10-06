from django.shortcuts import render, redirect
from .forms import ContactMessageForm

def home(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home.html', {
                'form': ContactMessageForm(),
                'success': True
            })
    else:
        form = ContactMessageForm()

    return render(request, 'home.html', {'form': form})
