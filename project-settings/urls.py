from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import app.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
urlpatterns = [
    path("", app.views.index, name="index"),
    path("embed-form/", app.views.embed_form, name="embed-form"),
    path("custom-form/", app.views.custom_form, name="custom-form"),
    path("api-name/", app.views.api_name, name="api-name"),
    path("tictactoe/", app.views.tic_tac_toe, name="tic-tac-toe"),
    path("atomic/", app.views.tic_tac_toe, name="atomic"),
    path("auth/callback/", app.views.auth_callback, name="rd-auth"),
    path("populate-personas/", app.views.populate_personas, name="populate-personas"),
    path("admin/", admin.site.urls)
]
