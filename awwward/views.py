from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

projects = [
    {
        'author': 'BwanaQ',
        'title': 'Dummy Content',
        'image': 'Blog Post 1',
        'description': 'First post content',
        'url': 'August 27, 2020',
        'timestamp': 'August 27, 2020'
    },
    {
        'author': 'Sally Koki',
        'title': 'Dummy Content',
        'image': 'Blog Post 2',
        'description': 'Second post content',
        'url': 'November 27, 2021',
        'timestamp': 'August 27, 2020'

    },
    {
        'author': 'Loise Hunja',
        'title': 'Dummy Content',
        'image': 'Blog Post 3',
        'description': 'Third post content',
        'url': 'March 2, 2021'
        'timestamp': 'August 27, 2020'
    }
]


def home(request):
    context = {
        'projects': projects
    }
    return render(request, 'awwward/home.html', context)
