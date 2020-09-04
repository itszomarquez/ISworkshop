from django.shortcuts import render
from .models import ProfilePage

def index(request):
  posts = ProfilePage.objects.all()
  return render(request, 'ISworkshop/profile.html', {'posts': posts})

from .forms import ProfilePageForm

def register(request):
  if request.method == 'POST':
    form = ProfilePageForm(request.POST)
    if form.is_valid():
      context = {'form': form}
      return render(request, 'ISworkshop/profile.html', context=context)
  else:
      form = ProfilePageForm()

  context = {'form': form}
  return render(request, 'ISworkshop/register.html', context=context)
