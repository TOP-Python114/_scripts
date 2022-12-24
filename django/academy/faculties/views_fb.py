from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect

from pprint import pprint

from .forms import DepartmentAddForm, DepartmentDelForm
from .models import Faculty, Department


def university_main_view(request: HttpRequest):
    return render(
        request,
        'faculties/main.html',
        {
            'object_list': Faculty.objects.all()
        }
    )


def faculty_view(request: HttpRequest, pk: int):
    # print(f'{act = }')
    if request.method == 'GET':
        return render(
            request,
            'faculties/faculty.html',
            {
                'object': Faculty.objects.get(pk=pk),
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
