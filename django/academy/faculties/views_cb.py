from django.views.generic import ListView, DetailView

from .models import Faculty


class UniversityMainView(ListView):
    model = Faculty
    template_name = 'faculties/main.html'


class FacultyView(DetailView):
    model = Faculty
    template_name = 'faculties/faculty.html'

