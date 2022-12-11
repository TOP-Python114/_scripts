from django.urls import path

from .views import index, publisher_view
from .models import Publisher

urlpatterns = [
    path('', index),
]

for pub in Publisher.objects.all():
    urlpatterns += [
        path(pub.name_en, publisher_view, kwargs={'pub_obj': pub})
    ]
