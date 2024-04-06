from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import AutoBranch
from .serializers import *
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(method='GET')
@api_view(['GET'])
def get_employee_branch(request, pk):
    if request.method == 'GET':
        employee = get_object_or_404(Employee, pk=pk)
        branch_id = employee.branch.id
        branch = get_object_or_404(AutoBranch, id=branch_id)
        serializered_branch = AutoBranchSerializer(branch)
        return Response(serializered_branch.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='GET')
@api_view(['GET'])
def check_branch_auto(request, name, pk):
    if request.method == 'GET':
        branch = get_object_or_404(AutoBranch, name=name)
        auto = get_object_or_404(Automobile, pk=pk)
        if auto.branch.id == branch.id:
            return Response({'message': 'Korsatilgan branchda automobil mavjud!'}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)