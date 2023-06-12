from django.urls import path
from . import views

app_name = 'quoteapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('tag/', views.tag, name='tag'),
    path('author/', views.author, name='author'),
    path('quote/', views.quote, name='quote'),
    path('detail_quote/<int:quote_id>', views.detail_quote, name='detail_quote'),
    path('detail_author/<int:quote_authors_id>', views.detail_author, name='detail_author')
]

