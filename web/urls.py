from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^submit/kharj/$', views.submit_kharj, name = 'submit_kharj'),
	url(r'^submit/dakhl/$', views.submit_dakhl, name = 'submit_dakhl'),
]