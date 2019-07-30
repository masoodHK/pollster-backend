from django.urls import path

from .views import CategoriesView, CategoriesRUDView

urlpatterns = [
    path('', CategoriesView.as_view()),
    path('<int:pk>', CategoriesRUDView.as_view()),
]