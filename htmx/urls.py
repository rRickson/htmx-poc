"""htmx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
landings:
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
from .views import landing, sample_post,dashboard,widget,form_sign,submit_form
urlpatterns = [
    path('admin/', admin.site.urls),
     path('landing/', landing, name='landing'),
    path('sample-post/',sample_post, name='sample-post'),
    path('dashboard/',dashboard, name='dashboard'),
    path('widget/(?P<widget_type>[0-9]+)$',widget, name='widget'),
    path('form',form_sign, name='form_sign'),
    path('submit-form',submit_form, name='submit_form'),
]
