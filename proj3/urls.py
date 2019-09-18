from django.urls import path
from . views import list_five, create_five, update_five, delete_five

urlpatterns = [
    path('odd/', list_five, name='list_five'),
    path('new_', create_five, name='create_five'),
    path('update_/<int:id>/', update_five, name='update_five'),
    path('delete_/<int:id>/', delete_five, name='delete_five'),
]