from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import handler404
import app.views
import auth0.views
import forms.views
import tic_tac_toe.views
import smart_home.views
import app.views
import stocks.views
import expenses_management.views


admin.autodiscover()
handler404 = app.views.handler_404

urlpatterns = [
    path('', app.views.index, name='index'),
    path('webhook', app.views.webhook),
    path('automation_webhook', app.views.automation_webhook),
    path('profile', app.views.profile),
    path('destroy-user', app.views.destroy_user),

    path('tictactoe', tic_tac_toe.views.tic_tac_toe, name='tic-tac-toe'),
    
    path('embed-form', forms.views.embed_form, name='embed-form'),
    
    path('custom-form', forms.views.custom_form, name='custom-form'),
    path('populate-personas', forms.views.populate_personas, name='populate-personas'),
    path('delete-persona/<int:persona_id>', forms.views.delete_persona, name='delete-persona'),
        
    path('login', auth0.views.login, name='login'),
    path('logout', auth0.views.logout),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),

    path('smart-home', smart_home.views.smart_home, name='smart-home'),
    path('settings', smart_home.views.settings, name='settings'),
    
    path('join', smart_home.views.join, name='join'),
    path('join-account', smart_home.views.join_account, name='join-account'),
    
    path('create-account', smart_home.views.create_account, name='create-account'),
    
    path('m/<str:microcontroller_token>', smart_home.views.microcontroller, name='microcontroller'),
    path('m/<str:microcontroller_token>/update', smart_home.views.update_microcontroller, name='update-microcontroller'),
    path('m/<str:microcontroller_token>/device', smart_home.views.device_settings, name='device-settings'),
    path('m/<str:microcontroller_token>/destroy', smart_home.views.destroy_microcontroller, name='destroy-microcontroller'),
    path('add-microcontroller', smart_home.views.add_microcontroller, name='add-microcontrollers'),
    path('populate-microcontroller', smart_home.views.populate_microcontroller, name='populate-microcontroller'),

    path('update-pins', smart_home.views.update_device, name='update-pins'),

    path('wallet', stocks.views.wallet, name='wallet'),
    path('update-wallet', stocks.views.update_wallet, name='wallet-update'),
    
    path('recommendations', stocks.views.recommendations, name='recommendations'),
    path('change-recommendation-status', stocks.views.change_recommendation_status, name='update-recommendation-status'),

    path('finance-dashboard', expenses_management.views.dashboard, name='finance-dashboard'),
    path('load-transactions/<str:transaction_type>', expenses_management.views.load_older),
    path('destroy-transaction/<str:transaction_type>', expenses_management.views.destroy_transaction),
    path('expenses', expenses_management.views.expenses, name='expenses'),
    path('recurring-payments', expenses_management.views.recurring, name='recurring-payments'),
    path('goals', expenses_management.views.goals, name='goals'),
    path('savings', expenses_management.views.savings, name='savings'),
    path('update-expense', expenses_management.views.update_expense, name='update-expense'),    
    path('update-recurring', expenses_management.views.update_recurring, name='update-recurring'),
    path('update-goal', expenses_management.views.update_goal, name='update-goal'),
    path('update-saving', expenses_management.views.update_saving, name='update-saving'),
]
