from django.shortcuts import render


def Home(request):
    return render(
        request, "Home.html", {}
    )

def sorry(request):
    return render(request, 'sorry.html', context={})
