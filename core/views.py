from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "htmx_widgets/dropdown_select.html")


def about(request):
    pass
