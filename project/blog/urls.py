from django.urls import path

from . import views

urlpatterns = [
    # Do blog-home, vs home, in case want to lookup. If just home, would conflict. This home is server.com/blog/
    # checks project.urls,, if /blog, moves here
    path('', views.home, name='blog-home'),
    # server.com/blog/about/
    path('about/', views.about, name='blog-about'),
]