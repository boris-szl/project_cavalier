from django.urls import path
from . import views


urlpatterns = [
	path('', views.defaultDataDisplayIndex, name=""),
	path('', views.getRoicDataIndex, name=""),
	path('index', views.defaultDataDisplayIndex, name="index"),
	path('index', views.getRoicDataIndex, name="index"),
	path('test', views.defaultDataDisplayDemo, name="test"),
	path('test', views.getRoicDataDemo, name="test"),
	path('error', views.getRoicDataIndex, name='error'),
	path('error', views.getRoicDataDemo, name='error'),
	path('test', views.ajax_view, name="test"),
]
