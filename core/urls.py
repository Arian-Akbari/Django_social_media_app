from django.urls import path

from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('search', views.search, name='search'),
    path('follow', views.follow, name='follow'),
    path('like-post', views.like_post, name='like_post'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
]
