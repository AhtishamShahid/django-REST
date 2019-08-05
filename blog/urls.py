from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='posts'),
    path('categories/', views.CategoryList.as_view(), name='categories'),

    # path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
