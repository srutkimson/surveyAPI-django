from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SurveyViewSet, QuestionViewSet, AnswerViewSet, ChoiceViewSet, ActiveSurveyListViewSet, \
                   UserSurveyListViewSet, AnswerCreateViewSet, SurveyIdViewSet

app_name = "surveyApp"
router = DefaultRouter()
router.register(r'surveys', SurveyViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'activeSurveys', ActiveSurveyListViewSet)
router.register(r'userSurveys', UserSurveyListViewSet, basename='userSurveys')
router.register('surveys/(?P<id>\d+)/questions/(?P<question_pk>\d+)/answers', AnswerCreateViewSet, basename='answerCreate')
router.register('surveys/(?P<id>\d+)/questions', SurveyIdViewSet, basename='Surveys&Questions')
urlpatterns = [
    path('', include(router.urls)),
]