from django.urls import path
from blogs.views import PostsListView, PostDetailsView, PostCreateView, PostUpdateView, PostDeleteView


app_name = 'blogs'

urlpatterns = [
    path('', PostsListView.as_view(), name='home_data'),
    path('post/<int:pk>/', PostDetailsView.as_view(), name='post_details'),
    path('add_post/', PostCreateView.as_view(), name='add_post'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='update_post'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete_post'),
]