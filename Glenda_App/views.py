from django.shortcuts import render,redirect

from Glenda_App.forms import MenuForm, SubMenuForm
from Glenda_App.models import Menu


# Create your views here.

def index(request):
    menus = Menu.objects.prefetch_related('submenus').all()
    return render(request, 'index.html', {'menus': menus})
def calendar(request):
    menus = Menu.objects.prefetch_related('submenus').all()
    return render(request, 'calendar.html', {'menus': menus})

def create_menu(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Change to redirect to index after creation
    else:
        form = MenuForm()
    return render(request, 'create_menu.html', {'form': form})

def create_submenu(request):
    if request.method == 'POST':
        form = SubMenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Change to redirect to index after creation
    else:
        form = SubMenuForm()
    return render(request, 'create_submenu.html', {'form': form})