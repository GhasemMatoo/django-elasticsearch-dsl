from django.urls import path
from . import views

app_name = 'elastic'

urlpatterns = [
    path('', views.BookSearchView.as_view(), name='home'),
    path('book/<int:book_id>', views.BookDitail.as_view(), name='book-detail'),
]
