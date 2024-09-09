from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app' : 'Leather Store',
        'name': 'William Matthew Saputra',
        'class': 'PBP F',
        
    }

    return render(request, "main.html", context)