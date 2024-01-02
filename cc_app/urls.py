from cc_app import views
from django.urls import path


urlpatterns = [
    path(
        "video-upload/<str:filename>/",
        views.FileUploadView.as_view(),
        name="video_upload",
    ),
]
