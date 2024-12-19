from rest_framework.generics import ListAPIView, RetrieveAPIView

from workers.models import Worker
from workers.serializerrs import WorkerSerializer


class WorkerListAPIView(ListAPIView):
    """Список работников."""

    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class WorkerRetrieveAPIView(RetrieveAPIView):
    """Информация о работнике."""

    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
