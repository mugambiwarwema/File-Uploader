from django.shortcuts import render
from .serializers import UserProfile_Serializer
from .models import UserProfile
from rest_framework import pagination, permissions, status, viewsets

from rest_framework_datatables_editor.filters import DatatablesFilterBackend
from rest_framework_datatables_editor.pagination import (DatatablesPageNumberPagination)
from rest_framework_datatables_editor.renderers import (DatatablesRenderer)
from rest_framework_datatables_editor.viewsets import (DatatablesEditorModelViewSet)

# Create your views here.
class UserProfile_ViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfile_Serializer