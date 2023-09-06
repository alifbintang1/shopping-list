from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Alif Bintang',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)