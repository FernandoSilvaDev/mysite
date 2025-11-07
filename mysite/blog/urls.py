from django.urls import path
from blog.views import PostView, PostDetail
from blog import views

urlpatterns = [
    path("home/", PostView.as_view(), name='home'),
    path("", PostView.as_view(), name="index"),
    path("post/<slug:slug>/", PostDetail.as_view(), name="post_detail"),
]
