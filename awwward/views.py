from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.utils.timezone import utc


projects = [
    {
        'creator': 'BwanaQ',
        'title': 'Dummy Content',
        'image': 'Blog Post 1',
        'description': 'First post content',
        'link': 'August 27, 2020',
        'timestamp': 'August 27, 2020'
    },
    {
        'creator': 'Sally Koki',
        'title': 'Dummy Content',
        'image': 'Blog Post 2',
        'description': 'Second post content',
        'link': 'November 27, 2021',
        'timestamp': 'August 27, 2020'

    },
    {
        'creator': 'Loise Hunja',
        'title': 'Dummy Content',
        'image': 'Blog Post 3',
        'description': 'Third post content',
        'link': 'March 2, 2021',
        'timestamp': 'August 27, 2020'
    }
]


def home(request):
    # Create your views here.
    now = datetime.datetime.utcnow().replace(tzinfo=utc)

    context = {
        'projects': projects,
        'now': now
    }
    return render(request, 'awwward/home.html', context)
