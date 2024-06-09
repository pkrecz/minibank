# -*- coding: utf-8 -*-

from django import forms
from .models import (CustomerModel, AccountModel, OperationModel, AccountTypeModel, ParameterModel)


class IdAccountModelChoiceField(forms.ModelChoiceField):
    """ Customized field for new account form"""

    def label_from_instance(self, object):
        return object.Id_account_type + ' - ' + object.Description


class CustomerForm(forms.ModelForm):
    """ Customer form """

    Birth_date = forms.DateField(
                                label='Birth date',
                                widget=forms.DateInput(
                                format="%Y-%m-%d",
                                attrs={"type": "date", "class": "form_widget"}),
                                input_formats=["%Y-%m-%d"])
    Identification = forms.CharField(
                                label='Identification',
                                widget=forms.TextInput(
                                attrs={"style": "text-transform: uppercase;", "class": "form_widget"}))
    Pesel = forms.CharField(
                                label='PESEL',
                                widget=forms.TextInput(
                                attrs={"placeholder": "11 digits", "class": "form_widget"}))
    Postal_code = forms.CharField(
                                label='Postal code',
                                widget=forms.TextInput(
                                attrs={"placeholder": "00-000", "class": "form_widget"}))
    
    class Meta:
        model = CustomerModel
        exclude = (
                    'Created_date',
                    'Created_employee')


class NewAccountForm(forms.ModelForm):
    """ Form new account """

    FK_Id_account_type = IdAccountModelChoiceField(
                                label='Account type',
                                queryset=AccountTypeModel.objects.all(),
                                widget=forms.Select(attrs={"class": "form_widget"}))
    Percent = forms.DecimalField(
                                label='Percent',
                                initial=0,
                                widget=forms.NumberInput(
                                attrs={"class": "form_widget", "step": "0.1"}))
    Debit = forms.DecimalField(
                                label='Debit',
                                initial=0,
                                widget=forms.NumberInput(
                                attrs={"class": "form_widget", "type": "number"}))

    class Meta:
        model = AccountModel
        fields = ('FK_Id_account_type', 'Percent', 'Debit')


class UpdateAccountForm(forms.ModelForm):
    """ Form for changing account parameter """

    Percent = forms.DecimalField(
                                label='Percent',
                                widget=forms.NumberInput(
                                attrs={"class": "form_widget", "step": "0.1"}))
    Debit = forms.DecimalField(
                                label='Debit',
                                initial=0,
                                widget=forms.NumberInput(
                                attrs={"class": "form_widget", "type": "number"}))

    class Meta:
        model = AccountModel
        fields = ('Percent','Debit')


class NewAccountTypeForm(forms.ModelForm):
    """ Form for creating new account type """

    Id_account_type = forms.CharField(
                                label='Id account type',
                                widget=forms.TextInput(
                                attrs={"placeholder": "A-00", "style": "text-transform: uppercase;", "class": "form_widget"}))
    Subaccount = forms.CharField(
                                label='Subaccount',
                                widget=forms.TextInput(
                                attrs={"placeholder": "000000", "class": "form_widget"}))
    Percent = forms.DecimalField(
                                label='Percent',
                                initial=0,
                                widget=forms.NumberInput(
                                attrs={"class": "form_widget", "step": "0.1"}))
    
    class Meta:
        model = AccountTypeModel
        fields = '__all__'


class UpdateAccountTypeForm(forms.ModelForm):
    """ Form for updating account type data """
        
    Subaccount = forms.CharField(
                                label='Subaccount',
                                widget=forms.TextInput(
                                attrs={"placeholder": "000000", "class": "form_widget"}))
    Percent = forms.DecimalField(
                                label='Percent',
                                widget=forms.NumberInput(
                                attrs={"class": "form_widget", "step": "0.1"}))
    
    class Meta:
        model = AccountTypeModel
        exclude = ('Id_account_type',)


class UpdateParameterForm(forms.ModelForm):
    """ Form for changing system data """

    class Meta:
        model = ParameterModel
        fields = ('Country_code', 'Bank_number')


class CreateOperationForm(forms.ModelForm):
    """ Form for new transaction """

    Value_operation = forms.DecimalField(
                                label='Value operation',
                                initial=0,
                                widget=forms.NumberInput(
                                attrs={"class": "form_widget", "type": "number", "min": "0.01"}))
    
    class Meta:
        model = OperationModel
        exclude = ( 
                    'Balance_after_operation',
                    'Operation_date',
                    'Operation_employee',
                    'FK_Id_account')


