import io, csv

from django.shortcuts import render, redirect
from django.forms import HiddenInput
from django.urls import reverse_lazy

from funky_sheets.formsets import HotView

from .models import Employee
from django.contrib.auth.decorators import login_required


@login_required
def Import_csv(request):
    if request.method == 'POST' and request.FILES['employeefile']:
        user = request.user  # get the current login user details
        for file in request.FILES.getlist('employeefile'):
            paramFile = io.TextIOWrapper(file)
            portfolio1 = csv.DictReader(paramFile)
            list_of_dict = list(portfolio1)
            objs = [
                Employee(
                    user=user,
                    empcode=row['Empcode'],
                    firstname=row['firstname'],

                )
                for row in list_of_dict
            ]
            try:
                msg = Employee.objects.bulk_create(objs)
                return redirect('user:homepage')
            except Exception as e:
                returnmsg = {"status_code": 500}

    return render(request, 'importexcel.html', {})


class CreateEmployeeView(HotView):
    # Define model to be used by the view
    model = Employee
    # Define template
    template_name = 'examples/create.html'
    # Define custom characters/strings for checked/unchecked checkboxes
    checkbox_checked = 'yes'  # default: true
    checkbox_unchecked = 'no'  # default: false
    # Define prefix for the formset which is constructed from Handsontable spreadsheet on submission
    prefix = 'table'
    # Define success URL
    success_url = reverse_lazy('user:homepage')
    # Define fields to be included as columns into the Handsontable spreadsheet
    fields = (
        'empcode',
        'firstname',
    )
    # # Define extra formset factory kwargs
    factory_kwargs = {
        'widgets': {
            'user': HiddenInput(
                attrs={'class': 'poi-input'}
            )
        }
    }
    # Define Handsontable settings as defined in Handsontable docs
    hot_settings = {
        'contextMenu': 'true',
        'autoWrapRow': 'true',
        'rowHeaders': 'true',
        'contextMenu': 'true',
        'search': 'true',
        # When value is dictionary don't wrap it in quotes
        'headerTooltips': {
            'rows': 'false',
            'columns': 'true'
        },
    }

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a formset instance with the passed
        POST variables and then checked for validity.
        """
        formset = self.construct_formset()
        if formset.is_valid():
            new_instances = formset.save(commit=False)
            for new_instance in new_instances:
                new_instance.user = request.user
                new_instance.save()
            return self.formset_valid(formset)
        else:
            return self.formset_invalid(formset)
