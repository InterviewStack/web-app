from django.contrib import admin
from .models import Question, Choice, Answer, Quiz, QuestionResult, QuizResult

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Answer)
admin.site.register(Quiz)
admin.site.register(QuestionResult)
admin.site.register(QuizResult)
