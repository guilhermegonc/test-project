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
    path("tictactoe/", app.views.tic_tac_toe, name="tic-tac-toe"),
    path("atomic/", app.views.atomic, name="atomic"),
    path("populate-personas/", app.views.populate_personas, name="populate-personas"),
    path("admin/", admin.site.urls),
    path("complete/auth0", app.views.confirm_auth0, name="login"),
    path("exit", app.views.logout, name="logout")
]
