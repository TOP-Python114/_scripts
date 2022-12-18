from django.urls import path

from .models import Faculty
from .views_fb import university_main_view, faculty_view
from .views_cb import UniversityMainView, FacultyView


FUNCTIONS_OR_CLASS = 0

if FUNCTIONS_OR_CLASS:
    university_main_view = UniversityMainView.as_view()
    faculty_view = FacultyView.as_view()


urlpatterns = [
    path('', university_main_view, name='main'),
]

for faculty in Faculty.objects.all():
    urlpatterns += [
        path(
            f'{faculty.short_en}{faculty.id}/',
            faculty_view,
            kwargs={'pk': faculty.id}
        ),
    ]
