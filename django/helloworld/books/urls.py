from django.urls import path

from .models import Publisher
from .views import index_view, publisher_view


urlpatterns = [
    path('', index_view),
]

for pub in Publisher.objects.all():
    urlpatterns += [
        path(pub.name_en, publisher_view, kwargs={'pub_obj': pub})
    ]
