from django.urls import path
from . import views
urlpatterns = [
    path('image/',views.uploadImageView),
    path('describe/<image_id>/',views.imageDescriveView),
]
