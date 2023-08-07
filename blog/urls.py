from django.urls import path
from blog.views import BlogDetailView


app_name = 'blog'

urlpatterns = [
    path('detail_article/<int:pk>', BlogDetailView.as_view(), name='detail_article'),
    ]
