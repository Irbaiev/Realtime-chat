from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Rooms(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.name


class Message(models.Model):
    room = models.ForeignKey(Rooms, related_name="messages", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("date_added",)

    def __str__(self) -> str:
        return f"Комната {self.room}, Пользователь {self.user}, Дата {self.date_added}"
