# Generated by Django 3.0.8 on 2020-09-10 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_quizquestion_quiz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizquestion',
            name='quiz',
        ),
        migrations.AddField(
            model_name='quizquestion',
            name='quiz',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='quiz', to='quiz.Quiz'),
            preserve_default=False,
        ),
    ]