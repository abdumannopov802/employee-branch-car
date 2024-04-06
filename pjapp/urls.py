from django.urls import path
from .views import *

urlpatterns = [
    path('get-employee-branch/<int:pk>', get_employee_branch),
    path('check-branch-auto/<str:name>/<int:pk>', check_branch_auto),
]
