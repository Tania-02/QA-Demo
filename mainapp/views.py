from collections import namedtuple
from django.shortcuts import render, redirect
from .models import User, Submission, Question
from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import get_object_or_404


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
    user_id = request.session.get('user_id')
    if user_id is not None:
        question_ = get_object_or_404(Question, id=question_id)
        user_ = get_object_or_404(User,id=user_id)

        if request.method == 'GET':
            return render(request, 'mainapp/question.html', {
                'question': question_
            })
        elif request.method == 'POST':
            # fetch answer
            answer_obtained = request.POST.get('answer')

            if answer_obtained is not None:
                if question_.answer == answer_obtained:
                    total_questions = Question.objects.count()
                    submission = Submission()
                    submission.question = question_
                    submission.user = user_
                    submission.save()

                    return redirect('question', question_id=(question_id % total_questions) + 1)

                else:
                    messages.error(request, 'WRONG ANSWER!')
                    return redirect('question', question_id=question_id)
            else:
                messages.warning(request, 'Please submit an answer!!')
                return redirect('question', question_id=question_id)
    else:
        # TODO: add error message 'User must log in!'
        return redirect('login')


def leaderboard(request):
    user_objects = User.objects.all()
    data = []

    for user_object in user_objects:
        user_points = Submission.objects \
            .filter(user=user_object) \
            .aggregate(Sum('question__point'))['question__point__sum']
        if user_points is None:
            user_points = 0

        data.append((user_object.name, user_points))

    data.sort(key=lambda t: t[1], reverse=True)

    return render(request, 'mainapp/leaderboard.html', {
        'data': data
    })

# USING NAMEDTUPLE
# def leaderboard(request):
#     user_objects = User.objects.all()
#     LeaderboardData = namedtuple('LeaderboardData', ['name', 'points'])
#     data = []
#
#     for user_object in user_objects:
#         user_points = Submission.objects \
#             .filter(user=user_object) \
#             .aggregate(Sum('question__point'))['question__point__sum']
#         if user_points is None:
#             user_points = 0
#
#         data.append(LeaderboardData(name=user_object.name, points=user_points))
#
#     data.sort(key=lambda lbd: lbd.points, reverse=True)
#
#     return render(request, 'mainapp/leaderboard.html', {
#         'data': data
#     })
