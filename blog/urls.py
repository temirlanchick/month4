from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('current_date/', views.current_date),
    path('goodbye/', views.goodbye),
    path('', views.main_view),
    path('', include('post.urls')),
    path('users/', include('users.urls'))
]



