from django.shortcuts import render
# Create your views here.


def hello_1(request):
    return render(request, 'Hello_1.html', {'text': 'Привет 1'})


def hello_2(request):
    text_1 = 'Привет 2'
    text_2 = 'Привет 3'
    context = {'text_1': text_1,
               'text_2': text_2}
    return render(request, 'Hello_2.html', context)