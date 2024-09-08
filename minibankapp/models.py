# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import (RegexValidator, MinValueValidator)
from .validators import (validator_free_balance, validator_number_iban)


""" Customer Model """
class CustomerModel(models.Model):

    Id_customer = models.AutoField(
                                primary_key=True,
                                verbose_name='Id customer')
    First_name = models.CharField(
                                max_length=100,
                                verbose_name='First name')
    Last_name = models.CharField(
                                max_length=100,
                                verbose_name='Last name')
    Street = models.CharField(
                                max_length=100,
                                verbose_name='Street')
    House = models.CharField(
                                max_length=10,
                                verbose_name='House')
    Apartment = models.CharField(
                                blank=True,
                                max_length=10,
                                verbose_name='Apartment')
    Postal_code = models.CharField(
                                max_length=6,
                                validators=[RegexValidator(regex='^[0-9]{2}-[0-9]{3}$')],
                                verbose_name='Postal code')
    City = models.CharField(
                                max_length=100,
                                verbose_name='City')
    Pesel = models.CharField(
                                max_length=11,
                                validators=[RegexValidator(regex='^[0-9]{11}$')],
                                verbose_name='PESEL')
    Birth_date = models.DateField(
                                verbose_name='Birth day')
    Birth_city = models.CharField(
                                max_length=100,
                                verbose_name='Birth city')
    Identification = models.CharField(
                                max_length=9,
                                verbose_name='Identification')
    Created_date = models.DateTimeField(
                                auto_now_add=True,
                                verbose_name='Created date')
    Created_employee = models.CharField(
                                max_length=50,
                                verbose_name='Employee')

    def save(self, *args, **kwargs):
        self.Identification = self.Identification.upper()
        super().save(*args, **kwargs)


""" Account Model """
class AccountModel(models.Model):

    Id_account = models.AutoField(
                                primary_key=True,
                                verbose_name='Id account')
    Number_IBAN = models.CharField(
                                max_length=28,
                                blank=True,
                                validators=[validator_number_iban],
                                verbose_name='IBAN number')
    Balance = models.DecimalField(
                                max_digits=12,
                                decimal_places=2,
                                default=0,
                                verbose_name='Balance')
    Debit = models.DecimalField(
                                max_digits=12,
                                decimal_places=2,
                                default=0,
                                validators=[MinValueValidator(0)],
                                verbose_name='Debit')
    Free_balance = models.DecimalField(
                                max_digits=12,
                                decimal_places=2,
                                default=0,
                                validators=[validator_free_balance],
                                verbose_name='Free balance')
    Percent = models.DecimalField(
                                max_digits=4,
                                decimal_places=2,
                                default=0,
                                validators=[MinValueValidator(0)],
                                verbose_name='Percent')
    Created_date = models.DateTimeField(
                                auto_now_add=True,
                                verbose_name='Created date')
    Created_employee = models.CharField(
                                max_length=50,
                                verbose_name='Employee')

    FK_Id_account_type = models.ForeignKey('minibankapp.AccountTypeModel', on_delete=models.PROTECT)
    FK_Id_customer = models.ForeignKey('minibankapp.CustomerModel', on_delete=models.PROTECT)


""" AccountType Model """
class AccountTypeModel(models.Model):

    Id_account_type = models.CharField(
                                primary_key=True,
                                max_length=4,
                                verbose_name='Id account type',
                                validators=[RegexValidator(regex='^[a-zA-Z]{1}-[0-9]{2}$')])
    Description = models.CharField(
                                max_length=100,
                                verbose_name='Description')
    Subaccount = models.CharField(
                                max_length=6,
                                verbose_name='Subaccount',
                                validators=[RegexValidator(regex='^[0-9]{6}$')])
    Percent = models.DecimalField(
                                max_digits=4,
                                decimal_places=2,
                                default=0,
                                verbose_name='Percent',
                                validators=[MinValueValidator(0)])

    def save(self, *args, **kwargs):
        self.Id_account_type = self.Id_account_type.upper()
        super().save(*args, **kwargs)

    @property
    def property_get_pk(self):
        return self.Id_account_type


""" Parameter Model """
class ParameterModel(models.Model):

    Id_parameter = models.AutoField(
                                primary_key=True)
    Country_code = models.CharField(
                                max_length=2,
                                validators=[RegexValidator(regex='^[a-zA-Z]{2}$')])
    Bank_number = models.CharField(
                                max_length=8,
                                validators=[RegexValidator(regex='^[0-9]{8}$')])

    def save(self, *args, **kwargs):
        self.Country_code = self.Country_code.upper()
        super().save(*args, **kwargs)


""" Operation Model """
class OperationModel(models.Model):

    type_choice = [
                    ('', '--------'),
                    (1, 'Deposit'),
                    (2, 'Withdrawal'),
                    (3, 'Interest')]

    Id_operation = models.AutoField(
                                primary_key=True,
                                verbose_name='Id operation')
    Type_operation = models.IntegerField(
                                choices=type_choice,
                                verbose_name='Type operation')
    Value_operation = models.DecimalField(
                                max_digits=12,
                                decimal_places=2,
                                default=0,
                                verbose_name='Value operation')
    Balance_after_operation = models.DecimalField(
                                max_digits=12,
                                decimal_places=2,
                                verbose_name='Balance after operation')
    Operation_date = models.DateTimeField(
                                auto_now_add=True,
                                verbose_name='Operation date')
    Operation_employee = models.CharField(
                                max_length=50,
                                verbose_name='Employee')
    
    FK_Id_account = models.ForeignKey('minibankapp.AccountModel', on_delete=models.PROTECT)


""" Log Model """
class LogModel(models.Model):

    Id_log = models.AutoField(
                                primary_key=True)
    Date_log = models.DateTimeField(
                                auto_now_add=True)
    Action_log = models.CharField(
                                max_length=50)
    Function_log = models.CharField(
                                max_length=50)
    Duration_log = models.DecimalField(
                                max_digits=12,
                                decimal_places=6)
    Data_log = models.CharField(
                                max_length=250,
                                blank=True)
    User_log = models.CharField(
                                max_length=50)
    Status_log = models.CharField(
                                max_length=20)
