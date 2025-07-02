from django.urls import path
from django.views.decorators.cache import cache_page

from catalog import views
from catalog.apps import CatalogConfig
# from catalog.views import home, contacts
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
# from blogs.views import PostListView, PostDetailsView, PostCreateView, PostUpdateView, PostDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    # path("", home, name="home"),
    # path("contacts/", contacts, name="contacts"),
    path('', ProductListView.as_view(), name='product_list'),
    path('catalog/<int:pk>/',cache_page(60) (ProductDetailView.as_view()), name='product_detail'),
    path('catalog/create', ProductCreateView.as_view(), name='product_create'),
    path('catalog/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('catalog/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('category/<int:category_id>/', views.ProductsByCategoryView.as_view(), name='products_by_category'),
]
    # path('home_data/', PostListView.as_view(), name='home_data'),
    # path('post/<int:pk>/', PostDetailsView.as_view(), name='post_details'),
    # path('add_post/', PostCreateView.as_view(), name='add_post'),
    # path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='update_post'),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete_post'),

