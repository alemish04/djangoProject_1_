from django.urls import path

from .views import *

urlpatterns = [
    # path('', Bloglist.as_view(), name='home'),
    # path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    # path('about/', AboutPageView.as_view(), name='about'),
    #
    # path('s/', SearchResultView.as_view(), name="search_result_url")
    path("", post_list, name="posts_list_url"),
    path("post/<int:id>/", post_detail, name="post_detail_url"),
    path("categories/", category_list, name="category_list_url"),
    path("category/<int:id>/", category_detail, name="category_detail_url"),
    path("about/", about_project, name="about_project_url")
]
