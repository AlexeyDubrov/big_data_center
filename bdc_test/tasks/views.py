# Create view
from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .models import Tasks
from .serializer import TasksSerializer


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

