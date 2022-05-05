from django.db.models import Q
from rest_framework import serializers

from .models import Survey, Question, Answer, Choice


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('id', 'name', 'dateStart', 'dateEnd', 'description')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'text', 'survey', 'type')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'user', 'question', 'text', 'sChoice', 'mChoices')


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'text', 'question')


class QuestionListSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField('get_answer')

    class Meta:
        fields = ['text', 'answers']
        model = Question

    def get_answer(self, question):
        user = self.context.get('request').user
        answers = Answer.objects.filter(Q(question=question) & Q(user=user))
        serializer = AnswerSerializer(instance=answers, many=True)
        return serializer.data


class QuestionSurveyListSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField('get_answer')

    class Meta:
        fields = ['text', 'answers']
        model = Question

    def get_answer(self, question):
        answers = Answer.objects.filter(Q(question=question))
        serializer = AnswerSerializer(instance=answers, many=True)
        return serializer.data


class SurveyListSerializer(serializers.ModelSerializer):
    questions = QuestionSurveyListSerializer(read_only=False, many=True)

    class Meta:
        fields = ['id', 'questions', 'dateStart', 'dateEnd', 'description']
        model = Survey


class UserSurveySerializer(serializers.ModelSerializer):
    questions = QuestionListSerializer(read_only=True, many=True)

    class Meta:
        fields = ['id', 'name',  'questions', 'dateStart', 'dateEnd', 'description']
        model = Survey


class AnswerTextSerializer(serializers.ModelSerializer):
    serializer_class = AnswerSerializer

    class Meta:
        fields = ['text']
        model = Answer


class AnswerSelectSerializer(serializers.ModelSerializer):
    serializer_class = AnswerSerializer

    class Meta:
        fields = ['sChoice']
        model = Answer


class AnswerMultipleSerializer(serializers.ModelSerializer):
    serializer_class = AnswerSerializer

    class Meta:
        fields = ['mChoices']
        model = Answer
