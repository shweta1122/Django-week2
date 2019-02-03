
from django.contrib import admin
from django.urls import path

from posts.views import show_post, homepage, detail, post_create, subject_sidebar, post_update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', show_post, name='post-show'),
    path('posts/create', post_create, name='post-create'),
    path('', homepage),

    path('posts/<slug:post_id>', detail),
    path('subject/<int:id>', subject_sidebar),
    path('posts/update/<int:id>', post_update, name='post-update'),
]


#  path('posts/<slug:slug>', detail),
