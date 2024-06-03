from django.urls import path
from . import views

app_name = "quoteapp"

urlpatterns = [
    path('', views.main, name="root"),
    path('<int:page>', views.main, name="root_paginate"),
    path('new_tag/', views.tag, name='tag'),
    path('new_quote/', views.quote, name='quote'),
    path('new_author/', views.author, name='author'),
    path('detail/<int:author_id>', views.detail, name='detail'),
    path('tag/<int:tag_id>', views.tags, name='tags'),
]
