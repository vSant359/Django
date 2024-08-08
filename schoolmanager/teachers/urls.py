from django.urls import path
from .views import TeacherListView, TeacherDetailView

# As rotas utilizam uma "view" como referência, a rota "/students" tem como referência a view "StudentDetailView", ou seja, quando uma requisição for feita para essa rota quem irá processar essa requisa será essa classe.

urlpatterns = [
    path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path('teacher/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),
]