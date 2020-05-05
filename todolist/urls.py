from django.urls import path
from . import views

app_name = 'todolist'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:task_id>/done/', views.done, name='done'),
    path('todolist/create/', views.create, name='create'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete')
]
