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
    worker_id = models.PositiveSmallIntegerField(
        verbose_name="ID работника", help_text="Укажите ID работника"
    )
    name = models.CharField(max_length=100, verbose_name="ФИО", help_text="Укажите ФИО")
    team_id = models.PositiveSmallIntegerField(
        verbose_name="ID бригады", help_text="Укажите ID бригады"
    )
    salary = models.PositiveIntegerField(
        verbose_name="Зарплата", help_text="Укажите зарплату"
    )
    specialization = models.CharField(
        max_length=20,
        choices=WORKER_SPECIALIZATION_CHOICES,
        verbose_name="Специализация",
        help_text="Укажите специализацию",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"
