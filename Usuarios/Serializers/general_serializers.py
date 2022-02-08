from rest_framework import serializers
from Usuarios.models import Usuario


class UsuarioTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields=("username",'email','nombres','apellidos', 'id_usuario')
class UsuarioSerializer(serializers. ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        
    def create(self,validated_data):
        usuario = Usuario(**validated_data)
        usuario.set_password(validated_data['password'])
        usuario.save()
        return usuario
    def update(self, instance, validated_data):
        updated_usuario = super().update(instance,validated_data)
        updated_usuario.set_password(validated_data['password'])
        updated_usuario.save()
        return updated_usuario

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
    
    def to_representation(self, instance):
        return {
                'id_usuario':instance['id_usuario'],
                'username':instance['username'],
                'email':instance['email'],
                'password':instance['password']
            }