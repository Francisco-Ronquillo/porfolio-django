from django.shortcuts import redirect, render
from .models import Project,Experience,Referencias_laborales
from django.contrib.auth.decorators import login_required
from .forms import Referencias

@login_required
def home(request):
    projects=Project.objects.all()
    experiences=Experience.objects.all()
    testimonios=Referencias_laborales.objects.all()
    return render(request, "home.html", {"projects": projects ,"experience":experiences,"testimonio":testimonios})


def referencia_create(request):
    data = {"title": "Referencias laborales", "title1": "Añadir referencias"}
    if request.method == "POST":
        form = Referencias(request.POST)
        if form.is_valid():
            form.save()
            return redirect("porfolio:home")
        else:
            data["form"] = form
            data["error"] = "Error al crear referencia."
            return render(request, "referencias/form.html", data)
    else:
        form = Referencias()
        data["form"] = form
    print(form)
    return render(request, "referencias/form.html", data)


def referencia_delete(request, id):
    referencia= Referencias_laborales.objects.get(id=id)
    data = {"title": "Eliminar", "title1": "Eliminar Referencias", "referencia": referencia}
    if request.method == "POST":
        referencia.delete()
        return redirect("porfolio:home")
    return render(request, "referencias/delete.html", data)


def referencia_update(request, id):
    data = {"title": "Referencias", "title1": "Editar Referencia"}
    referencia= Referencias_laborales.objects.get(pk=id)  # doctor1
    if request.method == "POST":
        form = Referencias(request.POST, instance=referencia)
        if form.is_valid():
            form.save()
            return redirect("porfolio:home")
        else:
            data["form"] = form
            data["error"] = "Error al editar referencia."
            return render(request, "referencias/form.html", data)
    else:
        form = Referencias(instance=referencia)
        data["form"] = form
    print(form)
    return render(request, "referencias/form.html", data)
