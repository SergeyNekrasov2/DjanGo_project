from django.urls import path
from blogs.apps import BlogsConfig
from blogs.views import PostsListView, PostDetailsView, PostCreateView, PostUpdateView, PostDeleteView


# app_name = 'blogs'
app_name = BlogsConfig.name

urlpatterns = [
    path('blogs/home_data/', PostsListView.as_view(), name='home_data'),
    path('blogs/post/<int:pk>/', PostDetailsView.as_view(), name='post_details'),
    path('blogs/add_post/', PostCreateView.as_view(), name='add_post'),
    path('blogs/post/<int:pk>/edit/', PostUpdateView.as_view(), name='update_post'),
    path('blogs/post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete_post'),
]