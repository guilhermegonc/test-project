from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import app.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", app.views.index, name="index"),
    path("cta/", app.views.cta, name="cta"),
    path("html-model/", app.views.template, name="test"),
    path("admin/", admin.site.urls),
]
