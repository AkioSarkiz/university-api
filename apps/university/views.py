from rest_framework import viewsets, permissions
from . import models
from . import serializers


class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    permission_classes = [permissions.IsAuthenticated]


class StudentGroupViewSet(viewsets.ModelViewSet):
    queryset = models.StudentGroup.objects.all()
    serializer_class = serializers.StudentGroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]
