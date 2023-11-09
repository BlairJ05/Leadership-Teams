
from django.contrib import admin
from django.urls import path
from app.views import team_views, leadership_views

urlpatterns = [
    path("", team_views, name="home"),
    path("<team>/", leadership_views, name="leadership"),
    path('admin/', admin.site.urls),
]
