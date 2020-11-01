from django.urls import path
from telephone_manage import views

urlpatterns = [
    path('',views.manage),
    path('add',views.project_add),
    path('edit/<int:pid>/',views.project_edit),
    path('delete/<int:pid>/',views.project_delete),
    path('search',views.project_search),

]