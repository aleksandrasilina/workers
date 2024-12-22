from django.urls import path, re_path

from workers.apps import WorkersConfig
from workers.views import WorkerListAPIView, WorkerRetrieveAPIView, FileUploadView

app_name = WorkersConfig.name

urlpatterns = [
    path("team/<int:team_id>/WorkerList/", WorkerListAPIView.as_view(), name="workers-list"),
    path("worker/<int:worker_id>/", WorkerRetrieveAPIView.as_view(), name="workers-retrieve"),
    re_path(r'^upload/(?P<filename>[^/]+)$', FileUploadView.as_view()),
]
