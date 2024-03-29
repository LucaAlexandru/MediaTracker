"""MediaTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers
from books.api_views import BookViewSet
from games.api_views import GameViewSet
from films.api_views import FilmViewSet

router = routers.DefaultRouter()
router.register("books", BookViewSet)
router.register("games", GameViewSet)
router.register("films", FilmViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('api-auth/', include('rest_framework.urls')),
    path('', views.homepage, name='homepage'),
    path('books/', include('books.urls')),
    path('films/', include('films.urls')),
    path('games/', include('games.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/', include(router.urls))
]

urlpatterns += staticfiles_urlpatterns()