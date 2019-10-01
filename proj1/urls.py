from django.urls import path
from .views import list_home, StaticViewSitemap, create_home, update_home, delete_home
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'static':StaticViewSitemap,
}


urlpatterns = [
    path('', list_home, name='list_home'),
    path('sitemap.xml/', sitemap,{'sitemaps':sitemaps}),
    path('new_', create_home, name='create_home'),
    path('update_/<int:id>/', update_home, name='update_home'),
    path('delete_/<int:id>/', delete_home, name='delete_home'),
]