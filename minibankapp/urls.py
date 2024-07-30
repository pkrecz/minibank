# -*- coding: utf-8 -*-

from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .views import (MainDasboard, ParameterUpdateView,
                    CustomerCreateView, CustomerListView, CustomerUpdateView, CustomerDeleteView, SelectCustomerAccountListView, CustomerCreateDoneView,
                    AccountTypeCreateView, AccountTypeListView, AccountTypeDeleteView, AccountTypeUpdateView,
                    AccountListView, AccountCreateView, AccountUpdateView, AccountGenerateUpdateView, AccountInterestUpdateView,
                    OperationCreateView, SelectCustomerOperationListView, SelectAcountOperationListView,
                    SelectCustomerHistoryListView, SelectAcountHistoryListView, HistoryOperationListView)


app_name = "minibankapp"
urlpatterns = [
     
     # Dashboard
     path(route="", view=MainDasboard.as_view(), name="dashboard"),

     # Parameter
     path(route="updateparameter/", view=ParameterUpdateView.as_view(), name="updateparameter"),

     # Customer
     path(route="newcustomer/", view=CustomerCreateView.as_view(), name="newcustomer"),
     path(route="newcustomer-done/<int:customer>/", view=CustomerCreateDoneView.as_view(), name="newcustomer_done"),
     path(route="listcustomer/", view=CustomerListView.as_view(), name="listcustomer"),
     path(route="updatecustomer/<int:customer>/", view=CustomerUpdateView.as_view(), name="updatecustomer"),
     path(route="deletecustomer/<int:customer>/", view=CustomerDeleteView.as_view(), name="deletecustomer"),

     # Account
     path(route="selectcustomer-account/", view=SelectCustomerAccountListView.as_view(), name="selectcustomer_account"),
     path(route="listaccount/<int:customer>/", view=AccountListView.as_view(), name="listaccount"),
     path(route="newaccount/<int:customer>/", view=AccountCreateView.as_view(), name="newaccount"),
     path(route="updateaccount/<int:customer>/<int:account>/", view=AccountUpdateView.as_view(), name="updateaccount"),
     path(route="generate/<int:customer>/<int:account>/", view=AccountGenerateUpdateView.as_view(), name="generate"),
     path(route="interest/", view=AccountInterestUpdateView.as_view(), name="interest"),

     # Operation
     path(route="selectcustomer-operation/", view=SelectCustomerOperationListView.as_view(), name="selectcustomer_operation"),
     path(route="selectaccount-operation/<int:customer>/", view=SelectAcountOperationListView.as_view(), name="selectacount_operation"),
     path(route="newoperation/<int:customer>/<int:account>/", view=OperationCreateView.as_view(), name="newoperation"),

     # History
     path(route="selectcustomer-history/", view=SelectCustomerHistoryListView.as_view(), name="selectcustomer_history"),
     path(route="selectaccount-history/<int:customer>/", view=SelectAcountHistoryListView.as_view(), name="selectacount_history"),
     path(route="historyoperation/<int:customer>/<int:account>/", view=HistoryOperationListView.as_view(), name="historyoperation"),

     # AccountType
     path(route="newaccounttype/", view=AccountTypeCreateView.as_view(), name="newaccounttype"),
     path(route="listaccounttype/", view=AccountTypeListView.as_view(), name="listaccounttype"),
     path(route="updateaccounttype/<str:accounttype>/", view=AccountTypeUpdateView.as_view(), name="updateaccounttype"),
     path(route="deleteaccounttype/<str:accounttype>/", view=AccountTypeDeleteView.as_view(), name="deleteaccounttype"),
    
     # Authorization
     path(route="login/", view=auth_views.LoginView.as_view(), name="login"),
     path(route="logout/", view=auth_views.LogoutView.as_view(), name="logout"),
     path(route="password-change/",
          view=auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('minibankapp:password_change_done')),
          name="password_change"),
     path(route="password-change/done/", view=auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
     path(route="password-reset/",
          view=auth_views.PasswordResetView.as_view(success_url=reverse_lazy('minibankapp:password_reset_done')),
          name="password_reset"),
     path(route="password-reset/done/", view=auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
     path(route="password-reset/<uidb64>/<token>/",
          view=auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('minibankapp:password_reset_complete')),
          name="password_reset_confirm"),
     path(route="password-reset/complete/",
          view=auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
