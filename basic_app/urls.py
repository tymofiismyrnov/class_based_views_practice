from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    path('<int:pk>/', views.SchoolDetailView.as_view(), name='detail')
]

app_name = 'basic_app'
