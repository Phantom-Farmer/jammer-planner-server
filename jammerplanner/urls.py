"""jammerplanner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from jammerplannerapi.views import check_user, register_user
from jammerplannerapi.views import UserView, BandView, SongView, SetView, SetSongView, RehearsalView, CommentView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'user', UserView, 'user')
router.register(r'band', BandView, 'band')
router.register(r'song', SongView, 'song')
router.register(r'set', SetView, 'set')
router.register(r'set_song', SetSongView, 'set_song')
router.register(r'rehearsal', RehearsalView, 'rehearsal')
router.register(r'comment', CommentView, 'comment')

urlpatterns = [
    path('register', register_user),
    path('checkuser', check_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
