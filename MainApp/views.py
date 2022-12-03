from django.shortcuts import render
from django.http import Http404
from read_from_file import countries
# from countries_dict import countries
import string
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    return render(request, 'index.html')

def countries_list(request, page):
    alphabet = list(string.ascii_uppercase)

    pagination = Paginator(countries, 10)
    countries_on_the_page = pagination.get_page(page)
    p_range = pagination.page_range
    pg = pagination.page(page)
    count = pagination.num_pages
    c2 = count - 2
    c3 = count - 3
    start = pg.start_index()

    context = {
        "countries": countries,
        "alphabet": alphabet,
        "countries_on_the_page": countries_on_the_page,
        'pg': pg,
        "p_range": p_range,
        "count": count,
        "c2": c2,
        "c3": c3,
        "start": start,
    }

    return render(request, 'countries-list.html', context)

def country_page(request, name):
    for this_country in countries:
        # context = {}
        if this_country['country'] == name:
            context = {
                "this_country": this_country
            }
    return render(request, 'country_page.html', context)
    # raise Http404(f"Страна {name} не найдена")

def countries_started_from(request, letter):
    countries_by_letter = []
    for this_country in countries:
        if list(this_country['country'])[0] == letter:
            countries_by_letter.append(this_country)
            context = {
                'countries_by_letter': countries_by_letter,
                'letter': letter
            }
    return render(request, 'countries-by-letter.html', context)

def languages(request):
    all_languages = set()
    for this_country in countries:
        country_langs = this_country['languages']
        for lang in country_langs:
            all_languages.add(lang)
    context = {
        'all_languages': all_languages
    }
    return render(request, 'languages.html', context)

def language(request, lang):
    countries_by_language = []
    for this_country in countries:
        country_langs = this_country['languages']
        for this_lang in country_langs:
            if this_lang == lang:
                countries_by_language.append(this_country)
    context = {
        'lang': lang,
        'countries_by_language': countries_by_language
    }
    return render(request, 'language.html', context)
