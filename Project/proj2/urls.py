from django.urls import path
from . views import list_three, create_three, update_three, delete_three

urlpatterns = [
    path('odd/', list_three, name='list_three'),
    path('new_', create_three, name='create_three'),
    path('update_/<int:id>/', update_three, name='update_three'),
    path('delete_/<int:id>/', delete_three, name='delete_three'),
]