from django.urls import path, include
from django.contrib import admin
from django.conf.urls import handler404
import app.views
import auth0.views
import forms.views
import tic_tac_toe.views
import app.views
import stocks.views
import expenses_management.views


admin.autodiscover()
handler404 = app.views.handler_404

urlpatterns = [
    path('', app.views.index, name='index'),
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
