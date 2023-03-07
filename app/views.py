from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Page


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


@login_required
def app_page(request):
    pages = Page.objects.raw("SELECT id, name FROM app_page")
    data = {"pages": []}
    for page in pages:
        data["pages"].append({"name": page.name, "id": page.id})
    return render(request, "base_template.html", context=data)


@login_required
def display_graph(request, graph_type="histogram"):
    pages = Page.objects.raw("SELECT id, name FROM app_page")
    data = {"pages": []}
    for page in pages:
        data["pages"].append({"name": page.name, "id": page.id})

    if graph_type == 'histogram':
        return render(request, "histogram.html", context=data)
    if graph_type == 'graph':
        return render(request, "graph.html", context=data)
    if graph_type == 'circle-chart':
        return render(request, "circle_chart.html", context=data)

    return HttpResponseNotFound("Not Found")
