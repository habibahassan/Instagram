from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('profile/update/',views.update_profile,name='update_profile'),
    path('no profile/',views.no_profile),
    path('search/', views.search_results, name='search_results'),
    path('new/image/',views.new_image,name="new_image"),
    path('comment/', views.comment, name='comment'),
    path('comment/like/',views.like_pic,name="like"),
    path('image/update',views.update_image,name='update_image'),
    path('profile/follow/', views.follow, name='follow'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)