from django.urls import path
from . import views

urlpatterns = [
    path("",views.IndexView.as_view(),name="index"),
    path("post/<int:pk>/",views.PostDetailView.as_view(),name="post_detail"),
    path("post/new/",views.CreatePostView.as_view(),name="post_new"),
    path("post/<int:pk>/edit/",views.EditPostView.as_view(),name="post_edit"),
    path("post/<int:pk>/delete/",views.DeletePostView.as_view(),name="post_delete"),
    path("category/<str:category>",views.CategoryView.as_view(),name="category"),
    path("search",views.SearchView.as_view(),name="search"),
]
