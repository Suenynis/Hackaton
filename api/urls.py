from django.urls import path
from . import views

urlpatterns = [ path('generate_images/', views.generate_images, name='generate_images'),
                path('generate-text/', views.generate_text_view, name='generate_text'),
]

