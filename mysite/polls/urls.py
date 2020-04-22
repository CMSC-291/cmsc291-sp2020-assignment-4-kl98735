from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add_question/', views.add_question, name='add_question'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/add_choice/', views.add_choice, name='add_choice'),
    path('<int:question_id>/remove_choice/<int:choice_id>', views.remove_choice, name='remove_choice'),
    path('<int:question_id>/remove_question/', views.remove_question, name='remove_question')

]