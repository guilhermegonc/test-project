from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import app.views, auth0.views

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
    path("paywall", auth0.views.paywall),
    path("dashboard", auth0.views.dashboard),
    path("logout", auth0.views.logout),
    path("", include('django.contrib.auth.urls')),
    path("", include('social_django.urls')),
]
