from django.urls import path

from . import views
app_name = 'babystats'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:category_id>/', views.detail, name='detail'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('<int:category_id>/running/<int:event_id>/', views.running, name='running'),
    path('<int:category_id>/end_event/<int:event_id>/', views.end_event, name='end_event'),
    path('<int:category_id>/create_new/', views.create_new, name='create_new'),
    path('<int:category_id>/saveme/<int:event_id>/', views.saveme, name='saveme'),
#    path('neu', views.neu, name='neu'),
    path('click', views.click, name='click'),
    # ex: /category/5/results/
    path('<int:category_id>/results/', views.results, name='results'),
    # ex: /category/5/vote/
    path('<int:category_id>/vote/', views.vote, name='vote'),

]
