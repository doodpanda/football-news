from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406351711',
        'name': 'Vincentius Filbert Amadeo',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)