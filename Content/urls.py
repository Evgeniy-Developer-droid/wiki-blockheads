from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name='main-page'),
    path('create-new-post', views.create_new_post, name='create-new-post'),

    path('api/all-posts', views.GetAllPostsView.as_view(), name='all-posts'),
    path('api/all-posts-by-user/<int:user>', views.GetPostsForUser.as_view(), name='all-posts-by-user')
]