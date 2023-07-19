from django.urls import path
from . import views
from .views import UpdatePostView

urlpatterns = [
#     blogs
   
    path("paintingslist/", views.paintingslist, name="paintingslist"),
  
    
    path("painting/<int:id>/", views.paintings_detail, name="paintings_detail"),
    path("add_paintings/", views.add_paintings, name="add_paintings"),
    path("edit_paintings/<int:pk>/", UpdatePostView.as_view(), name="edit_paintings"),
    path("delete_paintings/<int:id>/", views.Delete_Paintings, name="delete_paintings"),
    path("ART_SEARCH/", views.ART_SEARCH, name="ART_SEARCH"),
    
    
   
]