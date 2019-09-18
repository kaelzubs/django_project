from django.urls import path
from . views import list_about, create_about, update_about, delete_about

urlpatterns = [
    path('us/', list_about, name='list_about'),
    path('new_', create_about, name='create_about'),
    path('update_/<int:id>/', update_about, name='update_about'),
    path('delete_/<int:id>/', delete_about, name='delete_about'),
]