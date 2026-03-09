from rest_framework import serializers
from .models import Livro, Autor, Genero, Editora, Cidade, Emprestimo, Leitor

class AutorSerializer(serializers.ModelSerializer):
    cidade_nome = serializers.StringRelatedField(source='cidade', read_only=True)

    class Meta:
        model = Autor
        fields = '__all__'

class LivroSerializer(serializers.ModelSerializer):
    autor_nome = serializers.StringRelatedField(source='autor', read_only=True)

    class Meta:
        model = Livro
        fields = '__all__'

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'

class EditoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'

class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = '__all__'

class EmprestimoSerializer(serializers.ModelSerializer):
    livro_nome = serializers.StringRelatedField(source='livro', read_only=True)
    leitor_nome = serializers.StringRelatedField(source='leitor', read_only=True)
    
    class Meta:
        model = Emprestimo
        fields = '__all__'

class LeitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leitor
        fields = '__all__'