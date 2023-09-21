from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.utils import timezone

from .models import Choice, UserAnswer, Dogs, Result, Comment
from .forms import CommentForm

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
            print(f"格納されたリスト{list_a}")

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

            result = Result(result=most_similar_id, user=request.user)
            result.save()

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

            success_url = reverse('dogapp:result', kwargs={'dog_id': most_similar_id})

            return HttpResponseRedirect(success_url)

        else:
            print("一致するデータベース内のIDが見つかりませんでした。")
            print(f"{most_similar_id}{find_most_similar_id_with_order}")
            return render(request, 'index.html')


def result(request, dog_id):
    dog = get_object_or_404(Dogs, pk=dog_id)
    return render(request, 'result.html', {'dog': dog})


class DogsView(ListView):
    template_name = 'dog_list.html'
    model = Dogs
    paginate_by = 9


def count_results(request):
    result_counts = Result.objects.values('result').annotate(count=Count('result')).order_by('-count')[:3]

    # カウント結果を表示するためのコードを追加する
    for item in result_counts:
        print(f'整数 {item["result"]} のカウント: {item["count"]}')

    # ビューを返す場合
    return render(request, 'ranking.html', {'result_counts': result_counts})


class DetailView(DetailView):
    template_name = 'dog_detail.html'
    model = Dogs


# ランキングを表示するために上位3件に並び替え&リストに格納して返す
def count_results(request):
    result_counts = Result.objects.values('result').annotate(count=Count('result')).order_by('-count')[:3]

    dog_info_list = []

    for item in result_counts:
        result_value = item['result']
        dog_record = Dogs.objects.filter(id=result_value).first()

        if dog_record:
            dog_info_list.append({
                'dog_name': dog_record.dog_name,
                'dog_image_url': dog_record.image.url if dog_record.image else None  # 画像がない場合はNoneを設定
            })
        else:
            dog_info_list.append({
                'dog_name': '未登録',
                'dog_image_url': '画像なし'
            })

    return render(request, 'ranking.html', {'dog_info_list': dog_info_list})


class CommentListView(TemplateView):
    template_name = 'comment.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.order_by('-post_date')
        context['form'] = self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            postdata = form.save(commit=False)
            postdata.user = request.user
            postdata.post_date = timezone.now()
            postdata.save()
            return redirect('dogapp:comment')
        else:
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)


class CommentDeleteView(DeleteView):
    template_name = 'comment_delete.html'
    model = Comment
    success_url = reverse_lazy('dogapp:comment')

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
