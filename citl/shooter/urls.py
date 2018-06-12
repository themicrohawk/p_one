# shooter/urls.py

from django.urls import path

from . import views

app_name = 'shooter'

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),		# /shooter/
	path('test', views.TestView.as_view(), name='test'),	# /shooter/test/
	path('<int:year>/season/', views.SeasonView.as_view(), name='season'),	# /shooter/<year>/season
	path('<int:year>/<team>/team/', views.TeamView.as_view(), name='team'),	# /shooter/<year>/<team>/team
]