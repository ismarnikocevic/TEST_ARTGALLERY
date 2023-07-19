from django.urls import path
from . import views
from .views import UpdatePostView

urlpatterns = [
#     blogs
    path("blogslist/", views.blogslist, name="blogslist"),
    path("", views.home, name="home"),
    path("biography/", views.biography, name="biography"),
    path("blog/<int:id>/", views.blogs_detail, name="blogs_detail"),
    path("add_blogs/", views.add_blogs, name="add_blogs"),
    path("edit_blog_post/<int:pk>/", UpdatePostView.as_view(), name="edit_blog_post"),
    path("delete_blog_post/<int:id>/", views.Delete_Blog_Post, name="delete_blog_post"),
    path("search/", views.search, name="search"),


]