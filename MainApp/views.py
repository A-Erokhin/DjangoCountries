from django.shortcuts import render
from django.http import Http404
from countries_dict import countries

# Create your views here.
def home(request):
    return render(request, 'index.html')

def countries_list(request):
    context = {
        "countries": countries
    }
    return render(request, 'countries-list.html', context)

def country_page(request, name):
    # FIXME: данная функция реализована не верно. Запустите и проверьте на нескольких странах
    for this_country in countries:
        context = {}
        if this_country['country'] == name:
            context = {
                "this_country": this_country
            }
        return render(request, 'country_page.html', context)
    raise Http404(f"Страна {name} не найдена")