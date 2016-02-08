from django import forms
from django.contrib.auth.models import User
from registration.forms import RegistrationFormUniqueEmail

from models import (
	Borrower,
	BorrowerLoan,
)


class BorrowerRegistrationForm(RegistrationFormUniqueEmail):
	""" User and Borrower Registration form """

	phone_number = forms.IntegerField()
	full_name = forms.CharField(max_length=100)

	class Meta:
		model = User
		fields = [
			'username',
			'full_name',
			'phone_number',
			'email'
		]


class BorrowerLoanForm(forms.ModelForm):
	""" Borrower loan form setup """

	loan_amount = forms.IntegerField(min_value=10000)
	company_number = forms.IntegerField(min_value=1)
	loan_duration = forms.IntegerField(min_value=1)

	class Meta:
		model = BorrowerLoan
		exclude = ['borrower']
