"""gps URL Configuration

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
from gpsdj.views import LocationList, LocationCreate, LocationCreate,LocationDelete, LocationDetail, LocationUpdate


urlpatterns = [
    path('create/', LocationCreate.as_view(), name='create-Location'),
    path('', LocationList.as_view()),
    path('<int:device_id>/', LocationDetail.as_view(), name='retrieve-Location'),
    path('update/<int:device_id>/', LocationUpdate.as_view(), name='update-Location'),
    path('delete/<int:device_id>/', LocationDelete.as_view(), name='delete-Location'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'))
]
