from django.urls import path

from . import views

urlpatterns = [
    path('', views.PollsView.as_view()),
    path('<int:pk>', views.PollsRUDView.as_view()),
    path('<int:poll_id>/options', views.OptionsView.as_view()),
    path('<int:poll_id>/options/<int:pk>', views.OptionsRUDView.as_view()),
    path('<int:poll_id>/comment', views.CommentsView.as_view()),
    path('<int:poll_id>/comment/<int:pk>', views.CommentsRUDView.as_view()),
]