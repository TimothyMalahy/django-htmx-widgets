from django.shortcuts import render
from core.models import People
from django.apps import apps

from django.http import HttpRequest as HttpRequestBase
from django.http import HttpResponse
from django_htmx.middleware import HtmxDetails


class HttpRequest(HttpRequestBase):
    htmx: HtmxDetails


# Create your views here.


def filter_model_by_field(app_name, model_name, field_name, search_value):
    model = apps.get_model(app_name, model_name)
    filter_kwargs = {f"{field_name}__icontains": search_value}
    return model.objects.filter(**filter_kwargs)


# def multi_select(request, search, model, *args, **kwargs):
#     print(*args, **kwargs)
#     if search = "":
#         items = model.objects.all()
#     else:
#         items = model.objects.filter(first_name__icontains=search)
#     context = {}
#     context["items"] = People.objects.all()


def search(request):
    context = {}
    first_name = request.GET.get("first_name")
    items = filter_model_by_field("core", "People", "first_name", first_name)

    context["items"] = items
    return render(request, "htmx_widgets/search.html", context=context)


def add_item(request):
    # print(request.POST.get("item_id"))
    id = request.POST.get("item_id")
    person = People.objects.get(id=id)
    context = {}
    context["pill_content"] = person.first_name
    return render(request, "htmx_widgets/pill.html", context=context)

    return HttpResponse(f"{person.first_name} {person.last_name} {person.age}")
