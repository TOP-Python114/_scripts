from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect

from pprint import pprint

from .forms import DepartmentAddForm, DepartmentDelForm
from .models import Faculty, Department


styles = [
    'faculties/styles/faculties.css',
]


def university_main_view(request: HttpRequest):
    return render(request, 'bs_faculties/main.html')


def faculties_list_view(request: HttpRequest):
    return render(
        request,
        'bs_faculties/faculties_list.html',
        {
            # 'styles': styles,
            'object_list': Faculty.objects.all(),
        }
    )


def faculty_view(request: HttpRequest, pk: int):
    # print(f'{act = }')
    if request.method == 'GET':
        faculty = Faculty.objects.get(pk=pk)
        # lstyles = styles + ['faculties/styles/faculty.css']
        return render(
            request,
            'bs_faculties/faculty.html',
            {
                # 'styles': lstyles,
                'page_title': faculty.name,
                'object': faculty,
                'form_add': DepartmentAddForm(),
                'form_del': DepartmentDelForm(),
            }
        )
    elif request.method == 'POST':
        if 'SubmitAdd' in request.POST:
            form = DepartmentAddForm(request.POST)
            if form.is_valid():
                dep = Department(
                    faculty_id=pk,
                    **form.cleaned_data
                )
                dep.save()
        elif 'SubmitDel' in request.POST:
            form = DepartmentDelForm(request.POST)
            if form.is_valid():
                qs = Department.objects.filter(name=form.cleaned_data['name'])
                if qs:
                    dep: Department = qs
                    dep.delete()
        url = request.path.removesuffix('add').removesuffix('del')
        return redirect(url)
