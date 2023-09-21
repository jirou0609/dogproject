from django.db import models
from accounts.models import CustomUser


class Dogs(models.Model):
    dog_name = models.CharField(verbose_name='犬名', max_length=200)
    image = models.ImageField(verbose_name='イメージ', upload_to='photos')
    comment = models.TextField(verbose_name='コメント',)

    def __str__(self):
        return self.dog_name

class UserAnswer(models.Model):
    answer_1 = models.IntegerField(verbose_name='回答1',)
    answer_2 = models.IntegerField(verbose_name='回答2',)
    answer_3 = models.IntegerField(verbose_name='回答3',)
    answer_4 = models.IntegerField(verbose_name='回答4',)
    answer_5 = models.IntegerField(verbose_name='回答5',)
    answer_6 = models.IntegerField(verbose_name='回答6',)
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)


class Choice(models.Model):
    question_1 = models.IntegerField(verbose_name='質問1',)
    question_2 = models.IntegerField(verbose_name='質問2',)
    question_3 = models.IntegerField(verbose_name='質問3',)
    question_4 = models.IntegerField(verbose_name='質問4',)
    question_5 = models.IntegerField(verbose_name='質問5',)
    question_6 = models.IntegerField(verbose_name='質問6',)
    dog_name = models.ForeignKey(Dogs, verbose_name='犬名', on_delete=models.CASCADE)


class Result(models.Model):
    result = models.IntegerField(verbose_name='リザルト',)
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)


# コメントモデル
class Comment(models.Model):
    category = models.ForeignKey(Dogs, on_delete=models.CASCADE, verbose_name='犬名', related_name='comments', null=True, blank=True)
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)
    comment_text = models.TextField(verbose_name='コメント')
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post_date}'
