from django.db import models


class GuestBook(models.Model):

    ACTIVE = "active"
    BLOCKED = "blocked"

    STATUS_CHOICES = [
        (ACTIVE, 'Активно'),
        (BLOCKED, 'Заблокировано'),
    ]

    name = models.CharField(max_length=200, null=False, blank=False, verbose_name="Имя гостя")
    mail = models.EmailField(max_length=254, null=False, blank=False, verbose_name="Почта гостя")
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Текст записи")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=ACTIVE)

    def __str__(self):
        return "{}. {}".format(self.pk, self.name)
