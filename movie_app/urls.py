from django.urls import path
# from django.contrib.auth.views import LogoutView
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

  
           
urlpatterns = [

    path('login', views.login, name='login'),
    path('report/', views.report, name='report'),
    path("", views.register, name="register"),
    path("home/", views.home, name="home"),
    path('logout', views.logout, name='logout'),
    
            ]

if settings.DEBUG:

        urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()