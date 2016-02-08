from django.db import models
from django.contrib.auth.models import User
from django.core.validators import (
	MaxValueValidator,
	MinValueValidator
)

from consts import SECTORS

class Borrower(models.Model):
	full_name = models.CharField('Name', max_length=100)
	phone_number = models.BigIntegerField('Phone Number')
	email = models.EmailField(max_length=50)
	user = models.OneToOneField(User)


class BorrowerLoan(models.Model):
	borrower = models.ForeignKey(Borrower)
	company_name = models.CharField('Company Name', max_length=200)
	address = models.CharField('Address', max_length=200)
	company_number = models.PositiveIntegerField(
		'Company Number',
		unique=True,
		validators=[
			MinValueValidator(1),
			MaxValueValidator(99999999),
		]
	)
	sector = models.CharField(
		'Sector',
		max_length=50,
		choices=SECTORS
	)
	loan_amount = models.PositiveIntegerField(
		'Loan Amount (GBP)',
		validators=[
			MinValueValidator(10000),
			MaxValueValidator(100000),
		]
	)
	loan_duration = models.PositiveSmallIntegerField(
		'Loan Duration (Number of Days)'
	)
	loan_reason = models.TextField('Loan Reason')
