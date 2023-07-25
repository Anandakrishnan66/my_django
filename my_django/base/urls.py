from django.urls import path
from . import views

app_name="base"

urlpatterns=[
    path("",views.detail,name="detail"),
    path("runner/",views.runner,name="runner"),
    path("fruit/<int:fruit_id>",views.fruit,name="fruit")
]
