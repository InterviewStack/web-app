from django.shortcuts import render
from feed.models import *
from core.models import *
from quest.models import *

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
            tag.save()
            question = Question(
                question_text=data.get('question_text'),
                question_type=data.get('question_type'),
                tags=tag.id,
                author=request.user.id or data.get('author'),
            )
            question.save()
            choices = data.get('choices', [])
            for choice in choices:
                answer = Answer(
                    question=question.id,
                    choice=choice
                )
                answer.save()
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
