from rest_framework import serializers
from .models import MyUser


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True)

    class Meta:
        model = MyUser
        fields = ['email', 'first_name',
                  'password', 'password2', 'phone_number']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = MyUser(email=self.validated_data['email'],
                      phone_number=self.validated_data['phone_number'],
                      first_name=self.validated_data['first_name'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = [
            'email',
            'first_name',
            'phone_number']


class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = MyUser
        fields = ('first_name', 'phone_number', 'email')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    def validate_email(self, value):
        user = self.context['request'].user
        if MyUser.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def validate_first_name(self, value):
        user = self.context['request'].user
        if MyUser.objects.exclude(pk=user.pk).filter(first_name=value).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})
        return value

    def update(self, instance, validated_data):
        instance.first_name = validated_data['first_name']
        instance.phone_number = validated_data['phone_number']
        instance.email = validated_data['email']

        instance.save()

        return instance


