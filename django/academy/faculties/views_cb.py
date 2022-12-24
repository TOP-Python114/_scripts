from django.views.generic import ListView, DetailView, FormView

from string import ascii_letters as asl

from .forms import DepartmentAddForm
from .models import Faculty, Department


class UniversityMainView(ListView):
    model = Faculty
    template_name = 'faculties/main.html'


class FacultyView(FormView):
    form_class = DepartmentAddForm
    template_name = 'faculties/faculty.html'

    def get_success_url(self):
        return self.request.path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = Faculty.objects.get(pk=self.kwargs['pk'])
        context['form_add'] = context['form']
        return context

    def form_valid(self, form: DepartmentAddForm):
        dep = Department(
            faculty_id=self.kwargs['pk'],
            **form.cleaned_data
        )
        dep.save()
        return super().form_valid(form)
