from django.urls import path

from workers.views import WorkerListAPIView, WorkerRetrieveAPIView

urlpatterns = [
    path("team/<int:pk>/WorkerList/", WorkerListAPIView.as_view(), name="workers-list"),
    path("worker/<int:pk>/", WorkerRetrieveAPIView.as_view(), name="workers-retrieve"),
]
