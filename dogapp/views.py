from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponseRedirect

from .forms import UserAnswerForm
from .models import Choice, UserAnswer

app_name = 'dogapp'

class IndexView(TemplateView):
    template_name = 'index.html'

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

# データベースからリストを取得
# list_a = [1, 3, 2, 3, 1, 2]
# dog_choices_from_db = Choice.objects.all()

# most_similar_id = find_most_similar_id_with_order(list_a, dog_choices_from_db)
# if most_similar_id is not None:
#     print("リストAと最も一致率が高いデータベース内のID（順序考慮）:", most_similar_id)
# else:
#     print("一致するデータベース内のIDが見つかりませんでした。")

def question1(request):
    if request.method == 'POST':
        answer1 = request.POST.get('answer')
        request.session['answer1'] = answer1
        return render(request, 'question2.html')
    return render(request, 'question1.html')

def question2(request):
    if request.method == 'POST':
        answer2 = request.POST.get('answer')
        request.session['answer2'] = answer2
        return render(request, 'question3.html')
    return render(request, 'question2.html')

def question3(request):
    if request.method == 'POST':
        answer3 = request.POST.get('answer')
        request.session['answer3'] = answer3
        return render(request, 'question4.html')
    return render(request, 'question3.html')

def question4(request):
    if request.method == 'POST':
        answer4 = request.POST.get('answer')
        request.session['answer4'] = answer4
        return render(request, 'question5.html')
    return render(request, 'question5.html')

def question5(request):
    if request.method == 'POST':
        answer5 = request.POST.get('answer')
        request.session['answer5'] = answer5
        return render(request, 'question6.html')
    return render(request, 'question5.html')

def question6(request):
    if request.method == 'POST':
        answer6 = request.POST.get('answer')
        request.session['answer6'] = answer6
        return redirect('create_answer')
    return render(request, 'question6.html')

@method_decorator(login_required, name='dispatch')
class CreateAnswerView(CreateView):
    form_class = UserAnswerForm
    template_name = 'choiceform.html'


    def form_valid(self, form):
        answer_1 = self.request.session.get('answer1')
        answer_2 = self.request.session.get('answer2')
        answer_3 = self.request.session.get('answer3')
        answer_4 = self.request.session.get('answer4')
        answer_5 = self.request.session.get('answer5')
        answer_6 = self.request.session.get('answer6')

        form_answer_1 = form.cleaned_data['answer_1']
        form_answer_2 = form.cleaned_data['answer_2']
        form_answer_3 = form.cleaned_data['answer_3']
        form_answer_4 = form.cleaned_data['answer_4']
        form_answer_5 = form.cleaned_data['answer_5']
        form_answer_6 = form.cleaned_data['answer_6']

        # データベースからDogChoiceオブジェクトを取得
        dog_choices_from_db = Choice.objects.all()

        # 類似性を計算して最も類似したIDを見つける
        # most_similar_id = find_most_similar_id_with_order(list_a, dog_choices_from_db)
        most_similar_id = find_most_similar_id_with_order(
            [answer_1, answer_2, answer_3, answer_4, answer_5, answer_6],
            dog_choices_from_db
        )

        if most_similar_id is not None:
            print("フォームデータと最も一致率が高いデータベース内のID（順序考慮）:", most_similar_id)

            self.most_similar_id = most_similar_id

            # リダイレクト先のURLを指定
            success_url = reverse('dogapp:dog_detail', kwargs={'dog_id': most_similar_id})

            # リダイレクトを行う
            return HttpResponseRedirect(success_url)

        else:
            print("一致するデータベース内のIDが見つかりませんでした。")

        # 回答データを保存
        # postdata = form.save(commit=False)
        # postdata.user = self.request.user
        # postdata.save()

        user_answer = UserAnswer(
            answer_1=answer_1,
            answer_2=answer_2,
            answer_3=answer_3,
            answer_4=answer_4,
            answer_5=answer_5,
            answer_6=answer_6,
            user=self.request.user
        )

        return super().form_valid(form)


from django.shortcuts import render, get_object_or_404
from .models import Dogs

def dog_detail(request, dog_id):
    # 指定されたIDに対応するDogsモデルのインスタンスを取得
    dog = get_object_or_404(Dogs, pk=dog_id)
    return render(request, 'dog_detail.html', {'dog': dog})