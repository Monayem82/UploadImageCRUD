from django.urls import path
from . import views
urlpatterns = [
    path('image/',views.uploadImageView,name='uploadDashboard'),
    path('describe/<image_id>/',views.imageDescriveView),
]
