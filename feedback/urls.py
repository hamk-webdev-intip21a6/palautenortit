from django.urls import path
from . import views

app_name = 'feedback'
urlpatterns = [
    path('', views.FeedbackCreateView.as_view(), name='index'),
    path('index_success/', views.index_success, name='index_success'),
]
