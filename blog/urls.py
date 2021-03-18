"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from posts.views import index, detail_view, create_view, delete_view, update_view
# from users.views import login_view
from users.views import register_view, login_view, logout_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', index, name="index"),
                  path('detail/<int:id>/', detail_view, name="detail"),
                  path('create/', create_view, name="create"),
                  path('delete/<int:id>', delete_view, name="delete"),
                  path('update/<int:id>', update_view, name="update"),
                  # path('login/', login_view, name="login"),
                  path('register/', register_view, name='register'),
                  path('login/', login_view, name="login"),
                  path('logout/', logout_view, name="logout"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# here MEDIA_URL is placed instead of STATIC_URL and same for MEDIA_ROOT
# otherwise the uploaded image will not be displayed
