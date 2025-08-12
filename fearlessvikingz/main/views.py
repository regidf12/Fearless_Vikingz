from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def roadmap(request):
    return render(request, 'main/roadmap.html')


def team(request):
    return render(request, 'main/team.html')


def faq(request):
    return render(request, 'main/faq.html')
