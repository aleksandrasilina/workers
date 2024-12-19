from django.db import models


class Worker(models.Model):
    WORKER_SPECIALIZATION_CHOICES = (
        (
            "rough",
            "черновая",
        ),
        (
            "fine",
            "чистовая",
        ),
        (
            "foreman",
            "бригадир",
        ),
        (
            "taskmaster",
            "прораб",
        ),
    )

    name = models.CharField(max_length=100, verbose_name="ФИО",
                            help_text="Укажите ФИО")
    team_number = models.PositiveSmallIntegerField(verbose_name="Номер бригады",
                                                   help_text="Укажите номер бригады")
    salary = models.PositiveIntegerField(verbose_name="Зарплата",
                                         help_text="Укажите зарплату")
    specialization = models.CharField(max_length=20, choices=WORKER_SPECIALIZATION_CHOICES,
                                      verbose_name="Специализация",
                                      help_text="Укажите специализацию")
