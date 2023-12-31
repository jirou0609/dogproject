# Generated by Django 4.0.8 on 2023-09-20 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dogapp', '0004_comment_alter_result_result_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='dogapp.dogs', verbose_name='犬名'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(verbose_name='コメント'),
        ),
        migrations.DeleteModel(
            name='Response',
        ),
    ]
