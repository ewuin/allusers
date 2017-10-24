from django.conf.urls import url
from . import views           # This line is new!


urlpatterns = [
    url(r'^notes$', views.index),     # This line has changed!
    url(r'^add$',views.add),
    url(r'^delete$',views.delete),
    url(r'^refresh$',views.refresh),
    ]
