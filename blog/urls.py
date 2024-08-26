
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="Home-page" ),
    path("posts/", views.PostsView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.postdetail, name="post-detail-page"),
    path("read-later/", views.ReadLaterView.as_view(), name="read-later"),
    path("remove-read-later/", views.RemoveReadLaterView.as_view(),name = "remove-read-later" ),
]