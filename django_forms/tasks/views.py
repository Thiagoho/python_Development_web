from django.shortcuts import render

from django.http import HttpResponse

from .forms import ContactForm

# Segundo Passo.
# antes tivemos que adicionar uma pasta >> Templates >> form.html
def contact(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        print(name, email)
        
    form = ContactForm()
    
    return render(request, 'form.html', {'form': form})
