from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views


urlpatterns = [
	path('', views.api_root),
	path('snippets/', views.SnippetList.as_view()),
	path('snippets/<int:pk>/', views.SnippetDetails.as_view()),
	path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),
	path('users/', views.UserList.as_view()),
	path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)