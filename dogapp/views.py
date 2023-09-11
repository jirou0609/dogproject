from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Choice, UserAnswer, Dogs

app_name = 'dogapp'

class IndexView(ListView):
    template_name = 'index.html'
    model = Dogs

def calculate_similarity_with_order(list1, list2):
    total_elements = len(list1)
    matching_elements = sum(1 for x, y in zip(list1, list2) if x == y)
    similarity = matching_elements / total_elements
    return similarity

def find_most_similar_id_with_order(target_list, Choice):
    most_similar_id = None
    max_similarity = 0

    for choice in Choice:
        db_list = [
            choice.question_1,
            choice.question_2,
            choice.question_3,
            choice.question_4,
            choice.question_5,
            choice.question_6
        ]
        similarity = calculate_similarity_with_order(target_list, db_list)

        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_id = choice.id

    return most_similar_id


def create_answer_list_from_session(request):
    list_a = []

    for i in range(1, 7):
        session_key = f'answer{i}'
        if session_key in request.session:
            answer = request.session[session_key]
            print(f"セッションキー: {session_key}, セッション値: {answer}")
            list_a.append(answer)
            print(f"６まで終わったリスト{list_a}")

    return list_a


def question1(request):
    if request.method == 'POST':
        answer1 = request.POST.get('answer')
        request.session['answer1'] = answer1
        list_a = create_answer_list_from_session(request)
        return render(request, 'question2.html')
    return render(request, 'question1.html')


def question2(request):
    if request.method == 'POST':
        answer2 = request.POST.get('answer')
        request.session['answer2'] = answer2
        list_a = create_answer_list_from_session(request)
        return render(request, 'question3.html')
    return render(request, 'question2.html')


def question3(request):
    if request.method == 'POST':
        answer3 = request.POST.get('answer')
        request.session['answer3'] = answer3
        list_a = create_answer_list_from_session(request)
        return render(request, 'question4.html')
    return render(request, 'question3.html')


def question4(request):
    if request.method == 'POST':
        answer4 = request.POST.get('answer')
        request.session['answer4'] = answer4
        list_a = create_answer_list_from_session(request)
        return render(request, 'question5.html')
    return render(request, 'question5.html')


def question5(request):
    if request.method == 'POST':
        answer5 = request.POST.get('answer')
        request.session['answer5'] = answer5
        list_a = create_answer_list_from_session(request)
        return render(request, 'question6.html')
    return render(request, 'question5.html')


def question6(request):
    if request.method == 'POST':
        answer6 = request.POST.get('answer')
        request.session['answer6'] = answer6
        list_a = create_answer_list_from_session(request)
        print(f"さいご終わったリスト{list_a}")
        return redirect('dogapp:create_answer')
    return render(request, 'question6.html')


@login_required
def create_answer(request):
    # if request.method == 'POST':
        list_a = create_answer_list_from_session(request)
        print(f"defのリストは{list_a}")
        list_a = [int(x) for x in list_a]

        dog_choices_from_db = Choice.objects.all()
        most_similar_id = find_most_similar_id_with_order(list_a, dog_choices_from_db)
        if most_similar_id is not None:
            print("セッションデータと最も一致率が高いデータベース内のID（順序考慮）:", most_similar_id)

            user_answer = UserAnswer(
                answer_1=list_a[0],
                answer_2=list_a[1],
                answer_3=list_a[2],
                answer_4=list_a[3],
                answer_5=list_a[4],
                answer_6=list_a[5],
                user=request.user
            )
            user_answer.save()

            # リダイレクト先のURLを指定
            success_url = reverse('dogapp:dog_detail', kwargs={'dog_id': most_similar_id})

            # リダイレクトを行う
            return HttpResponseRedirect(success_url)

        else:
            print("一致するデータベース内のIDが見つかりませんでした。")
            print(f"{most_similar_id}{find_most_similar_id_with_order}")
            return render(request, 'index.html')


def dog_detail(request, dog_id):
    dog = get_object_or_404(Dogs, pk=dog_id)
    return render(request, 'dog_detail.html', {'dog': dog})

class DogsView(ListView):
    template_name = 'dog_list.html'
    model = Dogs
    paginate_by = 9