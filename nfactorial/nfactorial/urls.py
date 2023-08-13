from django.urls import path
from . import views

urlpatterns = [
    path('', views.nfactorial_view, name='nfactorial'),
    path('<int:first>/add/<int:second>/', views.add_view, name='add'),
    path('transform/<str:text>/', views.upper_view, name='upper'),
    path('check/<str:word>/', views.palindrome_view, name='palindrome'),
    path('calc/<int:first>/<str:operation>/<int:second>/', views.calculator_view, name='calculator'),
]
