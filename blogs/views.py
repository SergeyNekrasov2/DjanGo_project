from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

class PostsListView(ListView):
    model = Post
    template_name = 'blogs/home_data.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """ Выводим только опубликованные статьи """
        return Post.objects.filter(is_published=True)

class PostDetailsView(DetailView):
    model = Post
    template_name = 'blogs/post_details.html'
    context_object_name = 'post'


    def get_object(self, queryset=None):
        """ Увеличиваем количество просмотров при каждом открытии статьи """
        post = super().get_object(queryset)
        post.views += 1
        post.save(update_fields=['views'])
        return post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image', 'is_published']
    template_name = 'blogs/add_post.html'
    success_url = reverse_lazy('blogs:home_data')

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image', 'is_published']
    template_name = 'blogs/add_post.html'

    def get_success_url(self):
        return reverse('blogs:post_details', kwargs={'pk': self.object.pk})

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blogs/delete_post.html'
    success_url = reverse_lazy('blogs:home_data')