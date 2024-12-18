from django.shortcuts import render
from core.models import People

from django.http import HttpRequest as HttpRequestBase
from django.http import HttpResponse
from django_htmx.middleware import HtmxDetails


class HttpRequest(HttpRequestBase):
    htmx: HtmxDetails


# Create your views here.


def search(request):
    context = {}
    first_name = request.GET.get("first_name")

    context["items"] = People.objects.filter(first_name__icontains=first_name)
    return render(request, "htmx_widgets/search.html", context=context)


def add_item(request):
    # print(request.POST.get("item_id"))
    id = request.POST.get("item_id")
    person = People.objects.get(id=id)
    context = {}
    context["button_content"] = person.first_name
    return render(request, "htmx_widgets/button.html", context=context)

    return HttpResponse(f"{person.first_name} {person.last_name} {person.age}")
