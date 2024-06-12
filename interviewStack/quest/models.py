from django.db import models
from core.models import Tag, UserProfile

class Question(models.Model):
    question_text = models.TextField()
    question_type = models.CharField(max_length=10)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    posted_timestamp = models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.TextField()

class Quiz(models.Model):
    quizid = models.TextField(unique=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)

class QuestionResult(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Answer, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    reward = models.IntegerField()
    updated_timestamp = models.DateTimeField(auto_now_add=True)

class QuizResult(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.FloatField()
    date_taken = models.DateTimeField(auto_now_add=True)
