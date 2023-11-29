
from django.urls import path

from .views import *
urlpatterns = [

    path('login/',login_view,name='login'),
    path("check_session", check_session , name="check_session"),
    path("users/", users , name="users"),
    path("reset_password_get_token/", reset_password_get_token, name="reset_password_get_token"),
    path("reset_password_confirm/<uidb64>/<token>/", reset_password_confirm, name="reset_password_confirm"),

    # Admin
    path("get_participant/", get_participant, name="get_participant"),
    path("get_participant/<id>/", get_participant_details, name="get_participant_details"),

    # Chef de délégation

    path('get_delegation_participant/<type>/', get_delegation_participant, name='get_delegation_participant'),
    path('add_delegation_participant/', add_delegation_participant, name='add_delegation_participant')

]