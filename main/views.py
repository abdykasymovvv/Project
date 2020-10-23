from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Hello', 'My', 'Friends'],
        'obj': {
            'Abdykasymov': 'Mersedes',
            'Erlan': 18,
            'it-119': 'Football'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')



def list(request):
    return render(request, 'main/list.html')



