from django.shortcuts import render

def contact_view(request):
    contact = "E-mail: saek@trelemorele.pl"
    return render(request, 'contact/contact.html', {"contact": contact})

