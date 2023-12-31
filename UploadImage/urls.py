from django.urls import path
from . import views
urlpatterns = [
    path('image/',views.uploadImageView,name='uploadDashboard'),
    path('describe/<image_id>/',views.imageDescriveView),
    path('delete/<image_id>/',views.imageDelete),
    path('update/<image_id>/',views.imageUpdateView),
]
