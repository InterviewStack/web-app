from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from feed.models import *
from core.models import *
from quest.models import *
from django.urils import timestamp
from django.db.models import Sum


# Create your views here.
class addQuestions(APIView):
    def post(self, request):
        data = request.data
        try:
            tag = Tag(
                company_name=data.get('company_name'),
                content_type=data.get('content_type'),
                difficulty=data.get('difficulty', None),
                domain=data.get('domain'),
                technical_tags=data.get('technical_tags')
            )
            tag, created = Tag.objects.get_or_create(**tag_data)
            question = Question(
                question_text=data.get('question_text'),
                question_type=data.get('question_type'),
                tags=tag,
                author=request.user.id or data.get('author'),
            )
            question.save()
            choices = data.get('choices', [])
            for choice in choices:
                choice = Choice(
                    question=question.id,
                    choice=choice,
                )
                answer.save()
            answer = Answer(
                question=question.id,
                choice=data.get('correct_answer')
            )
        except Exception as e:
            return Response({'error': str(e)}, status=400)

class addTag(APIView):
    def post(self,request):
        data = request.data
        try:
            tag = Tag(
                    company_name=data.get('company_name'),
                    content_type=data.get('content_type'),
                    difficulty=data.get('difficulty', None),
                    domain=data.get('domain'),
                    technical_tags=data.get('technical_tags')
                )
            tag.save()
            return Response({"message": "Tag created successfully", "tag_id": tag.id}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class addQuiz(APIView):
    def post(self, request):
        data = request.data
        try:
            author = request.user
            test_duration = data.get("duration")
            tag_data = {
                'company_name': data.get('company_name'),
                'content_type': data.get('content_type'),
                'difficulty': data.get('difficulty', None),
                'domain': data.get('domain'),
                'technical_tags': data.get('technical_tags')
            }
            tag, created = Tag.objects.get_or_create(**tag_data)
            question_ids = data.get("questions", [])
            questions = Question.objects.filter(id__in=question_ids)
            quiz = Quiz.objects.create(
                author=author,
                test_duration=test_duration,
                tags=tag,
                question=questions
            )
            return Response({'message': 'Quiz created successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class recordAnswer(APIView):
    def post(self, request):
        data = request.data
        try:
            student = request.user
            question_id = data.get('question_id')
            ques = Question.objects.get(id=question_id)
            quiz_id = data.get('quiz_id')
            quiz = Quiz.objects.get(id=quiz_id)
            choice = data.get('choice')
            if choice == Answer.objects.get(question=ques).choice:
                reward = 1
            question_result, created = QuestionResult.objects.update_or_create(
                student=student,
                question=ques,
                choice= choice,
                reward= reward,
                quiz= quiz,  
                attempt = data.get('attempt')
            )
            return Response({'reward': reward}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class submitTest(APIView):
    data = request.data
    def post(self,request):
        try:
            student = request.user
            quiz = Quiz.objects.get(quizid = data.get("quiz"))
            attempt = data.get('attempt')
            score = QuestionResult.objects.filter(student=student, quiz=quiz, attempt=attempt).aggregate(Sum('reward'))
            time_submitted = timestamp.now()
            