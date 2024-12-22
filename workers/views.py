from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from workers.models import Worker
from workers.serializerrs import WorkerSerializer
from workers.services import excel_to_json_worker


class WorkerListAPIView(ListAPIView):
    """Возвращает список работников в бригаде."""

    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

    def get_queryset(self, *args, **kwargs):
        super().get_queryset(*args, **kwargs)
        return Worker.objects.filter(team_id=self.kwargs.get('team_id'))


class WorkerRetrieveAPIView(RetrieveAPIView):
    """Возвращает описание мастера."""

    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    lookup_field = "worker_id"


class FileUploadView(APIView):
    """Загружает файл excel и сохраняет данные работников в БД."""

    parser_classes = [FileUploadParser]

    def put(self, request, filename, format=None):
        try:
            file_obj = request.data['file']
            file_obj_json = excel_to_json_worker(file_obj)

            for worker in file_obj_json:
                Worker.objects.get_or_create(**worker)

            return Response({'status': 'success', 'message': 'File uploaded.'})

        except Exception as e:
            error_message = str(e)

            return Response({'status': 'error', 'message': error_message})
