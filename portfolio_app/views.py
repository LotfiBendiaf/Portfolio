from django.shortcuts import render, redirect
from .forms import MessageForm
from django.views.generic import TemplateView
from django.http import FileResponse
import os

# Create your views here.


def HomeView(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            print('Saved')
            form.save()
            form = MessageForm()
        else:
            print('Errors: ', form.errors)
    else:
        form = MessageForm()

    context = {
        'form': form,
    }

    return render(request, 'index.html', context)

def facture(request):
	filepath = os.path.join('static', 'Facture.pdf')
	return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def businessPlan(request):
	filepath = os.path.join('static', 'Business_Plan.pdf')
	return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def resume(request):
	filepath = os.path.join('static', 'Resume_fr.pdf')
	return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

