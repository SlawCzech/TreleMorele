from django.shortcuts import render

def homepage_view(request):
    name = "TreleMorele"
    return render(request, 'homepage/homepage.html', {"name_value": name})

