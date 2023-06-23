from django.urls import path
from .views import *

urlpatterns = [
    path('', OrdersList.as_view()),
    path('<int:pk>/', DetailOrder.as_view())
]