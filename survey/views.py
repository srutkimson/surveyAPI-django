from django.utils.datetime_safe import datetime
from rest_framework import viewsets, permissions, mixins
from rest_framework.generics import get_object_or_404


from .models import Survey, Question, Answer, Choice
from .serializers import SurveySerializer, QuestionSerializer, AnswerSerializer, ChoiceSerializer, UserSurveySerializer, \
    AnswerTextSerializer, AnswerSelectSerializer, AnswerMultipleSerializer, SurveyListSerializer


class SurveyViewSet(viewsets.ModelViewSet):
    serializer_class = SurveySerializer
    queryset = Survey.objects.all()
    permission_classes = permissions.IsAuthenticatedOrReadOnly,


class ActiveSurveyListViewSet(viewsets.GenericViewSet):
    queryset = Survey.objects.filter(dateEnd__lt=datetime.today())
    serializer_class = SurveySerializer
    permission_classes = permissions.AllowAny,


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = permissions.IsAuthenticatedOrReadOnly,


class ChoiceViewSet(viewsets.ModelViewSet):
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()
    permission_classes = permissions.IsAuthenticatedOrReadOnly,


class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = permissions.IsAuthenticatedOrReadOnly,


class AnswerCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = permissions.IsAuthenticated,

    def get_serializer_class(self):
        question = get_object_or_404(
            Question,
            pk=self.kwargs['question_pk'],
            survey__id=self.kwargs['id'],
        )
        if question.type == 'Text':
            return AnswerTextSerializer
        elif question.type == 'Select':
            return AnswerSelectSerializer
        else:
            return AnswerMultipleSerializer

    def perform_create(self, serializer):
        question = get_object_or_404(
            Question,
            pk=self.kwargs['question_pk'],
            survey__id=self.kwargs['id'],
        )
        serializer.save(user=self.request.user, question=question)


class UserSurveyListViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSurveySerializer
    permission_classes = permissions.IsAuthenticated,

    def get_queryset(self):
        user = self.request.user
        queryset = Survey.objects.filter(questions__answers__user=user)
        return queryset


class SurveyIdViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SurveyListSerializer
    permission_classes = permissions.IsAuthenticated,

    def get_queryset(self):
        queryset = Survey.objects.filter(id=self.kwargs['id'])
        return queryset
