from django.urls import path
from .views import index_view

app_name = 'landing_app'
urlpatterns = [
    path('', index_view, name='main_page'),
]
