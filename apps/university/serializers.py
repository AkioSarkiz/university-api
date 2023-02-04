from rest_framework import serializers

from .models import CustomUser, Student, StudentGroup, Teacher


class CustomUserProfileSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        read_only_fields = ("id",)
        exclude = (
            "password",
            "is_superuser",
            "is_active",
            "date_joined",
            "groups",
            "user_permissions",
            "first_name",
            "last_name",
        )

    def get_full_name(self, instance):
        return f"{instance.first_name} {instance.last_name}"


class StudentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        read_only_fields = ("id",)
        fields = ['name']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        read_only_fields = ("id",)
        fields = ['first_name', 'last_name', 'group']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        read_only_fields = ("id",)
        fields = ["first_name", "last_name", "group"]
