from django.db import models
from accounts.models import CustomUser


class Dogs(models.Model):
    dog_name = models.CharField(verbose_name='犬名', max_length=200)
    image = models.ImageField(verbose_name='イメージ', upload_to='photos')
    comment = models.TextField(verbose_name='コメント',)

    def __str__(self):
        return self.dog_name

