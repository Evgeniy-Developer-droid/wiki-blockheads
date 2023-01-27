from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name='main-page'),
    path('create-new-post', views.create_new_post, name='create-new-post'),
    
    path('games', views.games, name='games'),
    path('new-edits', views.new_edits, name='new-edits'),
    path('new-games', views.new_games, name='new-games'),
    path('randome-game', views.randome_game, name='randome-game'),

    path('search-results', views.SearchGames.as_view(), name='search_results'),

    path('update-post/<int:pk>', views.update_post, name='update-post'),
    path('post/<int:pk>', views.single_post, name='single-post'),

    path('api/all-posts', views.GetAllPostsView.as_view(), name='all-posts'),
    path('api/all-posts-by-user/<int:user>', views.GetPostsForUser.as_view(), name='all-posts-by-user'),
    path('api/single-post/<int:pk>', views.GetSinglePost.as_view(), name='api-single-post')
]