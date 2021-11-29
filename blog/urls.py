from django.urls import path

from . import views
# Code Here


urlpatterns = [
    path('blog', views.blog_home, name='blog_home'),
    path('blog/create', views.create_post, name='create_post'),
    path('blog/draft', views.create_draft, name='create_draft'),
    path('blog/draft/<int:post_id>', views.create_draft, name='update_draft'),
    path('blog/<str:username>', views.user_blog, name='user_blog'),
    path('blog/view/<int:post_id>', views.view_post, name='view_post'),
    path('blog/edit/<int:post_id>', views.edit_post, name='edit_post'),
    path('blog/delete/<int:post_id>', views.delete_post, name='delete_post'),
]
