from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


@login_required
def app_page(request, graph_type="histogram"):
    data = {"pages": [
        {"name": "Note", "id": "1"},
        {"name": "News", "id": "2"},
        {"name": "Main", "id": "3"}]}

    if graph_type == 'histogram':
        return render(request, "histogram.html", context=data)
    if graph_type == 'graph':
        return render(request, "graph.html", context=data)
    if graph_type == 'circle-chart':
        return render(request, "circle_chart.html", context=data)

    return HttpResponseNotFound("Not Found")
