from django.urls import path
from . import views

from .views import NewPost, AllPost, DetailPost, UpdatePost, DeletePost, Index, Gallery, About, Agriculture, Child, Contact, Donate, Ecology, Portfolio, Social

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('blog', AllPost.as_view(), name='blog'),
    path('gallery', Gallery.as_view(), name='gallery'),
    path('about', About.as_view(), name='about'),
    path('agriculture', Agriculture.as_view(), name='agriculture'),
    path('child', Child.as_view(), name='child'),
    path('contact', Contact.as_view(), name='contact'),
    path('donate', Donate.as_view(), name='donate'),
    path('ecology', Ecology.as_view(), name='ecology'),
    path('portfolio', Portfolio.as_view(), name='portfolio'),
    path('social', Social.as_view(), name='social'),
    path('post/<int:pk>', DetailPost.as_view(), name='detailPost'),
    path('new-post', NewPost.as_view(), name='newpost'),
    path('post/<int:pk>/update', UpdatePost.as_view(), name='updatePost'),
    path('post/<int:pk>/delete', DeletePost.as_view(), name='deletePost'),
]
