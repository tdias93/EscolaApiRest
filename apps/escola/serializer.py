from rest_framework import serializers
from apps.escola.models import Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Matricula
        exclude = []

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):

    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):

    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    data_nascimento = serializers.ReadOnlyField(source='aluno.data_nascimento')

    class Meta:
        model = Matricula
        fields = ['aluno_nome', 'data_nascimento']

class AlunoSerializerV2(serializers.ModelSerializer):
    
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'celular', 'rg', 'cpf', 'data_nascimento']