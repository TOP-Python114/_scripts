from pprint import pprint

from django.views.generic import ListView, DetailView, FormView

from string import ascii_letters as asl

from .forms import DepartmentAddForm, DepartmentDelForm
from .models import Faculty, Department


class UniversityMainView(ListView):
    model = Faculty
    template_name = 'faculties/main.html'


class FacultyView(FormView):
    form_class = None
    template_name = 'faculties/faculty.html'

    def get_success_url(self):
        return self.request.path

    def get_form_class(self):
        if 'SubmitAdd' in self.request.POST:
            return DepartmentAddForm
        elif 'SubmitDel' in self.request.POST:
            return DepartmentDelForm

    def get_context_data(self, **kwargs):
        context = {
            'object': Faculty.objects.get(pk=self.kwargs['pk'])
        }
        if self.request.method == 'GET':
            context['form_add'] = DepartmentAddForm()
            context['form_del'] = DepartmentDelForm()
        elif self.request.method == 'POST':
            context = super().get_context_data(**kwargs)
            context['form_add'] = context['form']
            context['form_del'] = context['form']
        return context

    def form_valid(self, form: DepartmentAddForm):
        if 'SubmitAdd' in self.request.POST:
            dep = Department(
                faculty_id=self.kwargs['pk'],
                **form.cleaned_data
            )
            dep.save()
        elif 'SubmitDel' in self.request.POST:
            qs = Department.objects.filter(name=form.cleaned_data['name'])
            if qs:
                dep: Department = qs[0]
                dep.delete()
        return super().form_valid(form)
