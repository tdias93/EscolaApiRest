from django.urls import path, include
from apps.escola.views import AlunosViewSet, CursosViewSet, MatriculaViewSet
from rest_framework import routers


routers = routers.DefaultRouter()
routers.register('alunos', AlunosViewSet, basename='Alunos')
routers.register('cursos', CursosViewSet, basename='Cursos')
routers.register('matricula', MatriculaViewSet, basename='Matricula')

urlpatterns = [
    path('', include(routers.urls)),
]