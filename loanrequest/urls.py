from django.conf.urls import (
	url,
	include
)

import views

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'request_loan', views.LoanRequestView.as_view(), name='request_loan'),
	url(
		r'^accounts/register/$',
		views.BorrowerRegistrationView.as_view(),
		name='registration_register'
	),
	url(r'^accounts/', include('registration.backends.simple.urls')),
]
