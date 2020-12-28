from django.urls import path
from django.views.generic.edit import DeleteView
from .views import CategoryListView, homeView, articleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView

urlpatterns = [
    path('', homeView.as_view(), name="home"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('article/<int:pk>', articleDetailView.as_view(), name="article-detail"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
    path('categories/<str:cats>', CategoryView, name="category"),
    path('category-list/', CategoryListView, name="category-list"),
]