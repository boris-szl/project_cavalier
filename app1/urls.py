from django.urls import path
from . import views


urlpatterns = [

	path('', views.validate, name="index"),
	path('home', views.validate, name="validate"),
	path('test', views.validate2, name="test"),
	path('error', views.validate2, name='error')
]
