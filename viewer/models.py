from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # performance = models.ForeignKey('viewer.Performance', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


# class Performance(models.Model):
#     score = models.CharField(max_length=100)


class OrganSystem(models.Model):
    name = models.CharField(max_length=75, default='')
    tutorials = models.ManyToManyField('viewer.Tutorial')

    def __str__(self):
        return self.name


class Tutorial(models.Model):
    name = models.CharField(max_length=75, default='')

    def __str__(self):
        return self.name


class Case(models.Model):
    name = models.CharField(max_length=250, default='')
    diagnosis = models.ForeignKey('viewer.Diagnosis', on_delete=models.SET_NULL, null=True)
    history = models.CharField(max_length=500, default='')
    teach_points = models.CharField(max_length=1000, default='')

    def get_image_url(self):
        case_name_low = self.name.lower()
        case_name = case_name_low.replace(' ', '_')
        case_name_dzi = case_name + '/' + case_name + '.dzi'
        return settings.STATIC_URL_2 + 'images/' + case_name_dzi

    def get_image_thumb(self):
        case_name_low = self.name.lower()
        case_name = case_name_low.replace(' ', '_')
        return settings.STATIC_URL_2 + 'images/' + case_name + '/thumb.PNG'

    def __str__(self):
        return str(self.id) + ': '+self.name


class Diagnosis(models.Model):
    text = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.text


class Quiz(models.Model):
    name = models.CharField(max_length=250, default='')

    def num_questions(self):
        return self.questions.all().count()

    def __str__(self):
        return self.name


class Question(models.Model):
    quiz = models.ManyToManyField('viewer.Quiz', related_name='questions')
    text = models.CharField(max_length=250, default='')

    def __str__(self):
        return self.text


# class Performance(models.Model):
#     user = models.ForeignKey(UserProfileInfo, related_name='user_answer', on_delete=models.CASCADE)
#     case = models.ForeignKey(Case, related_name='case_answer', on_delete=models.CASCADE)
#     answer = models.CharField(max_length=250, default='')
#
#     def submit_answer(self, ans):
#         self.answer = ans
#         self.save()
#
#     def get_absolute_url(self):
#         return reverse("profile")
#
#     def __str__(self):
#         return self.answer

# class UserAnswer(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     answer = models.CharField(max_length=200, default='')
#     is_correct = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.answer


# class UserPerformance(models.Model):
#     user_answer = models.ForeignKey(UserAnswer, on_delete=models.CASCADE)
#     total_attempts = models.IntegerField(default=0)
#     correct_answers = models.IntegerField(default=0)
#     complete = models.BooleanField(default=False)
#     timestamp = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.user.username
