from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Additional attributes
    answer = models.CharField(max_length=250, default='')

    def submit_answer(self, ans):
        self.answer = ans
        self.save()


    def __str__(self):
        return self.user.username

class Case(models.Model):
    diagnosis = models.CharField(max_length=250, unique=True)
    history = models.CharField(max_length=500)
    teach_points = models.CharField(max_length=1000)

    def __str__(self):
        return self.diagnosis

class Quiz(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, default='')
    num_questions = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    question = models.CharField(max_length=250, default='')

    def __str__(self):
        return self.question

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

class UserAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200, default='')
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer

class UserPerformance(models.Model):
    user_answer = models.ForeignKey(UserAnswer, on_delete=models.CASCADE)
    total_attempts = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    complete = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
