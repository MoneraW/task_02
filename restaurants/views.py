from django.shortcuts import render

# Create your views here.
def home(request):
    context = { 
        'msg': 'Hello World!',
    }
    return render(request, 'restaurants/task_2_test.html', context)