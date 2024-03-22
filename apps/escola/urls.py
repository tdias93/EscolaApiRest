from django.urls import path, include
from apps.escola.views import AlunosViewSet, CursosViewSet, MatriculaViewSet, ListaMatriculasAluno, ListaAlunosMatricula
from rest_framework import routers


routers = routers.DefaultRouter()
routers.register('alunos', AlunosViewSet, basename='Alunos')
routers.register('cursos', CursosViewSet, basename='Cursos')
routers.register('matricula', MatriculaViewSet, basename='Matricula')

urlpatterns = [
    path('', include(routers.urls)),
    path('alunos/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
    path('cursos/<int:pk>/matricula/', ListaAlunosMatricula.as_view())
]