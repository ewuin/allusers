from django.conf.urls import url
from . import views           # This line is new!


urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    url(r'^user_login/all.json$',views.all_json),
    url(r'^user_login/all.html$',views.all_html),
    url(r'^user_login/find$',views.find),
    url(r'^user_login/add$',views.add),
    ]
