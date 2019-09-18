from django.urls import path
from . views import list_contact, create_contact, update_contact, delete_contact, contact_success

urlpatterns = [
    path('us', list_contact, name='list_contact'),
    path('contact_success', contact_success, name='contact_success'),
    path('new_', create_contact, name='create_contact'),
    path('update_/<int:id>/', update_contact, name='update_contact'),
    path('delete_/<int:id>/', delete_contact, name='delete_contact'),
]