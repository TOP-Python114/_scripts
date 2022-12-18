from django.shortcuts import render
from django.http.request import HttpRequest

from pprint import pprint

from .forms import DepartmentForm
from .models import Faculty


def university_main_view(request: HttpRequest):
    return render(
        request,
        'faculties/main.html',
        {
            'object_list': Faculty.objects.all()
        }
    )


def faculty_view(request: HttpRequest, pk: int):
    if request.method == 'GET':
        print(f"'GET' branch of faculty_view()")
        return render(
            request,
            'faculties/faculty.html',
            {
                'object': Faculty.objects.get(pk=pk),
                'form': DepartmentForm()
            }
        )
    elif request.method == 'POST':
        print(f"'POST' branch of faculty_view()")

