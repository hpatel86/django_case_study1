from django.contrib import admin

from models import (
	Borrower,
	BorrowerLoan
)

# Register your models here.
admin.site.register(Borrower)
admin.site.register(BorrowerLoan)
