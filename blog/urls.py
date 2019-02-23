from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.news, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('articleupload/', views.news, name='news'),
    path('articleupload/<int:pk>', views.news_detail, name='news_detail'),
    path('articleupload/worldnews', views.world_news, name='world_news'),
    path('articleupload/usnews', views.us_news, name='us_news'),
    path('articleupload/politics', views.politics_news, name='politics_news'),
    #path(r'^articleupload/(?P<int:pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    path('articleupload/<pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    #path(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    #path(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    path('comment/<pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<pk>/remove/', views.comment_remove, name='comment_remove'),
    #path('vote/<pk>/vote_up/', views.vote_up, name='vote_up'),
    # path('admin/', admin.site.urls),
]
