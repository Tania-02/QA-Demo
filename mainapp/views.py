from django.shortcuts import render, redirect


def index(request):
    return redirect('login')


def login(request):
    return render(request, 'mainapp/login.html')


def logout(request):
    pass


def question(request, question_id):
    pass


def leaderboard(request):
    pass
