from django.shortcuts import render, redirect
from .models import User, Submission, Question
from django.contrib import messages



def index(request):
    return redirect('login')


# login not required
def login(request):
    if request.method == 'GET':
        return render(request, 'mainapp/login.html')
    elif request.method == 'POST':
        # fetch username and password
        phone_number = request.POST.get('phone')
        pwd = request.POST.get('password')

        try:
            # if user exits, then login user and redirect to /question/1
            user = User.objects.get(phone=phone_number, password=pwd)
            request.session['user_id'] = user.id
            return redirect('question', question_id=1)
        except User.DoesNotExist:
            # else redirect to /login/ with error message
            messages.error(request, 'Phone number or password doesn\'t match')
            return redirect('login')


# login required
def logout(request):
    del request.session['user_id']
    return redirect('login')


# login required
def question(request, question_id):
    print(request.session.get('user_id'))
    if request.session.get('user_id') is not None:
        if request.method == 'GET':
            return render(request, 'mainapp/question.html', {
                'q_id': question_id
            })
        elif request.method == 'POST':
            # fetch answer
            ...
            # if answer is correct

            #     add submission
            #     redirect to next question
            # else
            #     set message as "wrong answer"
            #     redirect to same question
            ...
    else:
        # TODO: add error message 'User must log in!'
        return redirect('login')


def leaderboard(request):
    user_objects = User.objects.all()
    data = []

    for user_object in user_objects:
        user_points = sum(Submission.objects.values('question__point').filter(user=user_object))
        data.append((user_object.name, user_points))

    return render(request, 'mainapp/leaderboard.html', {
        'data': data
    })
