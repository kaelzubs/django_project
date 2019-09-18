from django.urls import path
from . views import list_ten, create_ten, update_ten, delete_ten

urlpatterns = [
    path('odd/', list_ten, name='list_ten'),
    path('new_', create_ten, name='create_ten'),
    path('update_/<int:id>/', update_ten, name='update_ten'),
    path('delete_/<int:id>/', delete_ten, name='delete_ten'),
]