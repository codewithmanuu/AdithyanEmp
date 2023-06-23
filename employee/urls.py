from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("",views.login_admin,name="login"),
    path("index/",views.index,name="index"),
    path("create/", views.create_employee, name="create_employee"),
    path("manage/", views.manage_employee, name="manage_employee"),
    path("edit/<int:pk>", views.edit_employee, name="edit_employee"),
    path('delete/<int:id>', views.delete_employee, name="delete"),
    path("employee_leaves/",views.employee_leaves,name="employee_leaves"),
    path('create_leave',views.CreateLeave,name='create'),
    path('salary_graph',views.salary_graph,name='salary_graph')

]
