from django.shortcuts import render, redirect


def index(request):
    return redirect('login')


def login(request):
    if request.method == 'GET':
        return render(request, 'mainapp/login.html')
    elif request.method == 'POST':
        # fetch username and password
        # if   user exits, then login user and redirect to /question/1
        # else redirect to /login/ with error message
        ...


def logout(request):
    pass


def question(request, question_id):
    if request.method == 'GET':
        return render(request, 'mainapp/question.html', {
            'q_id': question_id
        })
    elif request.method == 'POST':
        # fetch answer
        # if answer is correct
        #     add submission
        #     redirect to next question
        # else
        #     set message as "wrong answer"
        #     redirect to same question
        ...


def leaderboard(request):
    return render(request, 'mainapp/leaderboard.html')

