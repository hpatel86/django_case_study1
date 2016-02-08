from django.shortcuts import render
from django.views import generic
from registration.backends.simple.views import RegistrationView

from forms import (
	BorrowerRegistrationForm,
	BorrowerLoanForm,
)

from models import Borrower


# Create your views here.
class IndexView(generic.TemplateView):
	template_name = 'loanrequest/index.html'


class LoanRequestView(generic.FormView):
	""" Loan Request form view """
	template_name = 'loanrequest/loanrequest_form.html'
	form_class = BorrowerLoanForm

	def form_valid(self, form):
		borrower_loan = form.save(commit=False)
		borrower_loan.borrower = Borrower.objects.get(user=self.request.user)
		borrower_loan.save()

		return render(
			self.request,
			'loanrequest/loanrequest_complete.html',
			dict()
		)


class BorrowerRegistrationView(RegistrationView):

	""" Override default one step simple registrtation"""

	form_class = BorrowerRegistrationForm

	def register(self, request, form_class):
		""" Register User and a Borrower """

		new_user = super(BorrowerRegistrationView, self).register(
			request, form_class
		)
		borrower = Borrower()
		borrower.user = new_user
		borrower.full_name = form_class.cleaned_data['full_name']
		borrower.phone_number = form_class.cleaned_data['phone_number']
		borrower.email = form_class.cleaned_data['email']
		borrower.save()

		return new_user

	def get_success_url(self, request, user):
		"""Redirect to request_loan handler on registration complete"""
		return 'request_loan'
