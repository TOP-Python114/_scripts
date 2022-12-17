from django.urls import path

from .models import Faculty
from .views import UniversityMainView, FacultyView


urlpatterns = [
    path('', UniversityMainView.as_view(), name='main'),
]

for faculty in Faculty.objects.all():
    urlpatterns += [
        path(
            f'{faculty.short_en}{faculty.id}/',
            FacultyView.as_view(),
            kwargs={'pk': faculty.id}
        ),
    ]
