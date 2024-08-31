from django.conf.urls import url
from django.contrib import admin

from real_estate_agency import views

urlpatterns = [
    url(r'^$', views.show_flats),
    url(r'^search/$', views.show_flats),
    url(r'^admin/', admin.site.urls),
]
