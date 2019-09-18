from django.urls import path
from . views import list_disclaim, create_disclaim, update_disclaim, delete_disclaim

urlpatterns = [
    path('page/', list_disclaim, name='list_disclaim'),
    path('new_', create_disclaim, name='create_disclaim'),
    path('update_/<int:id>/', update_disclaim, name='update_disclaim'),
    path('delete_/<int:id>/', delete_disclaim, name='delete_disclaim'),
]